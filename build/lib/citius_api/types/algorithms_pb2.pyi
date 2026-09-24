import datetime

from google.protobuf import timestamp_pb2 as _timestamp_pb2
from citius_api.types import templates_pb2 as _templates_pb2
from citius_api.buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class StandardAlgorithmCatalog(_message.Message):
    __slots__ = ("version", "last_updated", "description", "templates", "families")
    class TemplatesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _templates_pb2.TemplateInfo
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_templates_pb2.TemplateInfo, _Mapping]] = ...) -> None: ...
    VERSION_FIELD_NUMBER: _ClassVar[int]
    LAST_UPDATED_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    TEMPLATES_FIELD_NUMBER: _ClassVar[int]
    FAMILIES_FIELD_NUMBER: _ClassVar[int]
    version: str
    last_updated: _timestamp_pb2.Timestamp
    description: str
    templates: _containers.MessageMap[str, _templates_pb2.TemplateInfo]
    families: _containers.RepeatedCompositeFieldContainer[AlgorithmFamilySpec]
    def __init__(self, version: _Optional[str] = ..., last_updated: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., description: _Optional[str] = ..., templates: _Optional[_Mapping[str, _templates_pb2.TemplateInfo]] = ..., families: _Optional[_Iterable[_Union[AlgorithmFamilySpec, _Mapping]]] = ...) -> None: ...

class AlgorithmFamilySpec(_message.Message):
    __slots__ = ("family", "display_name", "description", "primitive", "standards", "template_ids", "default_template_id", "has_pqc_variants", "min_security_level")
    FAMILY_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    PRIMITIVE_FIELD_NUMBER: _ClassVar[int]
    STANDARDS_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_IDS_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    HAS_PQC_VARIANTS_FIELD_NUMBER: _ClassVar[int]
    MIN_SECURITY_LEVEL_FIELD_NUMBER: _ClassVar[int]
    family: str
    display_name: str
    description: str
    primitive: str
    standards: _containers.RepeatedScalarFieldContainer[str]
    template_ids: _containers.RepeatedScalarFieldContainer[str]
    default_template_id: str
    has_pqc_variants: bool
    min_security_level: int
    def __init__(self, family: _Optional[str] = ..., display_name: _Optional[str] = ..., description: _Optional[str] = ..., primitive: _Optional[str] = ..., standards: _Optional[_Iterable[str]] = ..., template_ids: _Optional[_Iterable[str]] = ..., default_template_id: _Optional[str] = ..., has_pqc_variants: _Optional[bool] = ..., min_security_level: _Optional[int] = ...) -> None: ...
