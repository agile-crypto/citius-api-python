from citius_api.messages import metadata_pb2 as _metadata_pb2
from citius_api.types import algorithm_params_pb2 as _algorithm_params_pb2
from citius_api.types import common_pb2 as _common_pb2
from citius_api.types import operation_params_pb2 as _operation_params_pb2
from citius_api.buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SignRequest(_message.Message):
    __slots__ = ("key_name", "input", "no_context", "domain_context", "vendor_context", "user_context")
    class UserContextEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    KEY_NAME_FIELD_NUMBER: _ClassVar[int]
    INPUT_FIELD_NUMBER: _ClassVar[int]
    NO_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    VENDOR_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    USER_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    key_name: str
    input: bytes
    no_context: _operation_params_pb2.NoParams
    domain_context: _operation_params_pb2.SignatureDomainContext
    vendor_context: _operation_params_pb2.VendorSignatureContext
    user_context: _containers.ScalarMap[str, str]
    def __init__(self, key_name: _Optional[str] = ..., input: _Optional[bytes] = ..., no_context: _Optional[_Union[_operation_params_pb2.NoParams, _Mapping]] = ..., domain_context: _Optional[_Union[_operation_params_pb2.SignatureDomainContext, _Mapping]] = ..., vendor_context: _Optional[_Union[_operation_params_pb2.VendorSignatureContext, _Mapping]] = ..., user_context: _Optional[_Mapping[str, str]] = ...) -> None: ...

class SignResponse(_message.Message):
    __slots__ = ("signature", "metadata")
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    signature: bytes
    metadata: _metadata_pb2.OperationMetadata
    def __init__(self, signature: _Optional[bytes] = ..., metadata: _Optional[_Union[_metadata_pb2.OperationMetadata, _Mapping]] = ...) -> None: ...

class VerifyRequest(_message.Message):
    __slots__ = ("key_name", "input", "signature", "metadata", "no_context", "domain_context", "vendor_context", "user_context")
    class UserContextEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    KEY_NAME_FIELD_NUMBER: _ClassVar[int]
    INPUT_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    NO_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    VENDOR_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    USER_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    key_name: str
    input: bytes
    signature: bytes
    metadata: _metadata_pb2.OperationMetadata
    no_context: _operation_params_pb2.NoParams
    domain_context: _operation_params_pb2.SignatureDomainContext
    vendor_context: _operation_params_pb2.VendorSignatureContext
    user_context: _containers.ScalarMap[str, str]
    def __init__(self, key_name: _Optional[str] = ..., input: _Optional[bytes] = ..., signature: _Optional[bytes] = ..., metadata: _Optional[_Union[_metadata_pb2.OperationMetadata, _Mapping]] = ..., no_context: _Optional[_Union[_operation_params_pb2.NoParams, _Mapping]] = ..., domain_context: _Optional[_Union[_operation_params_pb2.SignatureDomainContext, _Mapping]] = ..., vendor_context: _Optional[_Union[_operation_params_pb2.VendorSignatureContext, _Mapping]] = ..., user_context: _Optional[_Mapping[str, str]] = ...) -> None: ...

class VerifyResponse(_message.Message):
    __slots__ = ("valid", "metadata")
    VALID_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    valid: bool
    metadata: _metadata_pb2.OperationMetadata
    def __init__(self, valid: _Optional[bool] = ..., metadata: _Optional[_Union[_metadata_pb2.OperationMetadata, _Mapping]] = ...) -> None: ...

