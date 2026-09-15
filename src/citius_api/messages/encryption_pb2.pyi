from citius_api.messages import metadata_pb2 as _metadata_pb2
from citius_api.types import operation_params_pb2 as _operation_params_pb2
from citius_api.buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EncryptRequest(_message.Message):
    __slots__ = ("key_name", "plaintext", "no_params", "aead_params", "xts_params", "asymmetric_params", "vendor_params", "user_context")
    class UserContextEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    KEY_NAME_FIELD_NUMBER: _ClassVar[int]
    PLAINTEXT_FIELD_NUMBER: _ClassVar[int]
    NO_PARAMS_FIELD_NUMBER: _ClassVar[int]
    AEAD_PARAMS_FIELD_NUMBER: _ClassVar[int]
    XTS_PARAMS_FIELD_NUMBER: _ClassVar[int]
    ASYMMETRIC_PARAMS_FIELD_NUMBER: _ClassVar[int]
    VENDOR_PARAMS_FIELD_NUMBER: _ClassVar[int]
    USER_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    key_name: str
    plaintext: bytes
    no_params: _operation_params_pb2.NoParams
    aead_params: _operation_params_pb2.AeadEncryptParams
    xts_params: _operation_params_pb2.XtsEncryptParams
    asymmetric_params: _operation_params_pb2.AsymmetricEncryptParams
    vendor_params: _operation_params_pb2.VendorEncryptionParams
    user_context: _containers.ScalarMap[str, str]
    def __init__(self, key_name: _Optional[str] = ..., plaintext: _Optional[bytes] = ..., no_params: _Optional[_Union[_operation_params_pb2.NoParams, _Mapping]] = ..., aead_params: _Optional[_Union[_operation_params_pb2.AeadEncryptParams, _Mapping]] = ..., xts_params: _Optional[_Union[_operation_params_pb2.XtsEncryptParams, _Mapping]] = ..., asymmetric_params: _Optional[_Union[_operation_params_pb2.AsymmetricEncryptParams, _Mapping]] = ..., vendor_params: _Optional[_Union[_operation_params_pb2.VendorEncryptionParams, _Mapping]] = ..., user_context: _Optional[_Mapping[str, str]] = ...) -> None: ...

class EncryptResponse(_message.Message):
    __slots__ = ("ciphertext", "metadata")
    CIPHERTEXT_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    ciphertext: bytes
    metadata: _metadata_pb2.OperationMetadata
    def __init__(self, ciphertext: _Optional[bytes] = ..., metadata: _Optional[_Union[_metadata_pb2.OperationMetadata, _Mapping]] = ...) -> None: ...

class DecryptRequest(_message.Message):
    __slots__ = ("key_name", "ciphertext", "metadata", "no_params", "aead_params", "xts_params", "asymmetric_params", "vendor_params", "user_context")
    class UserContextEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    KEY_NAME_FIELD_NUMBER: _ClassVar[int]
    CIPHERTEXT_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    NO_PARAMS_FIELD_NUMBER: _ClassVar[int]
    AEAD_PARAMS_FIELD_NUMBER: _ClassVar[int]
    XTS_PARAMS_FIELD_NUMBER: _ClassVar[int]
    ASYMMETRIC_PARAMS_FIELD_NUMBER: _ClassVar[int]
    VENDOR_PARAMS_FIELD_NUMBER: _ClassVar[int]
    USER_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    key_name: str
    ciphertext: bytes
    metadata: _metadata_pb2.OperationMetadata
    no_params: _operation_params_pb2.NoParams
    aead_params: _operation_params_pb2.AeadEncryptParams
    xts_params: _operation_params_pb2.XtsEncryptParams
    asymmetric_params: _operation_params_pb2.AsymmetricEncryptParams
    vendor_params: _operation_params_pb2.VendorEncryptionParams
    user_context: _containers.ScalarMap[str, str]
    def __init__(self, key_name: _Optional[str] = ..., ciphertext: _Optional[bytes] = ..., metadata: _Optional[_Union[_metadata_pb2.OperationMetadata, _Mapping]] = ..., no_params: _Optional[_Union[_operation_params_pb2.NoParams, _Mapping]] = ..., aead_params: _Optional[_Union[_operation_params_pb2.AeadEncryptParams, _Mapping]] = ..., xts_params: _Optional[_Union[_operation_params_pb2.XtsEncryptParams, _Mapping]] = ..., asymmetric_params: _Optional[_Union[_operation_params_pb2.AsymmetricEncryptParams, _Mapping]] = ..., vendor_params: _Optional[_Union[_operation_params_pb2.VendorEncryptionParams, _Mapping]] = ..., user_context: _Optional[_Mapping[str, str]] = ...) -> None: ...

