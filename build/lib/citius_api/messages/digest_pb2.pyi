from citius_api.types import common_pb2 as _common_pb2
from citius_api.messages import metadata_pb2 as _metadata_pb2
from citius_api.buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DigestInitRequest(_message.Message):
    __slots__ = ("scope_spec", "template_id", "policy_name", "user_context")
    class UserContextEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    SCOPE_SPEC_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    POLICY_NAME_FIELD_NUMBER: _ClassVar[int]
    USER_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    scope_spec: _common_pb2.ScopeSpecification
    template_id: str
    policy_name: str
    user_context: _containers.ScalarMap[str, str]
    def __init__(self, scope_spec: _Optional[_Union[_common_pb2.ScopeSpecification, _Mapping]] = ..., template_id: _Optional[str] = ..., policy_name: _Optional[str] = ..., user_context: _Optional[_Mapping[str, str]] = ...) -> None: ...

class DigestInitResponse(_message.Message):
    __slots__ = ("success", "selected_template_id", "operation_id")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    SELECTED_TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    OPERATION_ID_FIELD_NUMBER: _ClassVar[int]
    success: bool
    selected_template_id: str
    operation_id: str
    def __init__(self, success: _Optional[bool] = ..., selected_template_id: _Optional[str] = ..., operation_id: _Optional[str] = ...) -> None: ...

class DigestRequest(_message.Message):
    __slots__ = ("scope_spec", "template_id", "data", "policy_name", "user_context")
    class UserContextEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    SCOPE_SPEC_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    POLICY_NAME_FIELD_NUMBER: _ClassVar[int]
    USER_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    scope_spec: _common_pb2.ScopeSpecification
    template_id: str
    data: bytes
    policy_name: str
    user_context: _containers.ScalarMap[str, str]
    def __init__(self, scope_spec: _Optional[_Union[_common_pb2.ScopeSpecification, _Mapping]] = ..., template_id: _Optional[str] = ..., data: _Optional[bytes] = ..., policy_name: _Optional[str] = ..., user_context: _Optional[_Mapping[str, str]] = ...) -> None: ...

class DigestResponse(_message.Message):
    __slots__ = ("digest", "metadata")
    DIGEST_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    digest: bytes
    metadata: _metadata_pb2.OperationMetadata
    def __init__(self, digest: _Optional[bytes] = ..., metadata: _Optional[_Union[_metadata_pb2.OperationMetadata, _Mapping]] = ...) -> None: ...

class DigestUpdateRequest(_message.Message):
    __slots__ = ("operation_id", "data_chunk")
    OPERATION_ID_FIELD_NUMBER: _ClassVar[int]
    DATA_CHUNK_FIELD_NUMBER: _ClassVar[int]
    operation_id: str
    data_chunk: bytes
    def __init__(self, operation_id: _Optional[str] = ..., data_chunk: _Optional[bytes] = ...) -> None: ...

class DigestUpdateResponse(_message.Message):
    __slots__ = ("success",)
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    success: bool
    def __init__(self, success: _Optional[bool] = ...) -> None: ...

class DigestKeyRequest(_message.Message):
    __slots__ = ("operation_id", "key_name")
    OPERATION_ID_FIELD_NUMBER: _ClassVar[int]
    KEY_NAME_FIELD_NUMBER: _ClassVar[int]
    operation_id: str
    key_name: str
    def __init__(self, operation_id: _Optional[str] = ..., key_name: _Optional[str] = ...) -> None: ...

class DigestKeyResponse(_message.Message):
    __slots__ = ("success",)
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    success: bool
    def __init__(self, success: _Optional[bool] = ...) -> None: ...

class DigestFinalRequest(_message.Message):
    __slots__ = ("operation_id",)
    OPERATION_ID_FIELD_NUMBER: _ClassVar[int]
    operation_id: str
    def __init__(self, operation_id: _Optional[str] = ...) -> None: ...