class DigestSignRequest(_message.Message):
    __slots__ = ("key_name", "digest", "no_context", "domain_context", "vendor_context", "hash_algorithm", "hash_algorithm_oid", "user_context")
    class UserContextEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    KEY_NAME_FIELD_NUMBER: _ClassVar[int]
    DIGEST_FIELD_NUMBER: _ClassVar[int]
    NO_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    VENDOR_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    HASH_ALGORITHM_FIELD_NUMBER: _ClassVar[int]
    HASH_ALGORITHM_OID_FIELD_NUMBER: _ClassVar[int]
    USER_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    key_name: str
    digest: bytes
    no_context: _operation_params_pb2.NoParams
    domain_context: _operation_params_pb2.SignatureDomainContext
    vendor_context: _operation_params_pb2.VendorSignatureContext
    hash_algorithm: _algorithm_params_pb2.HashAlgorithm
    hash_algorithm_oid: str
    user_context: _containers.ScalarMap[str, str]
    def __init__(self, key_name: _Optional[str] = ..., digest: _Optional[bytes] = ..., no_context: _Optional[_Union[_operation_params_pb2.NoParams, _Mapping]] = ..., domain_context: _Optional[_Union[_operation_params_pb2.SignatureDomainContext, _Mapping]] = ..., vendor_context: _Optional[_Union[_operation_params_pb2.VendorSignatureContext, _Mapping]] = ..., hash_algorithm: _Optional[_Union[_algorithm_params_pb2.HashAlgorithm, str]] = ..., hash_algorithm_oid: _Optional[str] = ..., user_context: _Optional[_Mapping[str, str]] = ...) -> None: ...

class DigestSignResponse(_message.Message):
    __slots__ = ("signature", "metadata")
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    signature: bytes
    metadata: _metadata_pb2.OperationMetadata
    def __init__(self, signature: _Optional[bytes] = ..., metadata: _Optional[_Union[_metadata_pb2.OperationMetadata, _Mapping]] = ...) -> None: ...

class DigestVerifyRequest(_message.Message):
    __slots__ = ("key_name", "digest", "signature", "metadata", "no_context", "domain_context", "vendor_context", "hash_algorithm", "hash_algorithm_oid", "user_context")
    class UserContextEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    KEY_NAME_FIELD_NUMBER: _ClassVar[int]
    DIGEST_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    NO_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    VENDOR_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    HASH_ALGORITHM_FIELD_NUMBER: _ClassVar[int]
    HASH_ALGORITHM_OID_FIELD_NUMBER: _ClassVar[int]
    USER_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    key_name: str
    digest: bytes
    signature: bytes
    metadata: _metadata_pb2.OperationMetadata
    no_context: _operation_params_pb2.NoParams
    domain_context: _operation_params_pb2.SignatureDomainContext
    vendor_context: _operation_params_pb2.VendorSignatureContext
    hash_algorithm: _algorithm_params_pb2.HashAlgorithm
    hash_algorithm_oid: str
    user_context: _containers.ScalarMap[str, str]
    def __init__(self, key_name: _Optional[str] = ..., digest: _Optional[bytes] = ..., signature: _Optional[bytes] = ..., metadata: _Optional[_Union[_metadata_pb2.OperationMetadata, _Mapping]] = ..., no_context: _Optional[_Union[_operation_params_pb2.NoParams, _Mapping]] = ..., domain_context: _Optional[_Union[_operation_params_pb2.SignatureDomainContext, _Mapping]] = ..., vendor_context: _Optional[_Union[_operation_params_pb2.VendorSignatureContext, _Mapping]] = ..., hash_algorithm: _Optional[_Union[_algorithm_params_pb2.HashAlgorithm, str]] = ..., hash_algorithm_oid: _Optional[str] = ..., user_context: _Optional[_Mapping[str, str]] = ...) -> None: ...

class DigestVerifyResponse(_message.Message):
    __slots__ = ("valid", "metadata")
    VALID_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    valid: bool
    metadata: _metadata_pb2.OperationMetadata
    def __init__(self, valid: _Optional[bool] = ..., metadata: _Optional[_Union[_metadata_pb2.OperationMetadata, _Mapping]] = ...) -> None: ...

class SignInitRequest(_message.Message):
    __slots__ = ("key_name", "no_context", "domain_context", "vendor_context", "user_context")
    class UserContextEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    KEY_NAME_FIELD_NUMBER: _ClassVar[int]
    NO_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    VENDOR_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    USER_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    key_name: str
    no_context: _operation_params_pb2.NoParams
    domain_context: _operation_params_pb2.SignatureDomainContext
    vendor_context: _operation_params_pb2.VendorSignatureContext
    user_context: _containers.ScalarMap[str, str]
    def __init__(self, key_name: _Optional[str] = ..., no_context: _Optional[_Union[_operation_params_pb2.NoParams, _Mapping]] = ..., domain_context: _Optional[_Union[_operation_params_pb2.SignatureDomainContext, _Mapping]] = ..., vendor_context: _Optional[_Union[_operation_params_pb2.VendorSignatureContext, _Mapping]] = ..., user_context: _Optional[_Mapping[str, str]] = ...) -> None: ...

