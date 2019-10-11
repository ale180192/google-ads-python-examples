# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v2/proto/resources/customer_extension_setting.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.google_ads.v2.proto.enums import extension_setting_device_pb2 as google_dot_ads_dot_googleads__v2_dot_proto_dot_enums_dot_extension__setting__device__pb2
from google.ads.google_ads.v2.proto.enums import extension_type_pb2 as google_dot_ads_dot_googleads__v2_dot_proto_dot_enums_dot_extension__type__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads_v2/proto/resources/customer_extension_setting.proto',
  package='google.ads.googleads.v2.resources',
  syntax='proto3',
  serialized_options=_b('\n%com.google.ads.googleads.v2.resourcesB\035CustomerExtensionSettingProtoP\001ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v2/resources;resources\242\002\003GAA\252\002!Google.Ads.GoogleAds.V2.Resources\312\002!Google\\Ads\\GoogleAds\\V2\\Resources\352\002%Google::Ads::GoogleAds::V2::Resources'),
  serialized_pb=_b('\nHgoogle/ads/googleads_v2/proto/resources/customer_extension_setting.proto\x12!google.ads.googleads.v2.resources\x1a\x42google/ads/googleads_v2/proto/enums/extension_setting_device.proto\x1a\x38google/ads/googleads_v2/proto/enums/extension_type.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x1cgoogle/api/annotations.proto\"\xa7\x02\n\x18\x43ustomerExtensionSetting\x12\x15\n\rresource_name\x18\x01 \x01(\t\x12V\n\x0e\x65xtension_type\x18\x02 \x01(\x0e\x32>.google.ads.googleads.v2.enums.ExtensionTypeEnum.ExtensionType\x12:\n\x14\x65xtension_feed_items\x18\x03 \x03(\x0b\x32\x1c.google.protobuf.StringValue\x12`\n\x06\x64\x65vice\x18\x04 \x01(\x0e\x32P.google.ads.googleads.v2.enums.ExtensionSettingDeviceEnum.ExtensionSettingDeviceB\x8a\x02\n%com.google.ads.googleads.v2.resourcesB\x1d\x43ustomerExtensionSettingProtoP\x01ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v2/resources;resources\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V2.Resources\xca\x02!Google\\Ads\\GoogleAds\\V2\\Resources\xea\x02%Google::Ads::GoogleAds::V2::Resourcesb\x06proto3')
  ,
  dependencies=[google_dot_ads_dot_googleads__v2_dot_proto_dot_enums_dot_extension__setting__device__pb2.DESCRIPTOR,google_dot_ads_dot_googleads__v2_dot_proto_dot_enums_dot_extension__type__pb2.DESCRIPTOR,google_dot_protobuf_dot_wrappers__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,])




_CUSTOMEREXTENSIONSETTING = _descriptor.Descriptor(
  name='CustomerExtensionSetting',
  full_name='google.ads.googleads.v2.resources.CustomerExtensionSetting',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v2.resources.CustomerExtensionSetting.resource_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='extension_type', full_name='google.ads.googleads.v2.resources.CustomerExtensionSetting.extension_type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='extension_feed_items', full_name='google.ads.googleads.v2.resources.CustomerExtensionSetting.extension_feed_items', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='device', full_name='google.ads.googleads.v2.resources.CustomerExtensionSetting.device', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=300,
  serialized_end=595,
)

_CUSTOMEREXTENSIONSETTING.fields_by_name['extension_type'].enum_type = google_dot_ads_dot_googleads__v2_dot_proto_dot_enums_dot_extension__type__pb2._EXTENSIONTYPEENUM_EXTENSIONTYPE
_CUSTOMEREXTENSIONSETTING.fields_by_name['extension_feed_items'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_CUSTOMEREXTENSIONSETTING.fields_by_name['device'].enum_type = google_dot_ads_dot_googleads__v2_dot_proto_dot_enums_dot_extension__setting__device__pb2._EXTENSIONSETTINGDEVICEENUM_EXTENSIONSETTINGDEVICE
DESCRIPTOR.message_types_by_name['CustomerExtensionSetting'] = _CUSTOMEREXTENSIONSETTING
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CustomerExtensionSetting = _reflection.GeneratedProtocolMessageType('CustomerExtensionSetting', (_message.Message,), dict(
  DESCRIPTOR = _CUSTOMEREXTENSIONSETTING,
  __module__ = 'google.ads.googleads_v2.proto.resources.customer_extension_setting_pb2'
  ,
  __doc__ = """A customer extension setting.
  
  
  Attributes:
      resource_name:
          The resource name of the customer extension setting.
          CustomerExtensionSetting resource names have the form:  ``cust
          omers/{customer_id}/customerExtensionSettings/{extension_type}
          ``
      extension_type:
          The extension type of the customer extension setting.
      extension_feed_items:
          The resource names of the extension feed items to serve under
          the customer. ExtensionFeedItem resource names have the form:
          ``customers/{customer_id}/extensionFeedItems/{feed_item_id}``
      device:
          The device for which the extensions will serve. Optional.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v2.resources.CustomerExtensionSetting)
  ))
_sym_db.RegisterMessage(CustomerExtensionSetting)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
