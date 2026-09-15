from google.api import annotations_pb2 as _annotations_pb2
from citius_api.types import providers_pb2 as _providers_pb2
from citius_api.types import implementation_pb2 as _implementation_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ListProvidersRequest(_message.Message):
    __slots__ = ("template_id", "requirements", "page_size", "page_token")
    TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    REQUIREMENTS_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    template_id: str
    requirements: _implementation_pb2.ProviderRequirements
    page_size: int
    page_token: str
    def __init__(self, template_id: _Optional[str] = ..., requirements: _Optional[_Union[_implementation_pb2.ProviderRequirements, _Mapping]] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class ListProvidersResponse(_message.Message):
    __slots__ = ("providers", "next_page_token")
    PROVIDERS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    providers: _containers.RepeatedCompositeFieldContainer[_providers_pb2.ProviderInfo]
    next_page_token: str
    def __init__(self, providers: _Optional[_Iterable[_Union[_providers_pb2.ProviderInfo, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class GetProviderRequest(_message.Message):
    __slots__ = ("provider_id",)
    PROVIDER_ID_FIELD_NUMBER: _ClassVar[int]
    provider_id: str
    def __init__(self, provider_id: _Optional[str] = ...) -> None: ...

class GetProviderResponse(_message.Message):
    __slots__ = ("provider",)
    PROVIDER_FIELD_NUMBER: _ClassVar[int]
    provider: _providers_pb2.ProviderInfo
    def __init__(self, provider: _Optional[_Union[_providers_pb2.ProviderInfo, _Mapping]] = ...) -> None: ...

class RegisterProviderInstanceRequest(_message.Message):
    __slots__ = ("instance",)
    INSTANCE_FIELD_NUMBER: _ClassVar[int]
    instance: _implementation_pb2.ProviderInstance
    def __init__(self, instance: _Optional[_Union[_implementation_pb2.ProviderInstance, _Mapping]] = ...) -> None: ...

class RegisterProviderInstanceResponse(_message.Message):
    __slots__ = ("success", "message", "instance")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_FIELD_NUMBER: _ClassVar[int]
    success: bool
    message: str
    instance: _implementation_pb2.ProviderInstance
    def __init__(self, success: _Optional[bool] = ..., message: _Optional[str] = ..., instance: _Optional[_Union[_implementation_pb2.ProviderInstance, _Mapping]] = ...) -> None: ...

class ListProviderInstancesRequest(_message.Message):
    __slots__ = ("provider_id", "requirements", "enabled_only", "page_size", "page_token")
    PROVIDER_ID_FIELD_NUMBER: _ClassVar[int]
    REQUIREMENTS_FIELD_NUMBER: _ClassVar[int]
    ENABLED_ONLY_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    provider_id: str
    requirements: _implementation_pb2.ProviderRequirements
    enabled_only: bool
    page_size: int
    page_token: str
    def __init__(self, provider_id: _Optional[str] = ..., requirements: _Optional[_Union[_implementation_pb2.ProviderRequirements, _Mapping]] = ..., enabled_only: _Optional[bool] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class ListProviderInstancesResponse(_message.Message):
    __slots__ = ("instances", "next_page_token")
    INSTANCES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    instances: _containers.RepeatedCompositeFieldContainer[_implementation_pb2.ProviderInstance]
    next_page_token: str
    def __init__(self, instances: _Optional[_Iterable[_Union[_implementation_pb2.ProviderInstance, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class GetProviderInstanceRequest(_message.Message):
    __slots__ = ("instance_id",)
    INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    instance_id: str
    def __init__(self, instance_id: _Optional[str] = ...) -> None: ...

class GetProviderInstanceResponse(_message.Message):
    __slots__ = ("instance",)
    INSTANCE_FIELD_NUMBER: _ClassVar[int]
    instance: _implementation_pb2.ProviderInstance
    def __init__(self, instance: _Optional[_Union[_implementation_pb2.ProviderInstance, _Mapping]] = ...) -> None: ...

class UpdateProviderInstanceRequest(_message.Message):
    __slots__ = ("instance",)
    INSTANCE_FIELD_NUMBER: _ClassVar[int]
    instance: _implementation_pb2.ProviderInstance
    def __init__(self, instance: _Optional[_Union[_implementation_pb2.ProviderInstance, _Mapping]] = ...) -> None: ...

class UpdateProviderInstanceResponse(_message.Message):
    __slots__ = ("success", "message", "instance")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_FIELD_NUMBER: _ClassVar[int]
    success: bool
    message: str
    instance: _implementation_pb2.ProviderInstance
    def __init__(self, success: _Optional[bool] = ..., message: _Optional[str] = ..., instance: _Optional[_Union[_implementation_pb2.ProviderInstance, _Mapping]] = ...) -> None: ...

class DeleteProviderInstanceRequest(_message.Message):
    __slots__ = ("instance_id",)
    INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    instance_id: str
    def __init__(self, instance_id: _Optional[str] = ...) -> None: ...

class DeleteProviderInstanceResponse(_message.Message):
    __slots__ = ("success", "message")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    success: bool
    message: str
    def __init__(self, success: _Optional[bool] = ..., message: _Optional[str] = ...) -> None: ...

class MatchProvidersRequest(_message.Message):
    __slots__ = ("template_id", "requirements", "include_disabled")
    TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    REQUIREMENTS_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_DISABLED_FIELD_NUMBER: _ClassVar[int]
    template_id: str
    requirements: _implementation_pb2.ProviderRequirements
    include_disabled: bool
    def __init__(self, template_id: _Optional[str] = ..., requirements: _Optional[_Union[_implementation_pb2.ProviderRequirements, _Mapping]] = ..., include_disabled: _Optional[bool] = ...) -> None: ...

class MatchProvidersResponse(_message.Message):
    __slots__ = ("matches",)
    MATCHES_FIELD_NUMBER: _ClassVar[int]
    matches: _containers.RepeatedCompositeFieldContainer[MatchedProvider]
    def __init__(self, matches: _Optional[_Iterable[_Union[MatchedProvider, _Mapping]]] = ...) -> None: ...

class MatchedProvider(_message.Message):
    __slots__ = ("instance", "resolved_implementation", "match_score")
    INSTANCE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_IMPLEMENTATION_FIELD_NUMBER: _ClassVar[int]
    MATCH_SCORE_FIELD_NUMBER: _ClassVar[int]
    instance: _implementation_pb2.ProviderInstance
    resolved_implementation: _implementation_pb2.ImplementationProperties
    match_score: int
    def __init__(self, instance: _Optional[_Union[_implementation_pb2.ProviderInstance, _Mapping]] = ..., resolved_implementation: _Optional[_Union[_implementation_pb2.ImplementationProperties, _Mapping]] = ..., match_score: _Optional[int] = ...) -> None: ...
