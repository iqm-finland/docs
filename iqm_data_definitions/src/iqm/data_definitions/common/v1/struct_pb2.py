# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: iqm/data_definitions/common/v1/struct.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+iqm/data_definitions/common/v1/struct.proto\x12\x1eiqm.data_definitions.common.v1\"\xa2\x01\n\x06Struct\x12\x42\n\x06\x66ields\x18\x01 \x03(\x0b\x32\x32.iqm.data_definitions.common.v1.Struct.FieldsEntry\x1aT\n\x0b\x46ieldsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x34\n\x05value\x18\x02 \x01(\x0b\x32%.iqm.data_definitions.common.v1.Value:\x02\x38\x01\"\xb0\x02\n\x05Value\x12?\n\nnull_value\x18\x01 \x01(\x0e\x32).iqm.data_definitions.common.v1.NullValueH\x00\x12\x16\n\x0cnumber_value\x18\x02 \x01(\x01H\x00\x12\x16\n\x0cstring_value\x18\x03 \x01(\tH\x00\x12\x14\n\nbool_value\x18\x04 \x01(\x08H\x00\x12>\n\x0cstruct_value\x18\x05 \x01(\x0b\x32&.iqm.data_definitions.common.v1.StructH\x00\x12?\n\nlist_value\x18\x06 \x01(\x0b\x32).iqm.data_definitions.common.v1.ListValueH\x00\x12\x17\n\rinteger_value\x18\x07 \x01(\x12H\x00\x42\x06\n\x04kind\"B\n\tListValue\x12\x35\n\x06values\x18\x01 \x03(\x0b\x32%.iqm.data_definitions.common.v1.Value*\'\n\tNullValue\x12\x1a\n\x16NULL_VALUE_UNSPECIFIED\x10\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'iqm.data_definitions.common.v1.struct_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _STRUCT_FIELDSENTRY._options = None
  _STRUCT_FIELDSENTRY._serialized_options = b'8\001'
  _NULLVALUE._serialized_start=619
  _NULLVALUE._serialized_end=658
  _STRUCT._serialized_start=80
  _STRUCT._serialized_end=242
  _STRUCT_FIELDSENTRY._serialized_start=158
  _STRUCT_FIELDSENTRY._serialized_end=242
  _VALUE._serialized_start=245
  _VALUE._serialized_end=549
  _LISTVALUE._serialized_start=551
  _LISTVALUE._serialized_end=617
# @@protoc_insertion_point(module_scope)
