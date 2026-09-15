from citius_api.messages import metadata_pb2 as _metadata_pb2
from citius_api.buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GenerateRandomRequest(_message.Message):
    __slots__ = ("num_bytes", "provider_id", "policy_name", "user_context")
    class UserContextEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    NUM_BYTES_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_ID_FIELD_NUMBER: _ClassVar[int]
    POLICY_NAME_FIELD_NUMBER: _ClassVar[int]
    USER_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    num_bytes: int
    provider_id: str
    policy_name: str
    user_context: _containers.ScalarMap[str, str]
    def __init__(self, num_bytes: _Optional[int] = ..., provider_id: _Optional[str] = ..., policy_name: _Optional[str] = ..., user_context: _Optional[_Mapping[str, str]] = ...) -> None: ...

class GenerateRandomResponse(_message.Message):
    __slots__ = ("random_bytes", "provider_id", "metadata")
    RANDOM_BYTES_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_ID_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    random_bytes: bytes
    provider_id: str
    metadata: _metadata_pb2.OperationMetadata
    def __init__(self, random_bytes: _Optional[bytes] = ..., provider_id: _Optional[str] = ..., metadata: _Optional[_Union[_metadata_pb2.OperationMetadata, _Mapping]] = ...) -> None: ...

class SeedRandomRequest(_message.Message):
    __slots__ = ("seed", "provider_id", "policy_name", "user_context")
    class UserContextEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    SEED_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_ID_FIELD_NUMBER: _ClassVar[int]
    POLICY_NAME_FIELD_NUMBER: _ClassVar[int]
    USER_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    seed: bytes
    provider_id: str
    policy_name: str
    user_context: _containers.ScalarMap[str, str]
    def __init__(self, seed: _Optional[bytes] = ..., provider_id: _Optional[str] = ..., policy_name: _Optional[str] = ..., user_context: _Optional[_Mapping[str, str]] = ...) -> None: ...

class SeedRandomResponse(_message.Message):
    __slots__ = ("success", "message")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    success: bool
    message: str
    def __init__(self, success: _Optional[bool] = ..., message: _Optional[str] = ...) -> None: ...
