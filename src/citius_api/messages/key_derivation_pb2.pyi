from citius_api.messages import metadata_pb2 as _metadata_pb2
from citius_api.types import common_pb2 as _common_pb2
from citius_api.messages import key_management_pb2 as _key_management_pb2
from citius_api.types import operation_params_pb2 as _operation_params_pb2
from citius_api.buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DeriveKeyRequest(_message.Message):
    __slots__ = ("base_key_name", "derived_key_name", "policy", "hkdf_params", "pbkdf2_params", "argon2_params", "ecdh_params", "x942_dh_params", "tls_prf_params", "tls12_kdf_params", "sp800_108_params", "gost_kdf_params", "x3dh_params", "vendor_params", "user_context")
    class UserContextEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    BASE_KEY_NAME_FIELD_NUMBER: _ClassVar[int]
    DERIVED_KEY_NAME_FIELD_NUMBER: _ClassVar[int]
    POLICY_FIELD_NUMBER: _ClassVar[int]
    HKDF_PARAMS_FIELD_NUMBER: _ClassVar[int]
    PBKDF2_PARAMS_FIELD_NUMBER: _ClassVar[int]
    ARGON2_PARAMS_FIELD_NUMBER: _ClassVar[int]
    ECDH_PARAMS_FIELD_NUMBER: _ClassVar[int]
    X942_DH_PARAMS_FIELD_NUMBER: _ClassVar[int]
    TLS_PRF_PARAMS_FIELD_NUMBER: _ClassVar[int]
    TLS12_KDF_PARAMS_FIELD_NUMBER: _ClassVar[int]
    SP800_108_PARAMS_FIELD_NUMBER: _ClassVar[int]
    GOST_KDF_PARAMS_FIELD_NUMBER: _ClassVar[int]
    X3DH_PARAMS_FIELD_NUMBER: _ClassVar[int]
    VENDOR_PARAMS_FIELD_NUMBER: _ClassVar[int]
    USER_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    base_key_name: str
    derived_key_name: str
    policy: str
    hkdf_params: _operation_params_pb2.HkdfOperationParams
    pbkdf2_params: _operation_params_pb2.Pbkdf2OperationParams
    argon2_params: _operation_params_pb2.Argon2OperationParams
    ecdh_params: _operation_params_pb2.EcdhOperationParams
    x942_dh_params: _operation_params_pb2.X942DhOperationParams
    tls_prf_params: _operation_params_pb2.TlsPrfOperationParams
    tls12_kdf_params: _operation_params_pb2.Tls12KdfOperationParams
    sp800_108_params: _operation_params_pb2.Sp800108OperationParams
    gost_kdf_params: _operation_params_pb2.GostKdfOperationParams
    x3dh_params: _operation_params_pb2.X3dhOperationParams
    vendor_params: _operation_params_pb2.VendorKdfParams
    user_context: _containers.ScalarMap[str, str]
    def __init__(self, base_key_name: _Optional[str] = ..., derived_key_name: _Optional[str] = ..., policy: _Optional[str] = ..., hkdf_params: _Optional[_Union[_operation_params_pb2.HkdfOperationParams, _Mapping]] = ..., pbkdf2_params: _Optional[_Union[_operation_params_pb2.Pbkdf2OperationParams, _Mapping]] = ..., argon2_params: _Optional[_Union[_operation_params_pb2.Argon2OperationParams, _Mapping]] = ..., ecdh_params: _Optional[_Union[_operation_params_pb2.EcdhOperationParams, _Mapping]] = ..., x942_dh_params: _Optional[_Union[_operation_params_pb2.X942DhOperationParams, _Mapping]] = ..., tls_prf_params: _Optional[_Union[_operation_params_pb2.TlsPrfOperationParams, _Mapping]] = ..., tls12_kdf_params: _Optional[_Union[_operation_params_pb2.Tls12KdfOperationParams, _Mapping]] = ..., sp800_108_params: _Optional[_Union[_operation_params_pb2.Sp800108OperationParams, _Mapping]] = ..., gost_kdf_params: _Optional[_Union[_operation_params_pb2.GostKdfOperationParams, _Mapping]] = ..., x3dh_params: _Optional[_Union[_operation_params_pb2.X3dhOperationParams, _Mapping]] = ..., vendor_params: _Optional[_Union[_operation_params_pb2.VendorKdfParams, _Mapping]] = ..., user_context: _Optional[_Mapping[str, str]] = ...) -> None: ...

