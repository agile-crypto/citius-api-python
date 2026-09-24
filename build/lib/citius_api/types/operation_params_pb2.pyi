from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf import any_pb2 as _any_pb2
from citius_api.types import algorithm_params_pb2 as _algorithm_params_pb2
from citius_api.buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HkdfSaltType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    HKDF_SALT_TYPE_UNSPECIFIED: _ClassVar[HkdfSaltType]
    HKDF_SALT_TYPE_DATA: _ClassVar[HkdfSaltType]
    HKDF_SALT_TYPE_NULL: _ClassVar[HkdfSaltType]
    HKDF_SALT_TYPE_KEY: _ClassVar[HkdfSaltType]

class Sp800108DataType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SP800_108_DATA_TYPE_UNSPECIFIED: _ClassVar[Sp800108DataType]
    SP800_108_DATA_TYPE_ITERATION_VARIABLE: _ClassVar[Sp800108DataType]
    SP800_108_DATA_TYPE_COUNTER: _ClassVar[Sp800108DataType]
    SP800_108_DATA_TYPE_DKM_LENGTH: _ClassVar[Sp800108DataType]
    SP800_108_DATA_TYPE_BYTE_ARRAY: _ClassVar[Sp800108DataType]
HKDF_SALT_TYPE_UNSPECIFIED: HkdfSaltType
HKDF_SALT_TYPE_DATA: HkdfSaltType
HKDF_SALT_TYPE_NULL: HkdfSaltType
HKDF_SALT_TYPE_KEY: HkdfSaltType
SP800_108_DATA_TYPE_UNSPECIFIED: Sp800108DataType
SP800_108_DATA_TYPE_ITERATION_VARIABLE: Sp800108DataType
SP800_108_DATA_TYPE_COUNTER: Sp800108DataType
SP800_108_DATA_TYPE_DKM_LENGTH: Sp800108DataType
SP800_108_DATA_TYPE_BYTE_ARRAY: Sp800108DataType