class SignInitResponse(_message.Message):
    __slots__ = ("success", "operation_id")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    OPERATION_ID_FIELD_NUMBER: _ClassVar[int]
    success: bool
    operation_id: str
    def __init__(self, success: _Optional[bool] = ..., operation_id: _Optional[str] = ...) -> None: ...

class SignUpdateRequest(_message.Message):
    __slots__ = ("operation_id", "data_chunk")
    OPERATION_ID_FIELD_NUMBER: _ClassVar[int]
    DATA_CHUNK_FIELD_NUMBER: _ClassVar[int]
    operation_id: str
    data_chunk: bytes
    def __init__(self, operation_id: _Optional[str] = ..., data_chunk: _Optional[bytes] = ...) -> None: ...

class SignUpdateResponse(_message.Message):
    __slots__ = ("success",)
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    success: bool
    def __init__(self, success: _Optional[bool] = ...) -> None: ...

class SignFinalRequest(_message.Message):
    __slots__ = ("operation_id",)
    OPERATION_ID_FIELD_NUMBER: _ClassVar[int]
    operation_id: str
    def __init__(self, operation_id: _Optional[str] = ...) -> None: ...

class SignFinalResponse(_message.Message):
    __slots__ = ("signature", "metadata")
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    signature: bytes
    metadata: _metadata_pb2.OperationMetadata
    def __init__(self, signature: _Optional[bytes] = ..., metadata: _Optional[_Union[_metadata_pb2.OperationMetadata, _Mapping]] = ...) -> None: ...

class VerifyInitRequest(_message.Message):
    __slots__ = ("key_name", "no_context", "domain_context", "vendor_context", "metadata", "user_context")
    class UserContextEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    KEY_NAME_FIELD_NUMBER: _ClassVar[int]
    NO_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    VENDOR_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    USER_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    key_name: str
    no_context: _operation_params_pb2.NoParams
    domain_context: _operation_params_pb2.SignatureDomainContext
    vendor_context: _operation_params_pb2.VendorSignatureContext
    metadata: _metadata_pb2.OperationMetadata
    user_context: _containers.ScalarMap[str, str]
    def __init__(self, key_name: _Optional[str] = ..., no_context: _Optional[_Union[_operation_params_pb2.NoParams, _Mapping]] = ..., domain_context: _Optional[_Union[_operation_params_pb2.SignatureDomainContext, _Mapping]] = ..., vendor_context: _Optional[_Union[_operation_params_pb2.VendorSignatureContext, _Mapping]] = ..., metadata: _Optional[_Union[_metadata_pb2.OperationMetadata, _Mapping]] = ..., user_context: _Optional[_Mapping[str, str]] = ...) -> None: ...

class VerifyInitResponse(_message.Message):
    __slots__ = ("success", "operation_id")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    OPERATION_ID_FIELD_NUMBER: _ClassVar[int]
    success: bool
    operation_id: str
    def __init__(self, success: _Optional[bool] = ..., operation_id: _Optional[str] = ...) -> None: ...

class VerifyUpdateRequest(_message.Message):
    __slots__ = ("operation_id", "data_chunk")
    OPERATION_ID_FIELD_NUMBER: _ClassVar[int]
    DATA_CHUNK_FIELD_NUMBER: _ClassVar[int]
    operation_id: str
    data_chunk: bytes
    def __init__(self, operation_id: _Optional[str] = ..., data_chunk: _Optional[bytes] = ...) -> None: ...

class VerifyUpdateResponse(_message.Message):
    __slots__ = ("success",)
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    success: bool
    def __init__(self, success: _Optional[bool] = ...) -> None: ...

class VerifyFinalRequest(_message.Message):
    __slots__ = ("operation_id", "signature")
    OPERATION_ID_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    operation_id: str
    signature: bytes
    def __init__(self, operation_id: _Optional[str] = ..., signature: _Optional[bytes] = ...) -> None: ...

class VerifyFinalResponse(_message.Message):
    __slots__ = ("valid", "metadata")
    VALID_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    valid: bool
    metadata: _metadata_pb2.OperationMetadata
    def __init__(self, valid: _Optional[bool] = ..., metadata: _Optional[_Union[_metadata_pb2.OperationMetadata, _Mapping]] = ...) -> None: ...