class DecryptResponse(_message.Message):
    __slots__ = ("plaintext", "metadata")
    PLAINTEXT_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    plaintext: bytes
    metadata: _metadata_pb2.OperationMetadata
    def __init__(self, plaintext: _Optional[bytes] = ..., metadata: _Optional[_Union[_metadata_pb2.OperationMetadata, _Mapping]] = ...) -> None: ...

class EncryptInitRequest(_message.Message):
    __slots__ = ("key_name", "no_params", "aead_params", "xts_params", "asymmetric_params", "vendor_params", "user_context")
    class UserContextEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    KEY_NAME_FIELD_NUMBER: _ClassVar[int]
    NO_PARAMS_FIELD_NUMBER: _ClassVar[int]
    AEAD_PARAMS_FIELD_NUMBER: _ClassVar[int]
    XTS_PARAMS_FIELD_NUMBER: _ClassVar[int]
    ASYMMETRIC_PARAMS_FIELD_NUMBER: _ClassVar[int]
    VENDOR_PARAMS_FIELD_NUMBER: _ClassVar[int]
    USER_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    key_name: str
    no_params: _operation_params_pb2.NoParams
    aead_params: _operation_params_pb2.AeadEncryptParams
    xts_params: _operation_params_pb2.XtsEncryptParams
    asymmetric_params: _operation_params_pb2.AsymmetricEncryptParams
    vendor_params: _operation_params_pb2.VendorEncryptionParams
    user_context: _containers.ScalarMap[str, str]
    def __init__(self, key_name: _Optional[str] = ..., no_params: _Optional[_Union[_operation_params_pb2.NoParams, _Mapping]] = ..., aead_params: _Optional[_Union[_operation_params_pb2.AeadEncryptParams, _Mapping]] = ..., xts_params: _Optional[_Union[_operation_params_pb2.XtsEncryptParams, _Mapping]] = ..., asymmetric_params: _Optional[_Union[_operation_params_pb2.AsymmetricEncryptParams, _Mapping]] = ..., vendor_params: _Optional[_Union[_operation_params_pb2.VendorEncryptionParams, _Mapping]] = ..., user_context: _Optional[_Mapping[str, str]] = ...) -> None: ...

class EncryptInitResponse(_message.Message):
    __slots__ = ("success", "operation_id")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    OPERATION_ID_FIELD_NUMBER: _ClassVar[int]
    success: bool
    operation_id: str
    def __init__(self, success: _Optional[bool] = ..., operation_id: _Optional[str] = ...) -> None: ...

class EncryptUpdateRequest(_message.Message):
    __slots__ = ("operation_id", "plaintext_chunk")
    OPERATION_ID_FIELD_NUMBER: _ClassVar[int]
    PLAINTEXT_CHUNK_FIELD_NUMBER: _ClassVar[int]
    operation_id: str
    plaintext_chunk: bytes
    def __init__(self, operation_id: _Optional[str] = ..., plaintext_chunk: _Optional[bytes] = ...) -> None: ...

class EncryptUpdateResponse(_message.Message):
    __slots__ = ("ciphertext_chunk",)
    CIPHERTEXT_CHUNK_FIELD_NUMBER: _ClassVar[int]
    ciphertext_chunk: bytes
    def __init__(self, ciphertext_chunk: _Optional[bytes] = ...) -> None: ...