class NoParams(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AeadEncryptParams(_message.Message):
    __slots__ = ("aad", "plaintext_length")
    AAD_FIELD_NUMBER: _ClassVar[int]
    PLAINTEXT_LENGTH_FIELD_NUMBER: _ClassVar[int]
    aad: bytes
    plaintext_length: int
    def __init__(self, aad: _Optional[bytes] = ..., plaintext_length: _Optional[int] = ...) -> None: ...

class XtsEncryptParams(_message.Message):
    __slots__ = ("tweak",)
    TWEAK_FIELD_NUMBER: _ClassVar[int]
    tweak: bytes
    def __init__(self, tweak: _Optional[bytes] = ...) -> None: ...

class AsymmetricEncryptParams(_message.Message):
    __slots__ = ("label",)
    LABEL_FIELD_NUMBER: _ClassVar[int]
    label: bytes
    def __init__(self, label: _Optional[bytes] = ...) -> None: ...

class SignatureDomainContext(_message.Message):
    __slots__ = ("context",)
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    context: bytes
    def __init__(self, context: _Optional[bytes] = ...) -> None: ...

class HkdfOperationParams(_message.Message):
    __slots__ = ("salt", "info", "salt_type", "salt_key_name")
    SALT_FIELD_NUMBER: _ClassVar[int]
    INFO_FIELD_NUMBER: _ClassVar[int]
    SALT_TYPE_FIELD_NUMBER: _ClassVar[int]
    SALT_KEY_NAME_FIELD_NUMBER: _ClassVar[int]
    salt: bytes
    info: bytes
    salt_type: HkdfSaltType
    salt_key_name: str
    def __init__(self, salt: _Optional[bytes] = ..., info: _Optional[bytes] = ..., salt_type: _Optional[_Union[HkdfSaltType, str]] = ..., salt_key_name: _Optional[str] = ...) -> None: ...

class Pbkdf2OperationParams(_message.Message):
    __slots__ = ("password", "salt")
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    SALT_FIELD_NUMBER: _ClassVar[int]
    password: bytes
    salt: bytes
    def __init__(self, password: _Optional[bytes] = ..., salt: _Optional[bytes] = ...) -> None: ...

class Argon2OperationParams(_message.Message):
    __slots__ = ("password", "salt", "associated_data", "secret")
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    SALT_FIELD_NUMBER: _ClassVar[int]
    ASSOCIATED_DATA_FIELD_NUMBER: _ClassVar[int]
    SECRET_FIELD_NUMBER: _ClassVar[int]
    password: bytes
    salt: bytes
    associated_data: bytes
    secret: bytes
    def __init__(self, password: _Optional[bytes] = ..., salt: _Optional[bytes] = ..., associated_data: _Optional[bytes] = ..., secret: _Optional[bytes] = ...) -> None: ...

class EcdhOperationParams(_message.Message):
    __slots__ = ("shared_info",)
    SHARED_INFO_FIELD_NUMBER: _ClassVar[int]
    shared_info: bytes
    def __init__(self, shared_info: _Optional[bytes] = ...) -> None: ...

class X942DhOperationParams(_message.Message):
    __slots__ = ("other_info",)
    OTHER_INFO_FIELD_NUMBER: _ClassVar[int]
    other_info: bytes
    def __init__(self, other_info: _Optional[bytes] = ...) -> None: ...

class TlsPrfOperationParams(_message.Message):
    __slots__ = ("label", "seed")
    LABEL_FIELD_NUMBER: _ClassVar[int]
    SEED_FIELD_NUMBER: _ClassVar[int]
    label: bytes
    seed: bytes
    def __init__(self, label: _Optional[bytes] = ..., seed: _Optional[bytes] = ...) -> None: ...

class Tls12KdfOperationParams(_message.Message):
    __slots__ = ("label", "client_random", "server_random", "context_data")
    LABEL_FIELD_NUMBER: _ClassVar[int]
    CLIENT_RANDOM_FIELD_NUMBER: _ClassVar[int]
    SERVER_RANDOM_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_DATA_FIELD_NUMBER: _ClassVar[int]
    label: bytes
    client_random: bytes
    server_random: bytes
    context_data: bytes
    def __init__(self, label: _Optional[bytes] = ..., client_random: _Optional[bytes] = ..., server_random: _Optional[bytes] = ..., context_data: _Optional[bytes] = ...) -> None: ...

class Sp800108OperationParams(_message.Message):
    __slots__ = ("data_params",)
    DATA_PARAMS_FIELD_NUMBER: _ClassVar[int]
    data_params: _containers.RepeatedCompositeFieldContainer[Sp800108DataParam]
    def __init__(self, data_params: _Optional[_Iterable[_Union[Sp800108DataParam, _Mapping]]] = ...) -> None: ...

class Sp800108DataParam(_message.Message):
    __slots__ = ("type", "value")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    type: Sp800108DataType
    value: bytes
    def __init__(self, type: _Optional[_Union[Sp800108DataType, str]] = ..., value: _Optional[bytes] = ...) -> None: ...

class GostKdfOperationParams(_message.Message):
    __slots__ = ("ukm",)
    UKM_FIELD_NUMBER: _ClassVar[int]
    ukm: bytes
    def __init__(self, ukm: _Optional[bytes] = ...) -> None: ...

class X3dhOperationParams(_message.Message):
    __slots__ = ("context",)
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    context: bytes
    def __init__(self, context: _Optional[bytes] = ...) -> None: ...

class KeyAgreementWrapParams(_message.Message):
    __slots__ = ("shared_info", "apu", "apv")
    SHARED_INFO_FIELD_NUMBER: _ClassVar[int]
    APU_FIELD_NUMBER: _ClassVar[int]
    APV_FIELD_NUMBER: _ClassVar[int]
    shared_info: bytes
    apu: bytes
    apv: bytes
    def __init__(self, shared_info: _Optional[bytes] = ..., apu: _Optional[bytes] = ..., apv: _Optional[bytes] = ...) -> None: ...

class GostWrapOperationParams(_message.Message):
    __slots__ = ("ukm",)
    UKM_FIELD_NUMBER: _ClassVar[int]
    ukm: bytes
    def __init__(self, ukm: _Optional[bytes] = ...) -> None: ...

class CustomizableMacParams(_message.Message):
    __slots__ = ("customization",)
    CUSTOMIZATION_FIELD_NUMBER: _ClassVar[int]
    customization: bytes
    def __init__(self, customization: _Optional[bytes] = ...) -> None: ...

class CustomOperationParams(_message.Message):
    __slots__ = ("vendor", "algorithm_name", "generic_params", "typed_params", "raw_params")
    VENDOR_FIELD_NUMBER: _ClassVar[int]
    ALGORITHM_NAME_FIELD_NUMBER: _ClassVar[int]
    GENERIC_PARAMS_FIELD_NUMBER: _ClassVar[int]
    TYPED_PARAMS_FIELD_NUMBER: _ClassVar[int]
    RAW_PARAMS_FIELD_NUMBER: _ClassVar[int]
    vendor: str
    algorithm_name: str
    generic_params: _struct_pb2.Struct
    typed_params: _any_pb2.Any
    raw_params: bytes
    def __init__(self, vendor: _Optional[str] = ..., algorithm_name: _Optional[str] = ..., generic_params: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., typed_params: _Optional[_Union[_any_pb2.Any, _Mapping]] = ..., raw_params: _Optional[bytes] = ...) -> None: ...

class VendorEncryptionParams(_message.Message):
    __slots__ = ("params",)
    PARAMS_FIELD_NUMBER: _ClassVar[int]
    params: CustomOperationParams
    def __init__(self, params: _Optional[_Union[CustomOperationParams, _Mapping]] = ...) -> None: ...

class VendorSignatureContext(_message.Message):
    __slots__ = ("params",)
    PARAMS_FIELD_NUMBER: _ClassVar[int]
    params: CustomOperationParams
    def __init__(self, params: _Optional[_Union[CustomOperationParams, _Mapping]] = ...) -> None: ...

class VendorKdfParams(_message.Message):
    __slots__ = ("params",)
    PARAMS_FIELD_NUMBER: _ClassVar[int]
    params: CustomOperationParams
    def __init__(self, params: _Optional[_Union[CustomOperationParams, _Mapping]] = ...) -> None: ...

class VendorWrapParams(_message.Message):
    __slots__ = ("params",)
    PARAMS_FIELD_NUMBER: _ClassVar[int]
    params: CustomOperationParams
    def __init__(self, params: _Optional[_Union[CustomOperationParams, _Mapping]] = ...) -> None: ...

class VendorMacParams(_message.Message):
    __slots__ = ("params",)
    PARAMS_FIELD_NUMBER: _ClassVar[int]
    params: CustomOperationParams
    def __init__(self, params: _Optional[_Union[CustomOperationParams, _Mapping]] = ...) -> None: ...
