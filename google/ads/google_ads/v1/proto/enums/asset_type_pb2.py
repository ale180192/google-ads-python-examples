# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v1/proto/enums/asset_type.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads_v1/proto/enums/asset_type.proto',
  package='google.ads.googleads.v1.enums',
  syntax='proto3',
  serialized_options=_b('\n!com.google.ads.googleads.v1.enumsB\016AssetTypeProtoP\001ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v1/enums;enums\242\002\003GAA\252\002\035Google.Ads.GoogleAds.V1.Enums\312\002\035Google\\Ads\\GoogleAds\\V1\\Enums\352\002!Google::Ads::GoogleAds::V1::Enums'),
  serialized_pb=_b('\n4google/ads/googleads_v1/proto/enums/asset_type.proto\x12\x1dgoogle.ads.googleads.v1.enums\x1a\x1cgoogle/api/annotations.proto\"t\n\rAssetTypeEnum\"c\n\tAssetType\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12\x11\n\rYOUTUBE_VIDEO\x10\x02\x12\x10\n\x0cMEDIA_BUNDLE\x10\x03\x12\t\n\x05IMAGE\x10\x04\x12\x08\n\x04TEXT\x10\x05\x42\xe3\x01\n!com.google.ads.googleads.v1.enumsB\x0e\x41ssetTypeProtoP\x01ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v1/enums;enums\xa2\x02\x03GAA\xaa\x02\x1dGoogle.Ads.GoogleAds.V1.Enums\xca\x02\x1dGoogle\\Ads\\GoogleAds\\V1\\Enums\xea\x02!Google::Ads::GoogleAds::V1::Enumsb\x06proto3')
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])



_ASSETTYPEENUM_ASSETTYPE = _descriptor.EnumDescriptor(
  name='AssetType',
  full_name='google.ads.googleads.v1.enums.AssetTypeEnum.AssetType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='YOUTUBE_VIDEO', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MEDIA_BUNDLE', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='IMAGE', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TEXT', index=5, number=5,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=134,
  serialized_end=233,
)
_sym_db.RegisterEnumDescriptor(_ASSETTYPEENUM_ASSETTYPE)


_ASSETTYPEENUM = _descriptor.Descriptor(
  name='AssetTypeEnum',
  full_name='google.ads.googleads.v1.enums.AssetTypeEnum',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _ASSETTYPEENUM_ASSETTYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=117,
  serialized_end=233,
)

_ASSETTYPEENUM_ASSETTYPE.containing_type = _ASSETTYPEENUM
DESCRIPTOR.message_types_by_name['AssetTypeEnum'] = _ASSETTYPEENUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AssetTypeEnum = _reflection.GeneratedProtocolMessageType('AssetTypeEnum', (_message.Message,), dict(
  DESCRIPTOR = _ASSETTYPEENUM,
  __module__ = 'google.ads.googleads_v1.proto.enums.asset_type_pb2'
  ,
  __doc__ = """Container for enum describing the types of asset.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v1.enums.AssetTypeEnum)
  ))
_sym_db.RegisterMessage(AssetTypeEnum)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
