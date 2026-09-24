import datetime

from citius_api.types import common_pb2 as _common_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from citius_api.buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PolicyDenialReason(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    POLICY_DENIAL_REASON_UNSPECIFIED: _ClassVar[PolicyDenialReason]
    POLICY_DENIAL_REASON_POLICY_NOT_FOUND: _ClassVar[PolicyDenialReason]
    POLICY_DENIAL_REASON_OPERATION_NOT_ALLOWED: _ClassVar[PolicyDenialReason]
    POLICY_DENIAL_REASON_TEMPLATE_NOT_ALLOWED: _ClassVar[PolicyDenialReason]
    POLICY_DENIAL_REASON_SCOPE_NOT_ALLOWED: _ClassVar[PolicyDenialReason]
    POLICY_DENIAL_REASON_PROVIDER_NOT_ALLOWED: _ClassVar[PolicyDenialReason]
    POLICY_DENIAL_REASON_KEY_NOT_FOUND: _ClassVar[PolicyDenialReason]
    POLICY_DENIAL_REASON_PROPERTY_MISMATCH: _ClassVar[PolicyDenialReason]
    POLICY_DENIAL_REASON_SECURITY_LEVEL_INSUFFICIENT: _ClassVar[PolicyDenialReason]
    POLICY_DENIAL_REASON_ALGORITHM_DEPRECATED: _ClassVar[PolicyDenialReason]
    POLICY_DENIAL_REASON_PQC_REQUIRED: _ClassVar[PolicyDenialReason]
POLICY_DENIAL_REASON_UNSPECIFIED: PolicyDenialReason
POLICY_DENIAL_REASON_POLICY_NOT_FOUND: PolicyDenialReason
POLICY_DENIAL_REASON_OPERATION_NOT_ALLOWED: PolicyDenialReason
POLICY_DENIAL_REASON_TEMPLATE_NOT_ALLOWED: PolicyDenialReason
POLICY_DENIAL_REASON_SCOPE_NOT_ALLOWED: PolicyDenialReason
POLICY_DENIAL_REASON_PROVIDER_NOT_ALLOWED: PolicyDenialReason
POLICY_DENIAL_REASON_KEY_NOT_FOUND: PolicyDenialReason
POLICY_DENIAL_REASON_PROPERTY_MISMATCH: PolicyDenialReason
POLICY_DENIAL_REASON_SECURITY_LEVEL_INSUFFICIENT: PolicyDenialReason
POLICY_DENIAL_REASON_ALGORITHM_DEPRECATED: PolicyDenialReason
POLICY_DENIAL_REASON_PQC_REQUIRED: PolicyDenialReason

class CreateCryptoPolicyRequest(_message.Message):
    __slots__ = ("name", "policy_document", "format")
    NAME_FIELD_NUMBER: _ClassVar[int]
    POLICY_DOCUMENT_FIELD_NUMBER: _ClassVar[int]
    FORMAT_FIELD_NUMBER: _ClassVar[int]
    name: str
    policy_document: str
    format: str
    def __init__(self, name: _Optional[str] = ..., policy_document: _Optional[str] = ..., format: _Optional[str] = ...) -> None: ...

class CreateCryptoPolicyResponse(_message.Message):
    __slots__ = ("success", "message", "version")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    success: bool
    message: str
    version: int
    def __init__(self, success: _Optional[bool] = ..., message: _Optional[str] = ..., version: _Optional[int] = ...) -> None: ...

class ReadCryptoPolicyRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ReadCryptoPolicyResponse(_message.Message):
    __slots__ = ("name", "policy_document", "format", "version", "created_at", "updated_at")
    NAME_FIELD_NUMBER: _ClassVar[int]
    POLICY_DOCUMENT_FIELD_NUMBER: _ClassVar[int]
    FORMAT_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    name: str
    policy_document: str
    format: str
    version: int
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    def __init__(self, name: _Optional[str] = ..., policy_document: _Optional[str] = ..., format: _Optional[str] = ..., version: _Optional[int] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class DeleteCryptoPolicyRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class DeleteCryptoPolicyResponse(_message.Message):
    __slots__ = ("success", "message")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    success: bool
    message: str
    def __init__(self, success: _Optional[bool] = ..., message: _Optional[str] = ...) -> None: ...

class UpdateCryptoPolicyRequest(_message.Message):
    __slots__ = ("name", "policy_document", "format", "expected_version")
    NAME_FIELD_NUMBER: _ClassVar[int]
    POLICY_DOCUMENT_FIELD_NUMBER: _ClassVar[int]
    FORMAT_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_VERSION_FIELD_NUMBER: _ClassVar[int]
    name: str
    policy_document: str
    format: str
    expected_version: int
    def __init__(self, name: _Optional[str] = ..., policy_document: _Optional[str] = ..., format: _Optional[str] = ..., expected_version: _Optional[int] = ...) -> None: ...

class UpdateCryptoPolicyResponse(_message.Message):
    __slots__ = ("success", "message", "version")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    success: bool
    message: str
    version: int
    def __init__(self, success: _Optional[bool] = ..., message: _Optional[str] = ..., version: _Optional[int] = ...) -> None: ...

class ListCryptoPoliciesRequest(_message.Message):
    __slots__ = ("name_prefix", "page_size", "page_token")
    NAME_PREFIX_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    name_prefix: str
    page_size: int
    page_token: str
    def __init__(self, name_prefix: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class ListCryptoPoliciesResponse(_message.Message):
    __slots__ = ("policies", "next_page_token")
    POLICIES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    policies: _containers.RepeatedCompositeFieldContainer[PolicySummary]
    next_page_token: str
    def __init__(self, policies: _Optional[_Iterable[_Union[PolicySummary, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class PolicySummary(_message.Message):
    __slots__ = ("name", "created_at", "updated_at", "version", "format")
    NAME_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    FORMAT_FIELD_NUMBER: _ClassVar[int]
    name: str
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    version: int
    format: str
    def __init__(self, name: _Optional[str] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., version: _Optional[int] = ..., format: _Optional[str] = ...) -> None: ...

class EvaluatePolicyRequest(_message.Message):
    __slots__ = ("policy_name", "operation", "key_name", "template_id", "scope_spec", "provider_id", "properties")
    class PropertiesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    POLICY_NAME_FIELD_NUMBER: _ClassVar[int]
    OPERATION_FIELD_NUMBER: _ClassVar[int]
    KEY_NAME_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    SCOPE_SPEC_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_ID_FIELD_NUMBER: _ClassVar[int]
    PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    policy_name: str
    operation: _common_pb2.CryptoOperation
    key_name: str
    template_id: str
    scope_spec: _common_pb2.ScopeSpecification
    provider_id: str
    properties: _containers.ScalarMap[str, str]
    def __init__(self, policy_name: _Optional[str] = ..., operation: _Optional[_Union[_common_pb2.CryptoOperation, str]] = ..., key_name: _Optional[str] = ..., template_id: _Optional[str] = ..., scope_spec: _Optional[_Union[_common_pb2.ScopeSpecification, _Mapping]] = ..., provider_id: _Optional[str] = ..., properties: _Optional[_Mapping[str, str]] = ...) -> None: ...

class EvaluatePolicyResponse(_message.Message):
    __slots__ = ("allowed", "denial_reason", "message", "details")
    ALLOWED_FIELD_NUMBER: _ClassVar[int]
    DENIAL_REASON_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    DETAILS_FIELD_NUMBER: _ClassVar[int]
    allowed: bool
    denial_reason: PolicyDenialReason
    message: str
    details: PolicyDecisionDetails
    def __init__(self, allowed: _Optional[bool] = ..., denial_reason: _Optional[_Union[PolicyDenialReason, str]] = ..., message: _Optional[str] = ..., details: _Optional[_Union[PolicyDecisionDetails, _Mapping]] = ...) -> None: ...

class PolicyDecisionDetails(_message.Message):
    __slots__ = ("policy_name", "policy_version", "evaluation_timestamp", "checks_performed", "failed_check", "allowed_templates", "allowed_operations", "allowed_scopes")
    POLICY_NAME_FIELD_NUMBER: _ClassVar[int]
    POLICY_VERSION_FIELD_NUMBER: _ClassVar[int]
    EVALUATION_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    CHECKS_PERFORMED_FIELD_NUMBER: _ClassVar[int]
    FAILED_CHECK_FIELD_NUMBER: _ClassVar[int]
    ALLOWED_TEMPLATES_FIELD_NUMBER: _ClassVar[int]
    ALLOWED_OPERATIONS_FIELD_NUMBER: _ClassVar[int]
    ALLOWED_SCOPES_FIELD_NUMBER: _ClassVar[int]
    policy_name: str
    policy_version: str
    evaluation_timestamp: _timestamp_pb2.Timestamp
    checks_performed: _containers.RepeatedScalarFieldContainer[str]
    failed_check: str
    allowed_templates: _containers.RepeatedScalarFieldContainer[str]
    allowed_operations: _containers.RepeatedScalarFieldContainer[_common_pb2.CryptoOperation]
    allowed_scopes: _containers.RepeatedCompositeFieldContainer[_common_pb2.ScopeSpecification]
    def __init__(self, policy_name: _Optional[str] = ..., policy_version: _Optional[str] = ..., evaluation_timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., checks_performed: _Optional[_Iterable[str]] = ..., failed_check: _Optional[str] = ..., allowed_templates: _Optional[_Iterable[str]] = ..., allowed_operations: _Optional[_Iterable[_Union[_common_pb2.CryptoOperation, str]]] = ..., allowed_scopes: _Optional[_Iterable[_Union[_common_pb2.ScopeSpecification, _Mapping]]] = ...) -> None: ...

class BatchEvaluatePolicyRequest(_message.Message):
    __slots__ = ("evaluations",)
    EVALUATIONS_FIELD_NUMBER: _ClassVar[int]
    evaluations: _containers.RepeatedCompositeFieldContainer[EvaluatePolicyRequest]
    def __init__(self, evaluations: _Optional[_Iterable[_Union[EvaluatePolicyRequest, _Mapping]]] = ...) -> None: ...

class BatchEvaluatePolicyResponse(_message.Message):
    __slots__ = ("results", "allowed_count", "denied_count")
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    ALLOWED_COUNT_FIELD_NUMBER: _ClassVar[int]
    DENIED_COUNT_FIELD_NUMBER: _ClassVar[int]
    results: _containers.RepeatedCompositeFieldContainer[EvaluatePolicyResponse]
    allowed_count: int
    denied_count: int
    def __init__(self, results: _Optional[_Iterable[_Union[EvaluatePolicyResponse, _Mapping]]] = ..., allowed_count: _Optional[int] = ..., denied_count: _Optional[int] = ...) -> None: ...
