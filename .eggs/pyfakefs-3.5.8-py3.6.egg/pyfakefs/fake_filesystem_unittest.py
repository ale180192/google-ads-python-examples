# Copyright 2014 Altera Corporation. All Rights Reserved.
# Copyright 2015-2017 John McGehee
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""This module provides a base class derived from `unittest.TestClass`
for unit tests using the :py:class:`pyfakefs` module.

`fake_filesystem_unittest.TestCase` searches `sys.modules` for modules
that import the `os`, `io`, `path` `shutil`, and `pathlib` modules.

The `setUpPyfakefs()` method binds these modules to the corresponding fake
modules from `pyfakefs`.  Further, the `open()` built-in is bound to a fake
`open()`.  In Python 2, built-in `file()` is similarly bound to the fake
`open()`.

It is expected that `setUpPyfakefs()` be invoked at the beginning of the
derived class' `setUp()` method.  There is no need to add anything to the
derived class' `tearDown()` method.

During the test, everything uses the fake file system and modules.  This means
that even in your test fixture, familiar functions like `open()` and
`os.makedirs()` manipulate the fake file system.

Existing unit tests that use the real file system can be retrofitted to use
pyfakefs by simply changing their base class from `:py:class`unittest.TestCase`
to `:py:class`pyfakefs.fake_filesystem_unittest.TestCase`.
"""
import doctest
import inspect
import os
import sys
import tempfile
import unittest
import zipfile  # noqa: F401 make sure it gets correctly stubbed, see #427

from pyfakefs.helpers import IS_PY2, IS_PYPY

from pyfakefs.deprecator import Deprecator

try:
    from importlib.machinery import ModuleSpec
except ImportError:
    ModuleSpec = object

try:
    # python >= 3.4
    from importlib import reload
except ImportError:
    try:
        # python 3.0 - 3.3
        from imp import reload
    except ImportError:
        # python 2 - reload is built-in
        pass

from pyfakefs import fake_filesystem
from pyfakefs import fake_filesystem_shutil
from pyfakefs import mox3_stubout
from pyfakefs.extra_packages import pathlib, pathlib2, use_scandir

if pathlib:
    from pyfakefs import fake_pathlib

if use_scandir:
    from pyfakefs import fake_scandir

if sys.version_info < (3, ):
    import __builtin__ as builtins  # pylint: disable=import-error
else:
    import builtins

OS_MODULE = 'nt' if sys.platform == 'win32' else 'posix'
PATH_MODULE = 'ntpath' if sys.platform == 'win32' else 'posixpath'
BUILTIN_MODULE = '__builtin__'


def load_doctests(loader, tests, ignore, module,
                  additional_skip_names=None,
                  use_dynamic_patch=True,
                  modules_to_reload=None,
                  modules_to_patch=None):  # pylint: disable=unused-argument
    """Load the doctest tests for the specified module into unittest.
        Args:
            loader, tests, ignore : arguments passed in from `load_tests()`
            module: module under test
            remaining args: see :py:class:`TestCase` for an explanation

    File `example_test.py` in the pyfakefs release provides a usage example.
    """
    _patcher = Patcher(additional_skip_names=additional_skip_names,
                       use_dynamic_patch=use_dynamic_patch,
                       modules_to_reload=modules_to_reload,
                       modules_to_patch=modules_to_patch)
    globs = _patcher.replace_globs(vars(module))
    tests.addTests(doctest.DocTestSuite(module,
                                        globs=globs,
                                        setUp=_patcher.setUp,
                                        tearDown=_patcher.tearDown))
    return tests


class TestCaseMixin(object):
    """Test case mixin that automatically replaces file-system related
    modules by fake implementations.

    Attributes:
        additional_skip_names: names of modules inside of which no module
            replacement shall be performed, in addition to the names in
            :py:attr:`fake_filesystem_unittest.Patcher.SKIPNAMES`.
        modules_to_reload: A list of modules that need to be reloaded
            to be patched dynamically; may be needed if the module
            imports file system modules under an alias

            .. note:: This is done independently of `use_dynamic_patch`

            .. caution:: Reloading modules may have unwanted side effects.
        use_dynamic_patch: If `True`, dynamic patching after setup is used
            (for example for modules loaded locally inside of functions).
            Can be switched off if it causes unwanted side effects.
        modules_to_patch: A dictionary of fake modules mapped to the
            fully qualified patched module names. Can be used to add patching
            of modules not provided by `pyfakefs`.

    If you specify some of these attributes here and you have DocTests,
    consider also specifying the same arguments to :py:func:`load_doctests`.

    Example usage in derived test classes::

        from unittest import TestCase
        from fake_filesystem_unittest import TestCaseMixin

        class MyTestCase(TestCase, TestCaseMixin):
            def __init__(self, methodName='runTest'):
                super(MyTestCase, self).__init__(
                    methodName=methodName,
                    additional_skip_names=['posixpath'])

        import sut

        class AnotherTestCase(TestCase, TestCaseMixin):
            def __init__(self, methodName='runTest'):
                super(MyTestCase, self).__init__(
                    methodName=methodName, modules_to_reload=[sut])
    """

    additional_skip_names = None
    modules_to_reload = None
    use_dynamic_patch = True
    modules_to_patch = None

    @property
    def fs(self):
        return self._stubber.fs

    def setUpPyfakefs(self,
                      additional_skip_names=None,
                      use_dynamic_patch=None,
                      modules_to_reload=None,
                      modules_to_patch=None):
        """Bind the file-related modules to the :py:class:`pyfakefs` fake file
        system instead of the real file system.  Also bind the fake `open()`
        function, and on Python 2, the `file()` function.

        Invoke this at the beginning of the `setUp()` method in your unit test
        class.
        For the arguments, see the `TestCaseMixin` attribute description.
        If any of the arguments is not None, it overwrites the settings for
        the current test case. Settings the arguments here may be a more
        convenient way to adapt the setting than overwriting `__init__()`.
        """
        if additional_skip_names is None:
            additional_skip_names = self.additional_skip_names
        if use_dynamic_patch is None:
            use_dynamic_patch = self.use_dynamic_patch
        if modules_to_reload is None:
            modules_to_reload = self.modules_to_reload
        if modules_to_patch is None:
            modules_to_patch = self.modules_to_patch
        self._stubber = Patcher(
            additional_skip_names=additional_skip_names,
            use_dynamic_patch=use_dynamic_patch,
            modules_to_reload=modules_to_reload,
            modules_to_patch=modules_to_patch)

        self._stubber.setUp()
        self.addCleanup(self._stubber.tearDown)

    def pause(self):
        """Pause the patching of the file system modules until `resume` is
        called. After that call, all file system calls are executed in the
        real file system.
        Calling pause() twice is silently ignored.

        """
        self._stubber.pause()

    def resume(self):
        """Resume the patching of the file system modules if `pause` has
        been called before. After that call, all file system calls are
        executed in the fake file system.
        Does nothing if patching is not paused.
        """
        self._stubber.resume()


class TestCase(unittest.TestCase, TestCaseMixin):
    """Test case class that automatically replaces file-system related
    modules by fake implementations. Inherits :py:class:`TestCaseMixin`.

    The arguments are explained in :py:class:`TestCaseMixin`.
    """

    def __init__(self, methodName='runTest',
                 additional_skip_names=None,
                 modules_to_reload=None,
                 use_dynamic_patch=True,
                 modules_to_patch=None):
        """Creates the test class instance and the patcher used to stub out
        file system related modules.

        Args:
            methodName: The name of the test method (same as in
                unittest.TestCase)
        """
        super(TestCase, self).__init__(methodName)

        self.additional_skip_names = additional_skip_names
        self.modules_to_reload = modules_to_reload
        self.use_dynamic_patch = use_dynamic_patch
        self.modules_to_patch = modules_to_patch

    @Deprecator('add_real_file')
    def copyRealFile(self, real_file_path, fake_file_path=None,
                     create_missing_dirs=True):
        """Add the file `real_file_path` in the real file system to the same
        path in the fake file system.

        **This method is deprecated** in favor of
        :py:meth:`FakeFilesystem..add_real_file`.
        `copyRealFile()` is retained with limited functionality for backward
        compatibility only.

        Args:
          real_file_path: Path to the file in both the real and fake
            file systems
          fake_file_path: Deprecated.  Use the default, which is
            `real_file_path`.
            If a value other than `real_file_path` is specified, a `ValueError`
            exception will be raised.
          create_missing_dirs: Deprecated.  Use the default, which creates
            missing directories in the fake file system.  If `False` is
            specified, a `ValueError` exception is raised.

        Returns:
          The newly created FakeFile object.

        Raises:
          IOError: If the file already exists in the fake file system.
          ValueError: If deprecated argument values are specified.

        See:
          :py:meth:`FakeFileSystem.add_real_file`
        """
        if fake_file_path is not None and real_file_path != fake_file_path:
            raise ValueError("CopyRealFile() is deprecated and no longer "
                             "supports different real and fake file paths")
        if not create_missing_dirs:
            raise ValueError("CopyRealFile() is deprecated and no longer "
                             "supports NOT creating missing directories")
        return self._stubber.fs.add_real_file(real_file_path, read_only=False)

    @DeprecationWarning
    def tearDownPyfakefs(self):
        """This method is deprecated and exists only for backward
        compatibility. It does nothing.
        """
        pass


class Patcher(object):
    """
    Instantiate a stub creator to bind and un-bind the file-related modules to
    the :py:mod:`pyfakefs` fake modules.

    The arguments are explained in :py:class:`TestCaseMixin`.

    :py:class:`Patcher` is used in :py:class:`TestCaseMixin`.
    :py:class:`Patcher` also works as a context manager for other tests::

        with Patcher():
            doStuff()
    """
    '''Stub nothing that is imported within these modules.
    `sys` is included to prevent `sys.path` from being stubbed with the fake
    `os.path`.
    '''
    SKIPMODULES = {None, fake_filesystem, fake_filesystem_shutil, sys}
    assert None in SKIPMODULES, ("sys.modules contains 'None' values;"
                                 " must skip them.")

    IS_WINDOWS = sys.platform in ('win32', 'cygwin')

    SKIPNAMES = {'os', 'path', 'io', 'genericpath', OS_MODULE, PATH_MODULE}
    if pathlib:
        SKIPNAMES.add('pathlib')
    if pathlib2:
        SKIPNAMES.add('pathlib2')

    # exclude the PyCharm debugger as it needs to access the real fs
    if IS_PY2 and os.environ.get('PYCHARM_HOSTED'):
        SKIPNAMES.add('pydevd')

    def __init__(self, additional_skip_names=None,
                 modules_to_reload=None, use_dynamic_patch=True,
                 modules_to_patch=None):
        """For a description of the arguments, see TestCase.__init__"""

        self._skipNames = self.SKIPNAMES.copy()
        # save the original open function for use in pytest plugin
        self.original_open = open
        self.fake_open = None

        if additional_skip_names is not None:
            self._skipNames.update(additional_skip_names)

        self.modules_to_reload = [tempfile]
        if modules_to_reload is not None:
            self.modules_to_reload.extend(modules_to_reload)
        self._use_dynamic_patch = use_dynamic_patch

        # Attributes set by _findModules()

        # IMPORTANT TESTING NOTE: Whenever you add a new module below, test
        # it by adding an attribute in fixtures/module_with_attributes.py
        # and a test in fake_filesystem_unittest_test.py, class
        # TestAttributesWithFakeModuleNames.
        self._fake_module_classes = {
            'os': fake_filesystem.FakeOsModule,
            'shutil': fake_filesystem_shutil.FakeShutilModule,
            'io': fake_filesystem.FakeIoModule,
        }
        if IS_PY2 or IS_PYPY:
            # in Python 2 io.open, the module is referenced as _io
            self._fake_module_classes['_io'] = fake_filesystem.FakeIoModule

        # class modules maps class names against a list of modules they can
        # be contained in - this allows for alternative modules like
        # `pathlib` and `pathlib2`
        self._class_modules = {}
        if pathlib:
            self._class_modules['Path'] = []
            if pathlib:
                self._fake_module_classes[
                    'pathlib'] = fake_pathlib.FakePathlibModule
                self._class_modules['Path'].append('pathlib')
            if pathlib2:
                self._fake_module_classes[
                    'pathlib2'] = fake_pathlib.FakePathlibModule
                self._class_modules['Path'].append('pathlib2')
            self._fake_module_classes[
                'Path'] = fake_pathlib.FakePathlibPathModule
        if use_scandir:
            self._fake_module_classes[
                'scandir'] = fake_scandir.FakeScanDirModule

        if modules_to_patch is not None:
            for name, fake_module in modules_to_patch.items():
                self._fake_module_classes[name] = fake_module

        # handle patching function imported separately like
        # `from os import stat`
        # each patched function name has to be looked up separately
        self._fake_module_functions = {}
        for mod_name, fake_module in self._fake_module_classes.items():
            if (hasattr(fake_module, 'dir') and
                    inspect.isfunction(fake_module.dir)):
                for fct_name in fake_module.dir():
                    module_attr = (getattr(fake_module, fct_name), mod_name)
                    self._fake_module_functions.setdefault(
                        fct_name, {})[mod_name] = module_attr
                    if mod_name == 'os':
                        self._fake_module_functions.setdefault(
                            fct_name, {})[OS_MODULE] = module_attr

        # special handling for functions in os.path
        fake_module = fake_filesystem.FakePathModule
        for fct_name in fake_module.dir():
            module_attr = (getattr(fake_module, fct_name), PATH_MODULE)
            self._fake_module_functions.setdefault(
                fct_name, {})['genericpath'] = module_attr
            self._fake_module_functions.setdefault(
                fct_name, {})[PATH_MODULE] = module_attr

        # Attributes set by _refresh()
        self._modules = {}
        self._fct_modules = {}
        self._open_functions = {}
        self._stubs = None
        self.fs = None
        self.fake_modules = {}
        self._dyn_patcher = None

        # _isStale is set by tearDown(), reset by _refresh()
        self._isStale = True
        self._patching = False

    def __enter__(self):
        """Context manager for usage outside of
        fake_filesystem_unittest.TestCase.
        Ensure that all patched modules are removed in case of an
        unhandled exception.
        """
        self.setUp()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.tearDown()

    def _find_modules(self):
        """Find and cache all modules that import file system modules.
        Later, `setUp()` will stub these with the fake file system
        modules.
        """

        def is_fs_module(mod, name):
            try:
                return (inspect.ismodule(mod) and
                        mod.__name__ in module_names
                        or inspect.isclass(mod) and
                        mod.__module__ in self._class_modules.get(name, []))
            except AttributeError:
                # handle cases where the module has no __name__ or __module__
                # attribute - see #460
                return False

        def is_open_function(fct):
            try:
                return ((inspect.isfunction(fct) or
                         inspect.isbuiltin(fct)) and
                        fct.__name__ == 'open' and
                        fct.__module__ == BUILTIN_MODULE)
            except AttributeError:
                return False

        def is_fs_function(fct):
            try:
                return ((inspect.isfunction(fct) or
                         inspect.isbuiltin(fct)) and
                        fct.__name__ in self._fake_module_functions and
                        fct.__module__ in self._fake_module_functions[
                            fct.__name__])
            except AttributeError:
                # handle cases where the function has no __name__ or __module__
                # attribute
                return False

        module_names = list(self._fake_module_classes.keys()) + [PATH_MODULE]
        for name, module in set(sys.modules.items()):
            try:
                if (module in self.SKIPMODULES or
                        not inspect.ismodule(module) or
                        module.__name__.split('.')[0] in self._skipNames):
                    continue
            except AttributeError:
                # workaround for some py (part of pytest) versions
                # where py.error has no __name__ attribute
                # see https://github.com/pytest-dev/py/issues/73
                continue

            modules = {name: mod for name, mod in module.__dict__.items()
                       if is_fs_module(mod, name)}
            for name, mod in modules.items():
                self._modules.setdefault(name, set()).add((module,
                                                           mod.__name__))
            functions = {name: fct for name, fct in module.__dict__.items()
                         if is_fs_function(fct)}
            for name, fct in functions.items():
                self._fct_modules.setdefault(
                    (name, fct.__name__, fct.__module__), set()).add(module)

            if IS_PY2:
                open_fcts = {name for name, fct in module.__dict__.items()
                             if is_open_function(fct)}
                for name in open_fcts:
                    self._open_functions.setdefault(name, set()).add(module)


    def _refresh(self):
        """Renew the fake file system and set the _isStale flag to `False`."""
        if self._stubs is not None:
            self._stubs.smart_unset_all()
        self._stubs = mox3_stubout.StubOutForTesting()

        self.fs = fake_filesystem.FakeFilesystem(patcher=self)
        for name in self._fake_module_classes:
            self.fake_modules[name] = self._fake_module_classes[name](self.fs)
        self.fake_modules[PATH_MODULE] = self.fake_modules['os'].path
        self.fake_open = fake_filesystem.FakeFileOpen(self.fs)

        self._isStale = False

    def setUp(self, doctester=None):
        """Bind the file-related modules to the :py:mod:`pyfakefs` fake
        modules real ones.  Also bind the fake `file()` and `open()` functions.
        """
        temp_dir = tempfile.gettempdir()
        self._find_modules()
        self._refresh()

        if doctester is not None:
            doctester.globs = self.replace_globs(doctester.globs)

        self.start_patching()

        # the temp directory is assumed to exist at least in `tempfile1`,
        # so we create it here for convenience
        self.fs.create_dir(temp_dir)

    def start_patching(self):
        if not self._patching:
            self._patching = True

            if IS_PY2:
                self._stubs.smart_set(builtins, 'open', self.fake_open)
                self._stubs.smart_set(builtins, 'file', self.fake_open)

            for name, modules in self._modules.items():
                for module, attr in modules:
                    self._stubs.smart_set(
                        module, name, self.fake_modules[attr])
            for (name, ft_name, ft_mod), modules in self._fct_modules.items():
                method, mod_name = self._fake_module_functions[ft_name][ft_mod]
                fake_module = self.fake_modules[mod_name]
                attr = method.__get__(fake_module, fake_module.__class__)
                for module in modules:
                    self._stubs.smart_set(module, name, attr)
            if IS_PY2:
                for name, modules in self._open_functions.items():
                    for module in modules:
                        self._stubs.smart_set(module, name, self.fake_open)

            self._dyn_patcher = DynamicPatcher(self)
            sys.meta_path.insert(0, self._dyn_patcher)
            for module in self.modules_to_reload:
                if module.__name__ in sys.modules:
                    reload(module)
            if not self._use_dynamic_patch:
                self._dyn_patcher.cleanup()
                sys.meta_path.pop(0)

    def replace_globs(self, globs_):
        globs = globs_.copy()
        if self._isStale:
            self._refresh()
        for name in self._fake_module_classes:
            if name in globs:
                globs[name] = self._fake_module_classes[name](self.fs)
        return globs

    def tearDown(self, doctester=None):
        """Clear the fake filesystem bindings created by `setUp()`."""
        self.stop_patching()

    def stop_patching(self):
        if self._patching:
            self._isStale = True
            self._patching = False
            self._stubs.smart_unset_all()
            if self._use_dynamic_patch:
                self._dyn_patcher.cleanup()
                sys.meta_path.pop(0)

    def pause(self):
        """Pause the patching of the file system modules until `resume` is
        called. After that call, all file system calls are executed in the
        real file system.
        Calling pause() twice is silently ignored.

        """
        self.stop_patching()

    def resume(self):
        """Resume the patching of the file system modules if `pause` has
        been called before. After that call, all file system calls are
        executed in the fake file system.
        Does nothing if patching is not paused.
        """
        self.start_patching()


class Pause(object):
    """Simple context manager that allows to pause/resume patching the
    filesystem. Patching is paused in the context manager, and resumed after
    going out of it's scope.
    """
    def __init__(self, caller):
        """Initializes the context manager with the fake filesystem.

        Args:
            caller: either the FakeFilesystem instance, the Patcher instance
                or the pyfakefs test case.
        """
        if isinstance(caller, (Patcher, TestCaseMixin)):
            self._fs = caller.fs
        elif isinstance(caller, fake_filesystem.FakeFilesystem):
            self._fs = caller
        else:
            raise ValueError('Invalid argument - should be of type '
                             '"fake_filesystem_unittest.Patcher", '
                             '"fake_filesystem_unittest.TestCase" '
                             'or "fake_filesystem.FakeFilesystem"')

    def __enter__(self):
        self._fs.pause()
        return self._fs

    def __exit__(self, *args):
        return self._fs.resume()


class DynamicPatcher(object):
    """A file loader that replaces file system related modules by their
    fake implementation if they are loaded after calling `setupPyFakefs()`.
    Implements the protocol needed for import hooks.
    """

    def __init__(self, patcher):
        self._patcher = patcher
        self.sysmodules = {}
        self.modules = self._patcher.fake_modules

        # remove all modules that have to be patched from `sys.modules`,
        # otherwise the find_... methods will not be called
        for name in self.modules:
            if self.needs_patch(name) and name in sys.modules:
                self.sysmodules[name] = sys.modules[name]
                del sys.modules[name]

        for name, module in self.modules.items():
            sys.modules[name] = module

    def cleanup(self):
        for module in self.sysmodules:
            sys.modules[module] = self.sysmodules[module]
        for module in self._patcher.modules_to_reload:
            if module.__name__ in sys.modules:
                reload(module)

    def needs_patch(self, name):
        """Check if the module with the given name shall be replaced."""
        if name not in self.modules:
            return False
        if (name in sys.modules and
                type(sys.modules[name]) == self.modules[name]):
            return False
        return True

    def find_spec(self, fullname, path, target=None):
        """Module finder for Python 3."""
        if self.needs_patch(fullname):
            return ModuleSpec(fullname, self)

    def find_module(self, fullname, path=None):
        """Module finder for Python 2."""
        if self.needs_patch(fullname):
            return self

    def load_module(self, fullname):
        """Replaces the module by its fake implementation."""
        sys.modules[fullname] = self.modules[fullname]
        return self.modules[fullname]
