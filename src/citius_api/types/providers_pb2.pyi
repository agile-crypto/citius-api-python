from citius_api.types import implementation_pb2 as _implementation_pb2
from citius_api.buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ProviderType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PROVIDER_TYPE_UNSPECIFIED: _ClassVar[ProviderType]
    PROVIDER_TYPE_SOFTWARE: _ClassVar[ProviderType]
    PROVIDER_TYPE_HSM: _ClassVar[ProviderType]
    PROVIDER_TYPE_CLOUD_KMS: _ClassVar[ProviderType]
    PROVIDER_TYPE_REMOTE: _ClassVar[ProviderType]
PROVIDER_TYPE_UNSPECIFIED: ProviderType
PROVIDER_TYPE_SOFTWARE: ProviderType
PROVIDER_TYPE_HSM: ProviderType
PROVIDER_TYPE_CLOUD_KMS: ProviderType
PROVIDER_TYPE_REMOTE: ProviderType

class ProviderInfo(_message.Message):
    __slots__ = ("provider_id", "display_name", "description", "capabilities", "configuration_schema", "default_implementation", "template_support", "provider_type")
    class CapabilitiesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class ConfigurationSchemaEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: ConfigurationParameter
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[ConfigurationParameter, _Mapping]] = ...) -> None: ...
    PROVIDER_ID_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    CONFIGURATION_SCHEMA_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_IMPLEMENTATION_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_SUPPORT_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_TYPE_FIELD_NUMBER: _ClassVar[int]
    provider_id: str
    display_name: str
    description: str
    capabilities: _containers.ScalarMap[str, str]
    configuration_schema: _containers.MessageMap[str, ConfigurationParameter]
    default_implementation: _implementation_pb2.ImplementationProperties
    template_support: _containers.RepeatedCompositeFieldContainer[_implementation_pb2.ProviderTemplateSupport]
    provider_type: ProviderType
    def __init__(self, provider_id: _Optional[str] = ..., display_name: _Optional[str] = ..., description: _Optional[str] = ..., capabilities: _Optional[_Mapping[str, str]] = ..., configuration_schema: _Optional[_Mapping[str, ConfigurationParameter]] = ..., default_implementation: _Optional[_Union[_implementation_pb2.ImplementationProperties, _Mapping]] = ..., template_support: _Optional[_Iterable[_Union[_implementation_pb2.ProviderTemplateSupport, _Mapping]]] = ..., provider_type: _Optional[_Union[ProviderType, str]] = ...) -> None: ...

class ConfigurationParameter(_message.Message):
    __slots__ = ("name", "type", "description", "required", "default_value")
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_VALUE_FIELD_NUMBER: _ClassVar[int]
    name: str
    type: str
    description: str
    required: bool
    default_value: str
    def __init__(self, name: _Optional[str] = ..., type: _Optional[str] = ..., description: _Optional[str] = ..., required: _Optional[bool] = ..., default_value: _Optional[str] = ...) -> None: ...
