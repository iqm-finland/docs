"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
Copyright 2019-2025 IQM

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import sys
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _NullValue:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _NullValueEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_NullValue.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    NULL_VALUE_UNSPECIFIED: _NullValue.ValueType  # 0
    """Null value."""

class NullValue(_NullValue, metaclass=_NullValueEnumTypeWrapper):
    """`NullValue` is a singleton enumeration to represent the null value for the
    `Value` type union.

    The JSON representation for `NullValue` is JSON `null`.
    """

NULL_VALUE_UNSPECIFIED: NullValue.ValueType  # 0
"""Null value."""
global___NullValue = NullValue

@typing.final
class Struct(google.protobuf.message.Message):
    """`Struct` represents a structured data value, consisting of fields
    which map to dynamically typed values. In some languages, `Struct`
    might be supported by a native representation. For example, in
    scripting languages like JS a struct is represented as an
    object. The details of that representation are described together
    with the proto support for the language.

    The JSON representation for `Struct` is JSON object.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing.final
    class FieldsEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.str
        @property
        def value(self) -> global___Value: ...
        def __init__(
            self,
            *,
            key: builtins.str = ...,
            value: global___Value | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing.Literal["value", b"value"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing.Literal["key", b"key", "value", b"value"]) -> None: ...

    FIELDS_FIELD_NUMBER: builtins.int
    @property
    def fields(self) -> google.protobuf.internal.containers.MessageMap[builtins.str, global___Value]:
        """Unordered map of dynamically typed values."""

    def __init__(
        self,
        *,
        fields: collections.abc.Mapping[builtins.str, global___Value] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["fields", b"fields"]) -> None: ...

global___Struct = Struct

@typing.final
class Value(google.protobuf.message.Message):
    """`Value` represents a dynamically typed value which can be either
    null, a double or an integer number, a string, a boolean, a recursive struct value, or a
    list of values. A producer of value is expected to set one of these
    variants. Absence of any variant indicates an error.

    The JSON representation for `Value` is JSON value.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NULL_VALUE_FIELD_NUMBER: builtins.int
    NUMBER_VALUE_FIELD_NUMBER: builtins.int
    STRING_VALUE_FIELD_NUMBER: builtins.int
    BOOL_VALUE_FIELD_NUMBER: builtins.int
    STRUCT_VALUE_FIELD_NUMBER: builtins.int
    LIST_VALUE_FIELD_NUMBER: builtins.int
    INTEGER_VALUE_FIELD_NUMBER: builtins.int
    null_value: global___NullValue.ValueType
    """Represents a null value."""
    number_value: builtins.float
    """Represents a double value."""
    string_value: builtins.str
    """Represents a string value."""
    bool_value: builtins.bool
    """Represents a boolean value."""
    integer_value: builtins.int
    """Represents an integer value."""
    @property
    def struct_value(self) -> global___Struct:
        """Represents a structured value."""

    @property
    def list_value(self) -> global___ListValue:
        """Represents a repeated `Value`."""

    def __init__(
        self,
        *,
        null_value: global___NullValue.ValueType = ...,
        number_value: builtins.float = ...,
        string_value: builtins.str = ...,
        bool_value: builtins.bool = ...,
        struct_value: global___Struct | None = ...,
        list_value: global___ListValue | None = ...,
        integer_value: builtins.int = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["bool_value", b"bool_value", "integer_value", b"integer_value", "kind", b"kind", "list_value", b"list_value", "null_value", b"null_value", "number_value", b"number_value", "string_value", b"string_value", "struct_value", b"struct_value"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["bool_value", b"bool_value", "integer_value", b"integer_value", "kind", b"kind", "list_value", b"list_value", "null_value", b"null_value", "number_value", b"number_value", "string_value", b"string_value", "struct_value", b"struct_value"]) -> None: ...
    def WhichOneof(self, oneof_group: typing.Literal["kind", b"kind"]) -> typing.Literal["null_value", "number_value", "string_value", "bool_value", "struct_value", "list_value", "integer_value"] | None: ...

global___Value = Value

@typing.final
class ListValue(google.protobuf.message.Message):
    """`ListValue` is a wrapper around a repeated field of values.

    The JSON representation for `ListValue` is JSON array.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    VALUES_FIELD_NUMBER: builtins.int
    @property
    def values(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Value]:
        """Repeated field of dynamically typed values."""

    def __init__(
        self,
        *,
        values: collections.abc.Iterable[global___Value] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["values", b"values"]) -> None: ...

global___ListValue = ListValue