class EncryptFinalRequest(_message.Message):
    __slots__ = ("operation_id",)
    OPERATION_ID_FIELD_NUMBER: _ClassVar[int]
    operation_id: str
    def __init__(self, operation_id: _Optional[str] = ...) -> None: ...

class EncryptFinalResponse(_message.Message):
    __slots__ = ("ciphertext_final", "metadata")
    CIPHERTEXT_FINAL_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    ciphertext_final: bytes
    metadata: _metadata_pb2.OperationMetadata
    def __init__(self, ciphertext_final: _Optional[bytes] = ..., metadata: _Optional[_Union[_metadata_pb2.OperationMetadata, _Mapping]] = ...) -> None: ...

class DecryptInitRequest(_message.Message):
    __slots__ = ("key_name", "no_params", "aead_params", "xts_params", "asymmetric_params", "vendor_params", "metadata", "user_context")
    class UserContextEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    KEY_NAME_FIELD_NUMBER: _ClassVar[int]
    NO_PARAMS_FIELD_NUMBER: _ClassVar[int]
    AEAD_PARAMS_FIELD_NUMBER: _ClassVar[int]
    XTS_PARAMS_FIELD_NUMBER: _ClassVar[int]
    ASYMMETRIC_PARAMS_FIELD_NUMBER: _ClassVar[int]
    VENDOR_PARAMS_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    USER_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    key_name: str
    no_params: _operation_params_pb2.NoParams
    aead_params: _operation_params_pb2.AeadEncryptParams
    xts_params: _operation_params_pb2.XtsEncryptParams
    asymmetric_params: _operation_params_pb2.AsymmetricEncryptParams
    vendor_params: _operation_params_pb2.VendorEncryptionParams
    metadata: _metadata_pb2.OperationMetadata
    user_context: _containers.ScalarMap[str, str]
    def __init__(self, key_name: _Optional[str] = ..., no_params: _Optional[_Union[_operation_params_pb2.NoParams, _Mapping]] = ..., aead_params: _Optional[_Union[_operation_params_pb2.AeadEncryptParams, _Mapping]] = ..., xts_params: _Optional[_Union[_operation_params_pb2.XtsEncryptParams, _Mapping]] = ..., asymmetric_params: _Optional[_Union[_operation_params_pb2.AsymmetricEncryptParams, _Mapping]] = ..., vendor_params: _Optional[_Union[_operation_params_pb2.VendorEncryptionParams, _Mapping]] = ..., metadata: _Optional[_Union[_metadata_pb2.OperationMetadata, _Mapping]] = ..., user_context: _Optional[_Mapping[str, str]] = ...) -> None: ...

class DecryptInitResponse(_message.Message):
    __slots__ = ("success", "operation_id")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    OPERATION_ID_FIELD_NUMBER: _ClassVar[int]
    success: bool
    operation_id: str
    def __init__(self, success: _Optional[bool] = ..., operation_id: _Optional[str] = ...) -> None: ...

class DecryptUpdateRequest(_message.Message):
    __slots__ = ("operation_id", "ciphertext_chunk")
    OPERATION_ID_FIELD_NUMBER: _ClassVar[int]
    CIPHERTEXT_CHUNK_FIELD_NUMBER: _ClassVar[int]
    operation_id: str
    ciphertext_chunk: bytes
    def __init__(self, operation_id: _Optional[str] = ..., ciphertext_chunk: _Optional[bytes] = ...) -> None: ...

class DecryptUpdateResponse(_message.Message):
    __slots__ = ("plaintext_chunk",)
    PLAINTEXT_CHUNK_FIELD_NUMBER: _ClassVar[int]
    plaintext_chunk: bytes
    def __init__(self, plaintext_chunk: _Optional[bytes] = ...) -> None: ...

class DecryptFinalRequest(_message.Message):
    __slots__ = ("operation_id",)
    OPERATION_ID_FIELD_NUMBER: _ClassVar[int]
    operation_id: str
    def __init__(self, operation_id: _Optional[str] = ...) -> None: ...

