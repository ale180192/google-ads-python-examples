# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v2/proto/resources/expanded_landing_page_view.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads_v2/proto/resources/expanded_landing_page_view.proto',
  package='google.ads.googleads.v2.resources',
  syntax='proto3',
  serialized_options=_b('\n%com.google.ads.googleads.v2.resourcesB\034ExpandedLandingPageViewProtoP\001ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v2/resources;resources\242\002\003GAA\252\002!Google.Ads.GoogleAds.V2.Resources\312\002!Google\\Ads\\GoogleAds\\V2\\Resources\352\002%Google::Ads::GoogleAds::V2::Resources'),
  serialized_pb=_b('\nHgoogle/ads/googleads_v2/proto/resources/expanded_landing_page_view.proto\x12!google.ads.googleads.v2.resources\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x1cgoogle/api/annotations.proto\"j\n\x17\x45xpandedLandingPageView\x12\x15\n\rresource_name\x18\x01 \x01(\t\x12\x38\n\x12\x65xpanded_final_url\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValueB\x89\x02\n%com.google.ads.googleads.v2.resourcesB\x1c\x45xpandedLandingPageViewProtoP\x01ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v2/resources;resources\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V2.Resources\xca\x02!Google\\Ads\\GoogleAds\\V2\\Resources\xea\x02%Google::Ads::GoogleAds::V2::Resourcesb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_wrappers__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,])




_EXPANDEDLANDINGPAGEVIEW = _descriptor.Descriptor(
  name='ExpandedLandingPageView',
  full_name='google.ads.googleads.v2.resources.ExpandedLandingPageView',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v2.resources.ExpandedLandingPageView.resource_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='expanded_final_url', full_name='google.ads.googleads.v2.resources.ExpandedLandingPageView.expanded_final_url', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=173,
  serialized_end=279,
)

_EXPANDEDLANDINGPAGEVIEW.fields_by_name['expanded_final_url'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
DESCRIPTOR.message_types_by_name['ExpandedLandingPageView'] = _EXPANDEDLANDINGPAGEVIEW
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ExpandedLandingPageView = _reflection.GeneratedProtocolMessageType('ExpandedLandingPageView', (_message.Message,), dict(
  DESCRIPTOR = _EXPANDEDLANDINGPAGEVIEW,
  __module__ = 'google.ads.googleads_v2.proto.resources.expanded_landing_page_view_pb2'
  ,
  __doc__ = """A landing page view with metrics aggregated at the expanded final URL
  level.
  
  
  Attributes:
      resource_name:
          The resource name of the expanded landing page view. Expanded
          landing page view resource names have the form:  ``customers/{
          customer_id}/expandedLandingPageViews/{expanded_final_url_fing
          erprint}``
      expanded_final_url:
          The final URL that clicks are directed to.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v2.resources.ExpandedLandingPageView)
  ))
_sym_db.RegisterMessage(ExpandedLandingPageView)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