class SignMessageInitRequest(_message.Message):
    __slots__ = ("key_name", "no_context", "domain_context", "vendor_context", "user_context")
    class UserContextEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    KEY_NAME_FIELD_NUMBER: _ClassVar[int]
    NO_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    VENDOR_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    USER_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    key_name: str
    no_context: _operation_params_pb2.NoParams
    domain_context: _operation_params_pb2.SignatureDomainContext
    vendor_context: _operation_params_pb2.VendorSignatureContext
    user_context: _containers.ScalarMap[str, str]
    def __init__(self, key_name: _Optional[str] = ..., no_context: _Optional[_Union[_operation_params_pb2.NoParams, _Mapping]] = ..., domain_context: _Optional[_Union[_operation_params_pb2.SignatureDomainContext, _Mapping]] = ..., vendor_context: _Optional[_Union[_operation_params_pb2.VendorSignatureContext, _Mapping]] = ..., user_context: _Optional[_Mapping[str, str]] = ...) -> None: ...

class SignMessageInitResponse(_message.Message):
    __slots__ = ("success", "operation_id")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    OPERATION_ID_FIELD_NUMBER: _ClassVar[int]
    success: bool
    operation_id: str
    def __init__(self, success: _Optional[bool] = ..., operation_id: _Optional[str] = ...) -> None: ...

class SignMessageRequest(_message.Message):
    __slots__ = ("key_name", "message", "operation_id", "user_context")
    class UserContextEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    KEY_NAME_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    OPERATION_ID_FIELD_NUMBER: _ClassVar[int]
    USER_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    key_name: str
    message: bytes
    operation_id: str
    user_context: _containers.ScalarMap[str, str]
    def __init__(self, key_name: _Optional[str] = ..., message: _Optional[bytes] = ..., operation_id: _Optional[str] = ..., user_context: _Optional[_Mapping[str, str]] = ...) -> None: ...

class SignMessageResponse(_message.Message):
    __slots__ = ("signature", "metadata")
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    signature: bytes
    metadata: _metadata_pb2.OperationMetadata
    def __init__(self, signature: _Optional[bytes] = ..., metadata: _Optional[_Union[_metadata_pb2.OperationMetadata, _Mapping]] = ...) -> None: ...

class SignMessageBeginRequest(_message.Message):
    __slots__ = ("operation_id",)
    OPERATION_ID_FIELD_NUMBER: _ClassVar[int]
    operation_id: str
    def __init__(self, operation_id: _Optional[str] = ...) -> None: ...

class SignMessageBeginResponse(_message.Message):
    __slots__ = ("success",)
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    success: bool
    def __init__(self, success: _Optional[bool] = ...) -> None: ...

class SignMessageNextRequest(_message.Message):
    __slots__ = ("operation_id", "message_chunk", "end_of_message")
    OPERATION_ID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_CHUNK_FIELD_NUMBER: _ClassVar[int]
    END_OF_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    operation_id: str
    message_chunk: bytes
    end_of_message: bool
    def __init__(self, operation_id: _Optional[str] = ..., message_chunk: _Optional[bytes] = ..., end_of_message: _Optional[bool] = ...) -> None: ...

class SignMessageNextResponse(_message.Message):
    __slots__ = ("success", "signature", "metadata")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    success: bool
    signature: bytes
    metadata: _metadata_pb2.OperationMetadata
    def __init__(self, success: _Optional[bool] = ..., signature: _Optional[bytes] = ..., metadata: _Optional[_Union[_metadata_pb2.OperationMetadata, _Mapping]] = ...) -> None: ...

class SignMessageFinalRequest(_message.Message):
    __slots__ = ("operation_id",)
    OPERATION_ID_FIELD_NUMBER: _ClassVar[int]
    operation_id: str
    def __init__(self, operation_id: _Optional[str] = ...) -> None: ...

class SignMessageFinalResponse(_message.Message):
    __slots__ = ("success",)
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    success: bool
    def __init__(self, success: _Optional[bool] = ...) -> None: ...

