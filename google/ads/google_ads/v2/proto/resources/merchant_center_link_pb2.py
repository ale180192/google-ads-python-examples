# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v2/proto/resources/merchant_center_link.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.google_ads.v2.proto.enums import merchant_center_link_status_pb2 as google_dot_ads_dot_googleads__v2_dot_proto_dot_enums_dot_merchant__center__link__status__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads_v2/proto/resources/merchant_center_link.proto',
  package='google.ads.googleads.v2.resources',
  syntax='proto3',
  serialized_options=_b('\n%com.google.ads.googleads.v2.resourcesB\027MerchantCenterLinkProtoP\001ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v2/resources;resources\242\002\003GAA\252\002!Google.Ads.GoogleAds.V2.Resources\312\002!Google\\Ads\\GoogleAds\\V2\\Resources\352\002%Google::Ads::GoogleAds::V2::Resources'),
  serialized_pb=_b('\nBgoogle/ads/googleads_v2/proto/resources/merchant_center_link.proto\x12!google.ads.googleads.v2.resources\x1a\x45google/ads/googleads_v2/proto/enums/merchant_center_link_status.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x1cgoogle/api/annotations.proto\"\xfe\x01\n\x12MerchantCenterLink\x12\x15\n\rresource_name\x18\x01 \x01(\t\x12\'\n\x02id\x18\x03 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12\x42\n\x1cmerchant_center_account_name\x18\x04 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x64\n\x06status\x18\x05 \x01(\x0e\x32T.google.ads.googleads.v2.enums.MerchantCenterLinkStatusEnum.MerchantCenterLinkStatusB\x84\x02\n%com.google.ads.googleads.v2.resourcesB\x17MerchantCenterLinkProtoP\x01ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v2/resources;resources\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V2.Resources\xca\x02!Google\\Ads\\GoogleAds\\V2\\Resources\xea\x02%Google::Ads::GoogleAds::V2::Resourcesb\x06proto3')
  ,
  dependencies=[google_dot_ads_dot_googleads__v2_dot_proto_dot_enums_dot_merchant__center__link__status__pb2.DESCRIPTOR,google_dot_protobuf_dot_wrappers__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,])




_MERCHANTCENTERLINK = _descriptor.Descriptor(
  name='MerchantCenterLink',
  full_name='google.ads.googleads.v2.resources.MerchantCenterLink',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v2.resources.MerchantCenterLink.resource_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id', full_name='google.ads.googleads.v2.resources.MerchantCenterLink.id', index=1,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='merchant_center_account_name', full_name='google.ads.googleads.v2.resources.MerchantCenterLink.merchant_center_account_name', index=2,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='google.ads.googleads.v2.resources.MerchantCenterLink.status', index=3,
      number=5, type=14, cpp_type=8, label=1,
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
  serialized_start=239,
  serialized_end=493,
)

_MERCHANTCENTERLINK.fields_by_name['id'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT64VALUE
_MERCHANTCENTERLINK.fields_by_name['merchant_center_account_name'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_MERCHANTCENTERLINK.fields_by_name['status'].enum_type = google_dot_ads_dot_googleads__v2_dot_proto_dot_enums_dot_merchant__center__link__status__pb2._MERCHANTCENTERLINKSTATUSENUM_MERCHANTCENTERLINKSTATUS
DESCRIPTOR.message_types_by_name['MerchantCenterLink'] = _MERCHANTCENTERLINK
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MerchantCenterLink = _reflection.GeneratedProtocolMessageType('MerchantCenterLink', (_message.Message,), dict(
  DESCRIPTOR = _MERCHANTCENTERLINK,
  __module__ = 'google.ads.googleads_v2.proto.resources.merchant_center_link_pb2'
  ,
  __doc__ = """A data sharing connection, proposed or in use, between a Google Ads
  Customer and a Merchant Center account.
  
  
  Attributes:
      resource_name:
          The resource name of the merchant center link. Merchant center
          link resource names have the form:  ``customers/{customer_id}/
          merchantCenterLinks/{merchant_center_id}``
      id:
          The ID of the Merchant Center account. This field is readonly.
      merchant_center_account_name:
          The name of the Merchant Center account. This field is
          readonly.
      status:
          The status of the link.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v2.resources.MerchantCenterLink)
  ))
_sym_db.RegisterMessage(MerchantCenterLink)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
