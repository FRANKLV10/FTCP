# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: building.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='building.proto',
  package='proto',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0e\x62uilding.proto\x12\x05proto\"[\n\x12ReqUpgradeBuilding\x12\x10\n\x08playerId\x18\x01 \x01(\t\x12\x12\n\nbuildingId\x18\x02 \x01(\x03\x12\x1f\n\x06\x63ostBy\x18\x03 \x01(\x0e\x32\x0f.proto.CostType\"\x94\x01\n\x12RspUpgradeBuilding\x12\x12\n\nbuildingId\x18\x01 \x01(\x03\x12\x18\n\x10\x62uildingLevelNow\x18\x02 \x01(\x05\x12\x14\n\x0cplayerGemNow\x18\x03 \x01(\x03\x12\x15\n\rplayerGoldNow\x18\x04 \x01(\x03\x12\x11\n\tisSuccess\x18\x05 \x01(\x08\x12\x10\n\x08\x65rrorMsg\x18\x06 \x01(\t*\x1e\n\x08\x43ostType\x12\x08\n\x04Gems\x10\x00\x12\x08\n\x04Gold\x10\x01\x62\x06proto3'
)

_COSTTYPE = _descriptor.EnumDescriptor(
  name='CostType',
  full_name='proto.CostType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='Gems', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='Gold', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=269,
  serialized_end=299,
)
_sym_db.RegisterEnumDescriptor(_COSTTYPE)

CostType = enum_type_wrapper.EnumTypeWrapper(_COSTTYPE)
Gems = 0
Gold = 1



_REQUPGRADEBUILDING = _descriptor.Descriptor(
  name='ReqUpgradeBuilding',
  full_name='proto.ReqUpgradeBuilding',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='playerId', full_name='proto.ReqUpgradeBuilding.playerId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='buildingId', full_name='proto.ReqUpgradeBuilding.buildingId', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='costBy', full_name='proto.ReqUpgradeBuilding.costBy', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=25,
  serialized_end=116,
)


_RSPUPGRADEBUILDING = _descriptor.Descriptor(
  name='RspUpgradeBuilding',
  full_name='proto.RspUpgradeBuilding',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='buildingId', full_name='proto.RspUpgradeBuilding.buildingId', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='buildingLevelNow', full_name='proto.RspUpgradeBuilding.buildingLevelNow', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='playerGemNow', full_name='proto.RspUpgradeBuilding.playerGemNow', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='playerGoldNow', full_name='proto.RspUpgradeBuilding.playerGoldNow', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='isSuccess', full_name='proto.RspUpgradeBuilding.isSuccess', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='errorMsg', full_name='proto.RspUpgradeBuilding.errorMsg', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=119,
  serialized_end=267,
)

_REQUPGRADEBUILDING.fields_by_name['costBy'].enum_type = _COSTTYPE
DESCRIPTOR.message_types_by_name['ReqUpgradeBuilding'] = _REQUPGRADEBUILDING
DESCRIPTOR.message_types_by_name['RspUpgradeBuilding'] = _RSPUPGRADEBUILDING
DESCRIPTOR.enum_types_by_name['CostType'] = _COSTTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ReqUpgradeBuilding = _reflection.GeneratedProtocolMessageType('ReqUpgradeBuilding', (_message.Message,), {
  'DESCRIPTOR' : _REQUPGRADEBUILDING,
  '__module__' : 'building_pb2'
  # @@protoc_insertion_point(class_scope:proto.ReqUpgradeBuilding)
  })
_sym_db.RegisterMessage(ReqUpgradeBuilding)

RspUpgradeBuilding = _reflection.GeneratedProtocolMessageType('RspUpgradeBuilding', (_message.Message,), {
  'DESCRIPTOR' : _RSPUPGRADEBUILDING,
  '__module__' : 'building_pb2'
  # @@protoc_insertion_point(class_scope:proto.RspUpgradeBuilding)
  })
_sym_db.RegisterMessage(RspUpgradeBuilding)


# @@protoc_insertion_point(module_scope)