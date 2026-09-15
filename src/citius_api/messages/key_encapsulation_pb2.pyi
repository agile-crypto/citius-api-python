from citius_api.messages import metadata_pb2 as _metadata_pb2
from citius_api.messages import key_management_pb2 as _key_management_pb2
from citius_api.buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EncapsulateKeyRequest(_message.Message):
    __slots__ = ("recipient_public_key_name", "shared_secret_name", "shared_secret_template_id", "user_context")
    class UserContextEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    RECIPIENT_PUBLIC_KEY_NAME_FIELD_NUMBER: _ClassVar[int]
    SHARED_SECRET_NAME_FIELD_NUMBER: _ClassVar[int]
    SHARED_SECRET_TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    USER_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    recipient_public_key_name: str
    shared_secret_name: str
    shared_secret_template_id: str
    user_context: _containers.ScalarMap[str, str]
    def __init__(self, recipient_public_key_name: _Optional[str] = ..., shared_secret_name: _Optional[str] = ..., shared_secret_template_id: _Optional[str] = ..., user_context: _Optional[_Mapping[str, str]] = ...) -> None: ...

class EncapsulateKeyResponse(_message.Message):
    __slots__ = ("ciphertext", "metadata", "key_metadata")
    CIPHERTEXT_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    KEY_METADATA_FIELD_NUMBER: _ClassVar[int]
    ciphertext: bytes
    metadata: _metadata_pb2.OperationMetadata
    key_metadata: _key_management_pb2.KeyMetadata
    def __init__(self, ciphertext: _Optional[bytes] = ..., metadata: _Optional[_Union[_metadata_pb2.OperationMetadata, _Mapping]] = ..., key_metadata: _Optional[_Union[_key_management_pb2.KeyMetadata, _Mapping]] = ...) -> None: ...

class DecapsulateKeyRequest(_message.Message):
    __slots__ = ("private_key_name", "ciphertext", "shared_secret_name", "shared_secret_template_id", "metadata", "user_context")
    class UserContextEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    PRIVATE_KEY_NAME_FIELD_NUMBER: _ClassVar[int]
    CIPHERTEXT_FIELD_NUMBER: _ClassVar[int]
    SHARED_SECRET_NAME_FIELD_NUMBER: _ClassVar[int]
    SHARED_SECRET_TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    USER_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    private_key_name: str
    ciphertext: bytes
    shared_secret_name: str
    shared_secret_template_id: str
    metadata: _metadata_pb2.OperationMetadata
    user_context: _containers.ScalarMap[str, str]
    def __init__(self, private_key_name: _Optional[str] = ..., ciphertext: _Optional[bytes] = ..., shared_secret_name: _Optional[str] = ..., shared_secret_template_id: _Optional[str] = ..., metadata: _Optional[_Union[_metadata_pb2.OperationMetadata, _Mapping]] = ..., user_context: _Optional[_Mapping[str, str]] = ...) -> None: ...

class DecapsulateKeyResponse(_message.Message):
    __slots__ = ("success", "metadata", "key_metadata")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    KEY_METADATA_FIELD_NUMBER: _ClassVar[int]
    success: bool
    metadata: _metadata_pb2.OperationMetadata
    key_metadata: _key_management_pb2.KeyMetadata
    def __init__(self, success: _Optional[bool] = ..., metadata: _Optional[_Union[_metadata_pb2.OperationMetadata, _Mapping]] = ..., key_metadata: _Optional[_Union[_key_management_pb2.KeyMetadata, _Mapping]] = ...) -> None: ...