class DecryptFinalResponse(_message.Message):
    __slots__ = ("plaintext_final", "metadata")
    PLAINTEXT_FINAL_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    plaintext_final: bytes
    metadata: _metadata_pb2.OperationMetadata
    def __init__(self, plaintext_final: _Optional[bytes] = ..., metadata: _Optional[_Union[_metadata_pb2.OperationMetadata, _Mapping]] = ...) -> None: ...

class EncryptMessageInitRequest(_message.Message):
    __slots__ = ("key_name", "no_params", "aead_params", "xts_params", "asymmetric_params", "vendor_params", "user_context")
    class UserContextEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    KEY_NAME_FIELD_NUMBER: _ClassVar[int]
    NO_PARAMS_FIELD_NUMBER: _ClassVar[int]
    AEAD_PARAMS_FIELD_NUMBER: _ClassVar[int]
    XTS_PARAMS_FIELD_NUMBER: _ClassVar[int]
    ASYMMETRIC_PARAMS_FIELD_NUMBER: _ClassVar[int]
    VENDOR_PARAMS_FIELD_NUMBER: _ClassVar[int]
    USER_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    key_name: str
    no_params: _operation_params_pb2.NoParams
    aead_params: _operation_params_pb2.AeadEncryptParams
    xts_params: _operation_params_pb2.XtsEncryptParams
    asymmetric_params: _operation_params_pb2.AsymmetricEncryptParams
    vendor_params: _operation_params_pb2.VendorEncryptionParams
    user_context: _containers.ScalarMap[str, str]
    def __init__(self, key_name: _Optional[str] = ..., no_params: _Optional[_Union[_operation_params_pb2.NoParams, _Mapping]] = ..., aead_params: _Optional[_Union[_operation_params_pb2.AeadEncryptParams, _Mapping]] = ..., xts_params: _Optional[_Union[_operation_params_pb2.XtsEncryptParams, _Mapping]] = ..., asymmetric_params: _Optional[_Union[_operation_params_pb2.AsymmetricEncryptParams, _Mapping]] = ..., vendor_params: _Optional[_Union[_operation_params_pb2.VendorEncryptionParams, _Mapping]] = ..., user_context: _Optional[_Mapping[str, str]] = ...) -> None: ...

class EncryptMessageInitResponse(_message.Message):
    __slots__ = ("success", "operation_id")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    OPERATION_ID_FIELD_NUMBER: _ClassVar[int]
    success: bool
    operation_id: str
    def __init__(self, success: _Optional[bool] = ..., operation_id: _Optional[str] = ...) -> None: ...

class EncryptMessageRequest(_message.Message):
    __slots__ = ("key_name", "associated_data", "plaintext", "operation_id", "user_context")
    class UserContextEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    KEY_NAME_FIELD_NUMBER: _ClassVar[int]
    ASSOCIATED_DATA_FIELD_NUMBER: _ClassVar[int]
    PLAINTEXT_FIELD_NUMBER: _ClassVar[int]
    OPERATION_ID_FIELD_NUMBER: _ClassVar[int]
    USER_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    key_name: str
    associated_data: bytes
    plaintext: bytes
    operation_id: str
    user_context: _containers.ScalarMap[str, str]
    def __init__(self, key_name: _Optional[str] = ..., associated_data: _Optional[bytes] = ..., plaintext: _Optional[bytes] = ..., operation_id: _Optional[str] = ..., user_context: _Optional[_Mapping[str, str]] = ...) -> None: ...

class EncryptMessageResponse(_message.Message):
    __slots__ = ("ciphertext", "metadata")
    CIPHERTEXT_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    ciphertext: bytes
    metadata: _metadata_pb2.OperationMetadata
    def __init__(self, ciphertext: _Optional[bytes] = ..., metadata: _Optional[_Union[_metadata_pb2.OperationMetadata, _Mapping]] = ...) -> None: ...

class EncryptMessageBeginRequest(_message.Message):
    __slots__ = ("operation_id", "associated_data")
    OPERATION_ID_FIELD_NUMBER: _ClassVar[int]
    ASSOCIATED_DATA_FIELD_NUMBER: _ClassVar[int]
    operation_id: str
    associated_data: bytes
    def __init__(self, operation_id: _Optional[str] = ..., associated_data: _Optional[bytes] = ...) -> None: ...