class VerifyMessageInitRequest(_message.Message):
    __slots__ = ("key_name", "no_context", "domain_context", "vendor_context", "user_context")
    class UserContextEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    KEY_NAME_FIELD_NUMBER: _ClassVar[int]
    NO_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    VENDOR_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    USER_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    key_name: str
    no_context: _operation_params_pb2.NoParams
    domain_context: _operation_params_pb2.SignatureDomainContext
    vendor_context: _operation_params_pb2.VendorSignatureContext
    user_context: _containers.ScalarMap[str, str]
    def __init__(self, key_name: _Optional[str] = ..., no_context: _Optional[_Union[_operation_params_pb2.NoParams, _Mapping]] = ..., domain_context: _Optional[_Union[_operation_params_pb2.SignatureDomainContext, _Mapping]] = ..., vendor_context: _Optional[_Union[_operation_params_pb2.VendorSignatureContext, _Mapping]] = ..., user_context: _Optional[_Mapping[str, str]] = ...) -> None: ...

class VerifyMessageInitResponse(_message.Message):
    __slots__ = ("success", "operation_id")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    OPERATION_ID_FIELD_NUMBER: _ClassVar[int]
    success: bool
    operation_id: str
    def __init__(self, success: _Optional[bool] = ..., operation_id: _Optional[str] = ...) -> None: ...

class VerifyMessageRequest(_message.Message):
    __slots__ = ("key_name", "message", "signature", "metadata", "operation_id", "user_context")
    class UserContextEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    KEY_NAME_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    OPERATION_ID_FIELD_NUMBER: _ClassVar[int]
    USER_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    key_name: str
    message: bytes
    signature: bytes
    metadata: _metadata_pb2.OperationMetadata
    operation_id: str
    user_context: _containers.ScalarMap[str, str]
    def __init__(self, key_name: _Optional[str] = ..., message: _Optional[bytes] = ..., signature: _Optional[bytes] = ..., metadata: _Optional[_Union[_metadata_pb2.OperationMetadata, _Mapping]] = ..., operation_id: _Optional[str] = ..., user_context: _Optional[_Mapping[str, str]] = ...) -> None: ...

class VerifyMessageResponse(_message.Message):
    __slots__ = ("valid", "metadata")
    VALID_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    valid: bool
    metadata: _metadata_pb2.OperationMetadata
    def __init__(self, valid: _Optional[bool] = ..., metadata: _Optional[_Union[_metadata_pb2.OperationMetadata, _Mapping]] = ...) -> None: ...

class VerifyMessageBeginRequest(_message.Message):
    __slots__ = ("operation_id",)
    OPERATION_ID_FIELD_NUMBER: _ClassVar[int]
    operation_id: str
    def __init__(self, operation_id: _Optional[str] = ...) -> None: ...

class VerifyMessageBeginResponse(_message.Message):
    __slots__ = ("success",)
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    success: bool
    def __init__(self, success: _Optional[bool] = ...) -> None: ...

class VerifyMessageNextRequest(_message.Message):
    __slots__ = ("operation_id", "message_chunk", "end_of_message", "signature")
    OPERATION_ID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_CHUNK_FIELD_NUMBER: _ClassVar[int]
    END_OF_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    operation_id: str
    message_chunk: bytes
    end_of_message: bool
    signature: bytes
    def __init__(self, operation_id: _Optional[str] = ..., message_chunk: _Optional[bytes] = ..., end_of_message: _Optional[bool] = ..., signature: _Optional[bytes] = ...) -> None: ...

class VerifyMessageNextResponse(_message.Message):
    __slots__ = ("success", "valid", "metadata")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    VALID_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    success: bool
    valid: bool
    metadata: _metadata_pb2.OperationMetadata
    def __init__(self, success: _Optional[bool] = ..., valid: _Optional[bool] = ..., metadata: _Optional[_Union[_metadata_pb2.OperationMetadata, _Mapping]] = ...) -> None: ...

class VerifyMessageFinalRequest(_message.Message):
    __slots__ = ("operation_id",)
    OPERATION_ID_FIELD_NUMBER: _ClassVar[int]
    operation_id: str
    def __init__(self, operation_id: _Optional[str] = ...) -> None: ...

class VerifyMessageFinalResponse(_message.Message):
    __slots__ = ("success",)
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    success: bool
    def __init__(self, success: _Optional[bool] = ...) -> None: ...
