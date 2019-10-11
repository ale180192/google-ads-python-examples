# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v1/proto/enums/bidding_strategy_status.proto

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
  name='google/ads/googleads_v1/proto/enums/bidding_strategy_status.proto',
  package='google.ads.googleads.v1.enums',
  syntax='proto3',
  serialized_options=_b('\n!com.google.ads.googleads.v1.enumsB\032BiddingStrategyStatusProtoP\001ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v1/enums;enums\242\002\003GAA\252\002\035Google.Ads.GoogleAds.V1.Enums\312\002\035Google\\Ads\\GoogleAds\\V1\\Enums\352\002!Google::Ads::GoogleAds::V1::Enums'),
  serialized_pb=_b('\nAgoogle/ads/googleads_v1/proto/enums/bidding_strategy_status.proto\x12\x1dgoogle.ads.googleads.v1.enums\x1a\x1cgoogle/api/annotations.proto\"l\n\x19\x42iddingStrategyStatusEnum\"O\n\x15\x42iddingStrategyStatus\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12\x0b\n\x07\x45NABLED\x10\x02\x12\x0b\n\x07REMOVED\x10\x04\x42\xef\x01\n!com.google.ads.googleads.v1.enumsB\x1a\x42iddingStrategyStatusProtoP\x01ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v1/enums;enums\xa2\x02\x03GAA\xaa\x02\x1dGoogle.Ads.GoogleAds.V1.Enums\xca\x02\x1dGoogle\\Ads\\GoogleAds\\V1\\Enums\xea\x02!Google::Ads::GoogleAds::V1::Enumsb\x06proto3')
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])



_BIDDINGSTRATEGYSTATUSENUM_BIDDINGSTRATEGYSTATUS = _descriptor.EnumDescriptor(
  name='BiddingStrategyStatus',
  full_name='google.ads.googleads.v1.enums.BiddingStrategyStatusEnum.BiddingStrategyStatus',
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
      name='REMOVED', index=3, number=4,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=159,
  serialized_end=238,
)
_sym_db.RegisterEnumDescriptor(_BIDDINGSTRATEGYSTATUSENUM_BIDDINGSTRATEGYSTATUS)


_BIDDINGSTRATEGYSTATUSENUM = _descriptor.Descriptor(
  name='BiddingStrategyStatusEnum',
  full_name='google.ads.googleads.v1.enums.BiddingStrategyStatusEnum',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _BIDDINGSTRATEGYSTATUSENUM_BIDDINGSTRATEGYSTATUS,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=130,
  serialized_end=238,
)

_BIDDINGSTRATEGYSTATUSENUM_BIDDINGSTRATEGYSTATUS.containing_type = _BIDDINGSTRATEGYSTATUSENUM
DESCRIPTOR.message_types_by_name['BiddingStrategyStatusEnum'] = _BIDDINGSTRATEGYSTATUSENUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

BiddingStrategyStatusEnum = _reflection.GeneratedProtocolMessageType('BiddingStrategyStatusEnum', (_message.Message,), dict(
  DESCRIPTOR = _BIDDINGSTRATEGYSTATUSENUM,
  __module__ = 'google.ads.googleads_v1.proto.enums.bidding_strategy_status_pb2'
  ,
  __doc__ = """Message describing BiddingStrategy statuses.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v1.enums.BiddingStrategyStatusEnum)
  ))
_sym_db.RegisterMessage(BiddingStrategyStatusEnum)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