class EncryptMessageBeginResponse(_message.Message):
    __slots__ = ("success", "partial_metadata")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    PARTIAL_METADATA_FIELD_NUMBER: _ClassVar[int]
    success: bool
    partial_metadata: _metadata_pb2.OperationMetadata
    def __init__(self, success: _Optional[bool] = ..., partial_metadata: _Optional[_Union[_metadata_pb2.OperationMetadata, _Mapping]] = ...) -> None: ...

class EncryptMessageNextRequest(_message.Message):
    __slots__ = ("operation_id", "plaintext_chunk", "end_of_message")
    OPERATION_ID_FIELD_NUMBER: _ClassVar[int]
    PLAINTEXT_CHUNK_FIELD_NUMBER: _ClassVar[int]
    END_OF_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    operation_id: str
    plaintext_chunk: bytes
    end_of_message: bool
    def __init__(self, operation_id: _Optional[str] = ..., plaintext_chunk: _Optional[bytes] = ..., end_of_message: _Optional[bool] = ...) -> None: ...

class EncryptMessageNextResponse(_message.Message):
    __slots__ = ("ciphertext_chunk",)
    CIPHERTEXT_CHUNK_FIELD_NUMBER: _ClassVar[int]
    ciphertext_chunk: bytes
    def __init__(self, ciphertext_chunk: _Optional[bytes] = ...) -> None: ...

class EncryptMessageFinalRequest(_message.Message):
    __slots__ = ("operation_id",)
    OPERATION_ID_FIELD_NUMBER: _ClassVar[int]
    operation_id: str
    def __init__(self, operation_id: _Optional[str] = ...) -> None: ...

class EncryptMessageFinalResponse(_message.Message):
    __slots__ = ("success",)
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    success: bool
    def __init__(self, success: _Optional[bool] = ...) -> None: ...

class DecryptMessageInitRequest(_message.Message):
    __slots__ = ("key_name", "no_params", "aead_params", "xts_params", "asymmetric_params", "vendor_params", "user_context")
    class UserContextEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    KEY_NAME_FIELD_NUMBER: _ClassVar[int]
    NO_PARAMS_FIELD_NUMBER: _ClassVar[int]
    AEAD_PARAMS_FIELD_NUMBER: _ClassVar[int]
    XTS_PARAMS_FIELD_NUMBER: _ClassVar[int]
    ASYMMETRIC_PARAMS_FIELD_NUMBER: _ClassVar[int]
    VENDOR_PARAMS_FIELD_NUMBER: _ClassVar[int]
    USER_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    key_name: str
    no_params: _operation_params_pb2.NoParams
    aead_params: _operation_params_pb2.AeadEncryptParams
    xts_params: _operation_params_pb2.XtsEncryptParams
    asymmetric_params: _operation_params_pb2.AsymmetricEncryptParams
    vendor_params: _operation_params_pb2.VendorEncryptionParams
    user_context: _containers.ScalarMap[str, str]
    def __init__(self, key_name: _Optional[str] = ..., no_params: _Optional[_Union[_operation_params_pb2.NoParams, _Mapping]] = ..., aead_params: _Optional[_Union[_operation_params_pb2.AeadEncryptParams, _Mapping]] = ..., xts_params: _Optional[_Union[_operation_params_pb2.XtsEncryptParams, _Mapping]] = ..., asymmetric_params: _Optional[_Union[_operation_params_pb2.AsymmetricEncryptParams, _Mapping]] = ..., vendor_params: _Optional[_Union[_operation_params_pb2.VendorEncryptionParams, _Mapping]] = ..., user_context: _Optional[_Mapping[str, str]] = ...) -> None: ...

class DecryptMessageInitResponse(_message.Message):
    __slots__ = ("success", "operation_id")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    OPERATION_ID_FIELD_NUMBER: _ClassVar[int]
    success: bool
    operation_id: str
    def __init__(self, success: _Optional[bool] = ..., operation_id: _Optional[str] = ...) -> None: ...

