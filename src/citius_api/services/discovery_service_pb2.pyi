from google.api import annotations_pb2 as _annotations_pb2
from citius_api.types import common_pb2 as _common_pb2
from citius_api.types import templates_pb2 as _templates_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ListTemplatesRequest(_message.Message):
    __slots__ = ("scope_spec", "allowed_statuses", "required_standards", "page_size", "page_token")
    SCOPE_SPEC_FIELD_NUMBER: _ClassVar[int]
    ALLOWED_STATUSES_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_STANDARDS_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    scope_spec: _common_pb2.ScopeSpecification
    allowed_statuses: _containers.RepeatedScalarFieldContainer[_templates_pb2.TemplateStatus]
    required_standards: _containers.RepeatedScalarFieldContainer[str]
    page_size: int
    page_token: str
    def __init__(self, scope_spec: _Optional[_Union[_common_pb2.ScopeSpecification, _Mapping]] = ..., allowed_statuses: _Optional[_Iterable[_Union[_templates_pb2.TemplateStatus, str]]] = ..., required_standards: _Optional[_Iterable[str]] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class ListTemplatesResponse(_message.Message):
    __slots__ = ("templates", "next_page_token")
    TEMPLATES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    templates: _containers.RepeatedCompositeFieldContainer[_templates_pb2.TemplateInfo]
    next_page_token: str
    def __init__(self, templates: _Optional[_Iterable[_Union[_templates_pb2.TemplateInfo, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class GetTemplateRequest(_message.Message):
    __slots__ = ("template_id",)
    TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    template_id: str
    def __init__(self, template_id: _Optional[str] = ...) -> None: ...

class GetTemplateResponse(_message.Message):
    __slots__ = ("template",)
    TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    template: _templates_pb2.TemplateInfo
    def __init__(self, template: _Optional[_Union[_templates_pb2.TemplateInfo, _Mapping]] = ...) -> None: ...

class ListScopesRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListScopesResponse(_message.Message):
    __slots__ = ("scopes",)
    SCOPES_FIELD_NUMBER: _ClassVar[int]
    scopes: _containers.RepeatedCompositeFieldContainer[_templates_pb2.ScopeInfo]
    def __init__(self, scopes: _Optional[_Iterable[_Union[_templates_pb2.ScopeInfo, _Mapping]]] = ...) -> None: ...
