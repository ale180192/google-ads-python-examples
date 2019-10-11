# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v1/proto/enums/feed_mapping_status.proto

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
  name='google/ads/googleads_v1/proto/enums/feed_mapping_status.proto',
  package='google.ads.googleads.v1.enums',
  syntax='proto3',
  serialized_options=_b('\n!com.google.ads.googleads.v1.enumsB\026FeedMappingStatusProtoP\001ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v1/enums;enums\242\002\003GAA\252\002\035Google.Ads.GoogleAds.V1.Enums\312\002\035Google\\Ads\\GoogleAds\\V1\\Enums\352\002!Google::Ads::GoogleAds::V1::Enums'),
  serialized_pb=_b('\n=google/ads/googleads_v1/proto/enums/feed_mapping_status.proto\x12\x1dgoogle.ads.googleads.v1.enums\x1a\x1cgoogle/api/annotations.proto\"d\n\x15\x46\x65\x65\x64MappingStatusEnum\"K\n\x11\x46\x65\x65\x64MappingStatus\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12\x0b\n\x07\x45NABLED\x10\x02\x12\x0b\n\x07REMOVED\x10\x03\x42\xeb\x01\n!com.google.ads.googleads.v1.enumsB\x16\x46\x65\x65\x64MappingStatusProtoP\x01ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v1/enums;enums\xa2\x02\x03GAA\xaa\x02\x1dGoogle.Ads.GoogleAds.V1.Enums\xca\x02\x1dGoogle\\Ads\\GoogleAds\\V1\\Enums\xea\x02!Google::Ads::GoogleAds::V1::Enumsb\x06proto3')
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])



_FEEDMAPPINGSTATUSENUM_FEEDMAPPINGSTATUS = _descriptor.EnumDescriptor(
  name='FeedMappingStatus',
  full_name='google.ads.googleads.v1.enums.FeedMappingStatusEnum.FeedMappingStatus',
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
      name='ENABLED', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REMOVED', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=151,
  serialized_end=226,
)
_sym_db.RegisterEnumDescriptor(_FEEDMAPPINGSTATUSENUM_FEEDMAPPINGSTATUS)


_FEEDMAPPINGSTATUSENUM = _descriptor.Descriptor(
  name='FeedMappingStatusEnum',
  full_name='google.ads.googleads.v1.enums.FeedMappingStatusEnum',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _FEEDMAPPINGSTATUSENUM_FEEDMAPPINGSTATUS,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=126,
  serialized_end=226,
)

_FEEDMAPPINGSTATUSENUM_FEEDMAPPINGSTATUS.containing_type = _FEEDMAPPINGSTATUSENUM
DESCRIPTOR.message_types_by_name['FeedMappingStatusEnum'] = _FEEDMAPPINGSTATUSENUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

FeedMappingStatusEnum = _reflection.GeneratedProtocolMessageType('FeedMappingStatusEnum', (_message.Message,), dict(
  DESCRIPTOR = _FEEDMAPPINGSTATUSENUM,
  __module__ = 'google.ads.googleads_v1.proto.enums.feed_mapping_status_pb2'
  ,
  __doc__ = """Container for enum describing possible statuses of a feed mapping.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v1.enums.FeedMappingStatusEnum)
  ))
_sym_db.RegisterMessage(FeedMappingStatusEnum)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