class DecryptMessageRequest(_message.Message):
    __slots__ = ("key_name", "associated_data", "ciphertext", "metadata", "operation_id", "user_context")
    class UserContextEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    KEY_NAME_FIELD_NUMBER: _ClassVar[int]
    ASSOCIATED_DATA_FIELD_NUMBER: _ClassVar[int]
    CIPHERTEXT_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    OPERATION_ID_FIELD_NUMBER: _ClassVar[int]
    USER_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    key_name: str
    associated_data: bytes
    ciphertext: bytes
    metadata: _metadata_pb2.OperationMetadata
    operation_id: str
    user_context: _containers.ScalarMap[str, str]
    def __init__(self, key_name: _Optional[str] = ..., associated_data: _Optional[bytes] = ..., ciphertext: _Optional[bytes] = ..., metadata: _Optional[_Union[_metadata_pb2.OperationMetadata, _Mapping]] = ..., operation_id: _Optional[str] = ..., user_context: _Optional[_Mapping[str, str]] = ...) -> None: ...

class DecryptMessageResponse(_message.Message):
    __slots__ = ("plaintext", "metadata")
    PLAINTEXT_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    plaintext: bytes
    metadata: _metadata_pb2.OperationMetadata
    def __init__(self, plaintext: _Optional[bytes] = ..., metadata: _Optional[_Union[_metadata_pb2.OperationMetadata, _Mapping]] = ...) -> None: ...

class DecryptMessageBeginRequest(_message.Message):
    __slots__ = ("operation_id", "associated_data", "partial_metadata")
    OPERATION_ID_FIELD_NUMBER: _ClassVar[int]
    ASSOCIATED_DATA_FIELD_NUMBER: _ClassVar[int]
    PARTIAL_METADATA_FIELD_NUMBER: _ClassVar[int]
    operation_id: str
    associated_data: bytes
    partial_metadata: _metadata_pb2.OperationMetadata
    def __init__(self, operation_id: _Optional[str] = ..., associated_data: _Optional[bytes] = ..., partial_metadata: _Optional[_Union[_metadata_pb2.OperationMetadata, _Mapping]] = ...) -> None: ...

class DecryptMessageBeginResponse(_message.Message):
    __slots__ = ("success",)
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    success: bool
    def __init__(self, success: _Optional[bool] = ...) -> None: ...

class DecryptMessageNextRequest(_message.Message):
    __slots__ = ("operation_id", "ciphertext_chunk", "end_of_message")
    OPERATION_ID_FIELD_NUMBER: _ClassVar[int]
    CIPHERTEXT_CHUNK_FIELD_NUMBER: _ClassVar[int]
    END_OF_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    operation_id: str
    ciphertext_chunk: bytes
    end_of_message: bool
    def __init__(self, operation_id: _Optional[str] = ..., ciphertext_chunk: _Optional[bytes] = ..., end_of_message: _Optional[bool] = ...) -> None: ...

class DecryptMessageNextResponse(_message.Message):
    __slots__ = ("plaintext_chunk",)
    PLAINTEXT_CHUNK_FIELD_NUMBER: _ClassVar[int]
    plaintext_chunk: bytes
    def __init__(self, plaintext_chunk: _Optional[bytes] = ...) -> None: ...

class DecryptMessageFinalRequest(_message.Message):
    __slots__ = ("operation_id",)
    OPERATION_ID_FIELD_NUMBER: _ClassVar[int]
    operation_id: str
    def __init__(self, operation_id: _Optional[str] = ...) -> None: ...

class DecryptMessageFinalResponse(_message.Message):
    __slots__ = ("success",)
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    success: bool
    def __init__(self, success: _Optional[bool] = ...) -> None: ...