class DigestFinalResponse(_message.Message):
    __slots__ = ("digest", "metadata")
    DIGEST_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    digest: bytes
    metadata: _metadata_pb2.OperationMetadata
    def __init__(self, digest: _Optional[bytes] = ..., metadata: _Optional[_Union[_metadata_pb2.OperationMetadata, _Mapping]] = ...) -> None: ...

class XofRequest(_message.Message):
    __slots__ = ("scope_spec", "template_id", "data", "output_length_bytes", "policy_name", "user_context")
    class UserContextEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    SCOPE_SPEC_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_LENGTH_BYTES_FIELD_NUMBER: _ClassVar[int]
    POLICY_NAME_FIELD_NUMBER: _ClassVar[int]
    USER_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    scope_spec: _common_pb2.ScopeSpecification
    template_id: str
    data: bytes
    output_length_bytes: int
    policy_name: str
    user_context: _containers.ScalarMap[str, str]
    def __init__(self, scope_spec: _Optional[_Union[_common_pb2.ScopeSpecification, _Mapping]] = ..., template_id: _Optional[str] = ..., data: _Optional[bytes] = ..., output_length_bytes: _Optional[int] = ..., policy_name: _Optional[str] = ..., user_context: _Optional[_Mapping[str, str]] = ...) -> None: ...

class XofResponse(_message.Message):
    __slots__ = ("output", "metadata")
    OUTPUT_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    output: bytes
    metadata: _metadata_pb2.OperationMetadata
    def __init__(self, output: _Optional[bytes] = ..., metadata: _Optional[_Union[_metadata_pb2.OperationMetadata, _Mapping]] = ...) -> None: ...

class XofInitRequest(_message.Message):
    __slots__ = ("scope_spec", "template_id", "output_length_bytes", "policy_name", "user_context")
    class UserContextEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    SCOPE_SPEC_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_LENGTH_BYTES_FIELD_NUMBER: _ClassVar[int]
    POLICY_NAME_FIELD_NUMBER: _ClassVar[int]
    USER_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    scope_spec: _common_pb2.ScopeSpecification
    template_id: str
    output_length_bytes: int
    policy_name: str
    user_context: _containers.ScalarMap[str, str]
    def __init__(self, scope_spec: _Optional[_Union[_common_pb2.ScopeSpecification, _Mapping]] = ..., template_id: _Optional[str] = ..., output_length_bytes: _Optional[int] = ..., policy_name: _Optional[str] = ..., user_context: _Optional[_Mapping[str, str]] = ...) -> None: ...

class XofInitResponse(_message.Message):
    __slots__ = ("success", "selected_template_id", "operation_id")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    SELECTED_TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    OPERATION_ID_FIELD_NUMBER: _ClassVar[int]
    success: bool
    selected_template_id: str
    operation_id: str
    def __init__(self, success: _Optional[bool] = ..., selected_template_id: _Optional[str] = ..., operation_id: _Optional[str] = ...) -> None: ...

class XofUpdateRequest(_message.Message):
    __slots__ = ("operation_id", "data_chunk")
    OPERATION_ID_FIELD_NUMBER: _ClassVar[int]
    DATA_CHUNK_FIELD_NUMBER: _ClassVar[int]
    operation_id: str
    data_chunk: bytes
    def __init__(self, operation_id: _Optional[str] = ..., data_chunk: _Optional[bytes] = ...) -> None: ...

class XofUpdateResponse(_message.Message):
    __slots__ = ("success",)
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    success: bool
    def __init__(self, success: _Optional[bool] = ...) -> None: ...

class XofFinalRequest(_message.Message):
    __slots__ = ("operation_id",)
    OPERATION_ID_FIELD_NUMBER: _ClassVar[int]
    operation_id: str
    def __init__(self, operation_id: _Optional[str] = ...) -> None: ...

class XofFinalResponse(_message.Message):
    __slots__ = ("output", "metadata")
    OUTPUT_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    output: bytes
    metadata: _metadata_pb2.OperationMetadata
    def __init__(self, output: _Optional[bytes] = ..., metadata: _Optional[_Union[_metadata_pb2.OperationMetadata, _Mapping]] = ...) -> None: ...