class DeriveKeyResponse(_message.Message):
    __slots__ = ("success", "message", "metadata", "key_metadata")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    KEY_METADATA_FIELD_NUMBER: _ClassVar[int]
    success: bool
    message: str
    metadata: _metadata_pb2.OperationMetadata
    key_metadata: _key_management_pb2.KeyMetadata
    def __init__(self, success: _Optional[bool] = ..., message: _Optional[str] = ..., metadata: _Optional[_Union[_metadata_pb2.OperationMetadata, _Mapping]] = ..., key_metadata: _Optional[_Union[_key_management_pb2.KeyMetadata, _Mapping]] = ...) -> None: ...

class KeyAgreementRequest(_message.Message):
    __slots__ = ("private_key_name", "peer_public_key", "shared_secret_name", "shared_secret_template_id", "ecdh_params", "x942_dh_params", "x3dh_params", "vendor_params", "peer_public_key_format", "user_context")
    class UserContextEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    PRIVATE_KEY_NAME_FIELD_NUMBER: _ClassVar[int]
    PEER_PUBLIC_KEY_FIELD_NUMBER: _ClassVar[int]
    SHARED_SECRET_NAME_FIELD_NUMBER: _ClassVar[int]
    SHARED_SECRET_TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    ECDH_PARAMS_FIELD_NUMBER: _ClassVar[int]
    X942_DH_PARAMS_FIELD_NUMBER: _ClassVar[int]
    X3DH_PARAMS_FIELD_NUMBER: _ClassVar[int]
    VENDOR_PARAMS_FIELD_NUMBER: _ClassVar[int]
    PEER_PUBLIC_KEY_FORMAT_FIELD_NUMBER: _ClassVar[int]
    USER_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    private_key_name: str
    peer_public_key: bytes
    shared_secret_name: str
    shared_secret_template_id: str
    ecdh_params: _operation_params_pb2.EcdhOperationParams
    x942_dh_params: _operation_params_pb2.X942DhOperationParams
    x3dh_params: _operation_params_pb2.X3dhOperationParams
    vendor_params: _operation_params_pb2.VendorKdfParams
    peer_public_key_format: _common_pb2.KeyFormat
    user_context: _containers.ScalarMap[str, str]
    def __init__(self, private_key_name: _Optional[str] = ..., peer_public_key: _Optional[bytes] = ..., shared_secret_name: _Optional[str] = ..., shared_secret_template_id: _Optional[str] = ..., ecdh_params: _Optional[_Union[_operation_params_pb2.EcdhOperationParams, _Mapping]] = ..., x942_dh_params: _Optional[_Union[_operation_params_pb2.X942DhOperationParams, _Mapping]] = ..., x3dh_params: _Optional[_Union[_operation_params_pb2.X3dhOperationParams, _Mapping]] = ..., vendor_params: _Optional[_Union[_operation_params_pb2.VendorKdfParams, _Mapping]] = ..., peer_public_key_format: _Optional[_Union[_common_pb2.KeyFormat, str]] = ..., user_context: _Optional[_Mapping[str, str]] = ...) -> None: ...

class KeyAgreementResponse(_message.Message):
    __slots__ = ("success", "message", "metadata", "key_metadata")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    KEY_METADATA_FIELD_NUMBER: _ClassVar[int]
    success: bool
    message: str
    metadata: _metadata_pb2.OperationMetadata
    key_metadata: _key_management_pb2.KeyMetadata
    def __init__(self, success: _Optional[bool] = ..., message: _Optional[str] = ..., metadata: _Optional[_Union[_metadata_pb2.OperationMetadata, _Mapping]] = ..., key_metadata: _Optional[_Union[_key_management_pb2.KeyMetadata, _Mapping]] = ...) -> None: ...