class DigestEncryptUpdateRequest(_message.Message):
    __slots__ = ("digest_operation_id", "encrypt_operation_id", "plaintext_chunk")
    DIGEST_OPERATION_ID_FIELD_NUMBER: _ClassVar[int]
    ENCRYPT_OPERATION_ID_FIELD_NUMBER: _ClassVar[int]
    PLAINTEXT_CHUNK_FIELD_NUMBER: _ClassVar[int]
    digest_operation_id: str
    encrypt_operation_id: str
    plaintext_chunk: bytes
    def __init__(self, digest_operation_id: _Optional[str] = ..., encrypt_operation_id: _Optional[str] = ..., plaintext_chunk: _Optional[bytes] = ...) -> None: ...

class DigestEncryptUpdateResponse(_message.Message):
    __slots__ = ("ciphertext_chunk",)
    CIPHERTEXT_CHUNK_FIELD_NUMBER: _ClassVar[int]
    ciphertext_chunk: bytes
    def __init__(self, ciphertext_chunk: _Optional[bytes] = ...) -> None: ...

class DecryptDigestUpdateRequest(_message.Message):
    __slots__ = ("decrypt_operation_id", "digest_operation_id", "ciphertext_chunk")
    DECRYPT_OPERATION_ID_FIELD_NUMBER: _ClassVar[int]
    DIGEST_OPERATION_ID_FIELD_NUMBER: _ClassVar[int]
    CIPHERTEXT_CHUNK_FIELD_NUMBER: _ClassVar[int]
    decrypt_operation_id: str
    digest_operation_id: str
    ciphertext_chunk: bytes
    def __init__(self, decrypt_operation_id: _Optional[str] = ..., digest_operation_id: _Optional[str] = ..., ciphertext_chunk: _Optional[bytes] = ...) -> None: ...

class DecryptDigestUpdateResponse(_message.Message):
    __slots__ = ("plaintext_chunk",)
    PLAINTEXT_CHUNK_FIELD_NUMBER: _ClassVar[int]
    plaintext_chunk: bytes
    def __init__(self, plaintext_chunk: _Optional[bytes] = ...) -> None: ...

class SignEncryptUpdateRequest(_message.Message):
    __slots__ = ("sign_operation_id", "encrypt_operation_id", "plaintext_chunk")
    SIGN_OPERATION_ID_FIELD_NUMBER: _ClassVar[int]
    ENCRYPT_OPERATION_ID_FIELD_NUMBER: _ClassVar[int]
    PLAINTEXT_CHUNK_FIELD_NUMBER: _ClassVar[int]
    sign_operation_id: str
    encrypt_operation_id: str
    plaintext_chunk: bytes
    def __init__(self, sign_operation_id: _Optional[str] = ..., encrypt_operation_id: _Optional[str] = ..., plaintext_chunk: _Optional[bytes] = ...) -> None: ...

class SignEncryptUpdateResponse(_message.Message):
    __slots__ = ("ciphertext_chunk",)
    CIPHERTEXT_CHUNK_FIELD_NUMBER: _ClassVar[int]
    ciphertext_chunk: bytes
    def __init__(self, ciphertext_chunk: _Optional[bytes] = ...) -> None: ...

class DecryptVerifyUpdateRequest(_message.Message):
    __slots__ = ("decrypt_operation_id", "verify_operation_id", "ciphertext_chunk")
    DECRYPT_OPERATION_ID_FIELD_NUMBER: _ClassVar[int]
    VERIFY_OPERATION_ID_FIELD_NUMBER: _ClassVar[int]
    CIPHERTEXT_CHUNK_FIELD_NUMBER: _ClassVar[int]
    decrypt_operation_id: str
    verify_operation_id: str
    ciphertext_chunk: bytes
    def __init__(self, decrypt_operation_id: _Optional[str] = ..., verify_operation_id: _Optional[str] = ..., ciphertext_chunk: _Optional[bytes] = ...) -> None: ...

class DecryptVerifyUpdateResponse(_message.Message):
    __slots__ = ("plaintext_chunk",)
    PLAINTEXT_CHUNK_FIELD_NUMBER: _ClassVar[int]
    plaintext_chunk: bytes
    def __init__(self, plaintext_chunk: _Optional[bytes] = ...) -> None: ...
