# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v2/proto/resources/hotel_performance_view.proto

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
  name='google/ads/googleads_v2/proto/resources/hotel_performance_view.proto',
  package='google.ads.googleads.v2.resources',
  syntax='proto3',
  serialized_options=_b('\n%com.google.ads.googleads.v2.resourcesB\031HotelPerformanceViewProtoP\001ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v2/resources;resources\242\002\003GAA\252\002!Google.Ads.GoogleAds.V2.Resources\312\002!Google\\Ads\\GoogleAds\\V2\\Resources\352\002%Google::Ads::GoogleAds::V2::Resources'),
  serialized_pb=_b('\nDgoogle/ads/googleads_v2/proto/resources/hotel_performance_view.proto\x12!google.ads.googleads.v2.resources\x1a\x1cgoogle/api/annotations.proto\"-\n\x14HotelPerformanceView\x12\x15\n\rresource_name\x18\x01 \x01(\tB\x86\x02\n%com.google.ads.googleads.v2.resourcesB\x19HotelPerformanceViewProtoP\x01ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v2/resources;resources\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V2.Resources\xca\x02!Google\\Ads\\GoogleAds\\V2\\Resources\xea\x02%Google::Ads::GoogleAds::V2::Resourcesb\x06proto3')
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])




_HOTELPERFORMANCEVIEW = _descriptor.Descriptor(
  name='HotelPerformanceView',
  full_name='google.ads.googleads.v2.resources.HotelPerformanceView',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v2.resources.HotelPerformanceView.resource_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=137,
  serialized_end=182,
)

DESCRIPTOR.message_types_by_name['HotelPerformanceView'] = _HOTELPERFORMANCEVIEW
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

HotelPerformanceView = _reflection.GeneratedProtocolMessageType('HotelPerformanceView', (_message.Message,), dict(
  DESCRIPTOR = _HOTELPERFORMANCEVIEW,
  __module__ = 'google.ads.googleads_v2.proto.resources.hotel_performance_view_pb2'
  ,
  __doc__ = """A hotel performance view.
  
  
  Attributes:
      resource_name:
          The resource name of the hotel performance view. Hotel
          performance view resource names have the form:
          ``customers/{customer_id}/hotelPerformanceView``
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v2.resources.HotelPerformanceView)
  ))
_sym_db.RegisterMessage(HotelPerformanceView)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
