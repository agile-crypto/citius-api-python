from citius_api.buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf import any_pb2 as _any_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HashAlgorithm(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    HASH_ALGORITHM_UNSPECIFIED: _ClassVar[HashAlgorithm]
    HASH_ALGORITHM_SHA256: _ClassVar[HashAlgorithm]
    HASH_ALGORITHM_SHA384: _ClassVar[HashAlgorithm]
    HASH_ALGORITHM_SHA512: _ClassVar[HashAlgorithm]
    HASH_ALGORITHM_SHA512_256: _ClassVar[HashAlgorithm]
    HASH_ALGORITHM_SHA224: _ClassVar[HashAlgorithm]
    HASH_ALGORITHM_SHA512_224: _ClassVar[HashAlgorithm]
    HASH_ALGORITHM_SHA3_256: _ClassVar[HashAlgorithm]
    HASH_ALGORITHM_SHA3_384: _ClassVar[HashAlgorithm]
    HASH_ALGORITHM_SHA3_512: _ClassVar[HashAlgorithm]
    HASH_ALGORITHM_SHA3_224: _ClassVar[HashAlgorithm]
    HASH_ALGORITHM_SHAKE128: _ClassVar[HashAlgorithm]
    HASH_ALGORITHM_SHAKE256: _ClassVar[HashAlgorithm]
    HASH_ALGORITHM_BLAKE2B_256: _ClassVar[HashAlgorithm]
    HASH_ALGORITHM_BLAKE2B_384: _ClassVar[HashAlgorithm]
    HASH_ALGORITHM_BLAKE2B_512: _ClassVar[HashAlgorithm]
    HASH_ALGORITHM_BLAKE2S_256: _ClassVar[HashAlgorithm]
    HASH_ALGORITHM_BLAKE2S_160: _ClassVar[HashAlgorithm]
    HASH_ALGORITHM_BLAKE2S_224: _ClassVar[HashAlgorithm]
    HASH_ALGORITHM_BLAKE3: _ClassVar[HashAlgorithm]
    HASH_ALGORITHM_GOST_R3411_94: _ClassVar[HashAlgorithm]
    HASH_ALGORITHM_GOST_R3411_2012_256: _ClassVar[HashAlgorithm]
    HASH_ALGORITHM_GOST_R3411_2012_512: _ClassVar[HashAlgorithm]
    HASH_ALGORITHM_SHA1: _ClassVar[HashAlgorithm]
    HASH_ALGORITHM_MD5: _ClassVar[HashAlgorithm]
    HASH_ALGORITHM_OTHER: _ClassVar[HashAlgorithm]

class EllipticCurve(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ELLIPTIC_CURVE_UNSPECIFIED: _ClassVar[EllipticCurve]
    ELLIPTIC_CURVE_P256: _ClassVar[EllipticCurve]
    ELLIPTIC_CURVE_P384: _ClassVar[EllipticCurve]
    ELLIPTIC_CURVE_P521: _ClassVar[EllipticCurve]
    ELLIPTIC_CURVE_CURVE25519: _ClassVar[EllipticCurve]
    ELLIPTIC_CURVE_CURVE448: _ClassVar[EllipticCurve]
    ELLIPTIC_CURVE_SECP256K1: _ClassVar[EllipticCurve]
    ELLIPTIC_CURVE_BRAINPOOL_P256R1: _ClassVar[EllipticCurve]
    ELLIPTIC_CURVE_BRAINPOOL_P384R1: _ClassVar[EllipticCurve]
    ELLIPTIC_CURVE_BRAINPOOL_P512R1: _ClassVar[EllipticCurve]
    ELLIPTIC_CURVE_BRAINPOOL_P256T1: _ClassVar[EllipticCurve]
    ELLIPTIC_CURVE_BRAINPOOL_P384T1: _ClassVar[EllipticCurve]
    ELLIPTIC_CURVE_BRAINPOOL_P512T1: _ClassVar[EllipticCurve]
    ELLIPTIC_CURVE_K163: _ClassVar[EllipticCurve]
    ELLIPTIC_CURVE_B163: _ClassVar[EllipticCurve]
    ELLIPTIC_CURVE_K233: _ClassVar[EllipticCurve]
    ELLIPTIC_CURVE_B233: _ClassVar[EllipticCurve]
    ELLIPTIC_CURVE_K283: _ClassVar[EllipticCurve]
    ELLIPTIC_CURVE_B283: _ClassVar[EllipticCurve]
    ELLIPTIC_CURVE_K409: _ClassVar[EllipticCurve]
    ELLIPTIC_CURVE_B409: _ClassVar[EllipticCurve]
    ELLIPTIC_CURVE_K571: _ClassVar[EllipticCurve]
    ELLIPTIC_CURVE_B571: _ClassVar[EllipticCurve]

class PaddingScheme(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PADDING_SCHEME_UNSPECIFIED: _ClassVar[PaddingScheme]
    PADDING_SCHEME_NONE: _ClassVar[PaddingScheme]
    PADDING_SCHEME_PKCS7: _ClassVar[PaddingScheme]
    PADDING_SCHEME_ISO7816: _ClassVar[PaddingScheme]
    PADDING_SCHEME_X923: _ClassVar[PaddingScheme]
    PADDING_SCHEME_ZERO: _ClassVar[PaddingScheme]

class SignatureFormat(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SIGNATURE_FORMAT_UNSPECIFIED: _ClassVar[SignatureFormat]
    SIGNATURE_FORMAT_DER: _ClassVar[SignatureFormat]
    SIGNATURE_FORMAT_IEEE_P1363: _ClassVar[SignatureFormat]
    SIGNATURE_FORMAT_RAW: _ClassVar[SignatureFormat]

class MaskGenerationFunction(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MGF_UNSPECIFIED: _ClassVar[MaskGenerationFunction]
    MGF_MGF1: _ClassVar[MaskGenerationFunction]

class Argon2Variant(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ARGON2_VARIANT_UNSPECIFIED: _ClassVar[Argon2Variant]
    ARGON2_VARIANT_D: _ClassVar[Argon2Variant]
    ARGON2_VARIANT_I: _ClassVar[Argon2Variant]
    ARGON2_VARIANT_ID: _ClassVar[Argon2Variant]

class Ed25519Variant(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ED25519_VARIANT_UNSPECIFIED: _ClassVar[Ed25519Variant]
    ED25519_VARIANT_PURE: _ClassVar[Ed25519Variant]
    ED25519_VARIANT_CTX: _ClassVar[Ed25519Variant]
    ED25519_VARIANT_PH: _ClassVar[Ed25519Variant]

class Ed448Variant(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ED448_VARIANT_UNSPECIFIED: _ClassVar[Ed448Variant]
    ED448_VARIANT_PURE: _ClassVar[Ed448Variant]
    ED448_VARIANT_PH: _ClassVar[Ed448Variant]

class KeyType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    KEY_TYPE_UNSPECIFIED: _ClassVar[KeyType]
    KEY_TYPE_SYMMETRIC: _ClassVar[KeyType]
    KEY_TYPE_RSA: _ClassVar[KeyType]
    KEY_TYPE_EC: _ClassVar[KeyType]
    KEY_TYPE_ED25519: _ClassVar[KeyType]
    KEY_TYPE_ED448: _ClassVar[KeyType]
    KEY_TYPE_X25519: _ClassVar[KeyType]
    KEY_TYPE_X448: _ClassVar[KeyType]
    KEY_TYPE_DSA: _ClassVar[KeyType]
    KEY_TYPE_DH: _ClassVar[KeyType]
    KEY_TYPE_ML_KEM: _ClassVar[KeyType]
    KEY_TYPE_ML_DSA: _ClassVar[KeyType]
    KEY_TYPE_SLH_DSA: _ClassVar[KeyType]
    KEY_TYPE_HYBRID: _ClassVar[KeyType]
    KEY_TYPE_GOST: _ClassVar[KeyType]
    KEY_TYPE_OTP: _ClassVar[KeyType]
    KEY_TYPE_VENDOR: _ClassVar[KeyType]
    KEY_TYPE_PQ_EXPERIMENTAL: _ClassVar[KeyType]
    KEY_TYPE_CUSTOM: _ClassVar[KeyType]

class CryptoPrimitive(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CRYPTO_PRIMITIVE_UNSPECIFIED: _ClassVar[CryptoPrimitive]
    CRYPTO_PRIMITIVE_AE: _ClassVar[CryptoPrimitive]
    CRYPTO_PRIMITIVE_BLOCK_CIPHER: _ClassVar[CryptoPrimitive]
    CRYPTO_PRIMITIVE_STREAM_CIPHER: _ClassVar[CryptoPrimitive]
    CRYPTO_PRIMITIVE_PKE: _ClassVar[CryptoPrimitive]
    CRYPTO_PRIMITIVE_SIGNATURE: _ClassVar[CryptoPrimitive]
    CRYPTO_PRIMITIVE_KEM: _ClassVar[CryptoPrimitive]
    CRYPTO_PRIMITIVE_KEY_AGREE: _ClassVar[CryptoPrimitive]
    CRYPTO_PRIMITIVE_HASH: _ClassVar[CryptoPrimitive]
    CRYPTO_PRIMITIVE_MAC: _ClassVar[CryptoPrimitive]
    CRYPTO_PRIMITIVE_XOF: _ClassVar[CryptoPrimitive]
    CRYPTO_PRIMITIVE_KDF: _ClassVar[CryptoPrimitive]
    CRYPTO_PRIMITIVE_KEY_WRAP: _ClassVar[CryptoPrimitive]
    CRYPTO_PRIMITIVE_OTP: _ClassVar[CryptoPrimitive]
    CRYPTO_PRIMITIVE_DRBG: _ClassVar[CryptoPrimitive]
    CRYPTO_PRIMITIVE_COMBINER: _ClassVar[CryptoPrimitive]
    CRYPTO_PRIMITIVE_OTHER: _ClassVar[CryptoPrimitive]

class MlDsaParameterSet(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ML_DSA_PARAMETER_SET_UNSPECIFIED: _ClassVar[MlDsaParameterSet]
    ML_DSA_44: _ClassVar[MlDsaParameterSet]
    ML_DSA_65: _ClassVar[MlDsaParameterSet]
    ML_DSA_87: _ClassVar[MlDsaParameterSet]

class MlKemParameterSet(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ML_KEM_PARAMETER_SET_UNSPECIFIED: _ClassVar[MlKemParameterSet]
    ML_KEM_512: _ClassVar[MlKemParameterSet]
    ML_KEM_768: _ClassVar[MlKemParameterSet]
    ML_KEM_1024: _ClassVar[MlKemParameterSet]

class SlhDsaHashType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SLH_DSA_HASH_TYPE_UNSPECIFIED: _ClassVar[SlhDsaHashType]
    SLH_DSA_SHA2: _ClassVar[SlhDsaHashType]
    SLH_DSA_SHAKE: _ClassVar[SlhDsaHashType]

class SlhDsaParameterSet(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SLH_DSA_PARAMETER_SET_UNSPECIFIED: _ClassVar[SlhDsaParameterSet]
    SLH_DSA_128S: _ClassVar[SlhDsaParameterSet]
    SLH_DSA_128F: _ClassVar[SlhDsaParameterSet]
    SLH_DSA_192S: _ClassVar[SlhDsaParameterSet]
    SLH_DSA_192F: _ClassVar[SlhDsaParameterSet]
    SLH_DSA_256S: _ClassVar[SlhDsaParameterSet]
    SLH_DSA_256F: _ClassVar[SlhDsaParameterSet]

class EcdhKdfType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ECDH_KDF_UNSPECIFIED: _ClassVar[EcdhKdfType]
    ECDH_KDF_HKDF_SHA256: _ClassVar[EcdhKdfType]
    ECDH_KDF_HKDF_SHA384: _ClassVar[EcdhKdfType]
    ECDH_KDF_HKDF_SHA512: _ClassVar[EcdhKdfType]
    ECDH_KDF_X963_SHA256: _ClassVar[EcdhKdfType]
    ECDH_KDF_X963_SHA384: _ClassVar[EcdhKdfType]
    ECDH_KDF_X963_SHA512: _ClassVar[EcdhKdfType]
HASH_ALGORITHM_UNSPECIFIED: HashAlgorithm
HASH_ALGORITHM_SHA256: HashAlgorithm
HASH_ALGORITHM_SHA384: HashAlgorithm
HASH_ALGORITHM_SHA512: HashAlgorithm
HASH_ALGORITHM_SHA512_256: HashAlgorithm
HASH_ALGORITHM_SHA224: HashAlgorithm
HASH_ALGORITHM_SHA512_224: HashAlgorithm
HASH_ALGORITHM_SHA3_256: HashAlgorithm
HASH_ALGORITHM_SHA3_384: HashAlgorithm
HASH_ALGORITHM_SHA3_512: HashAlgorithm
HASH_ALGORITHM_SHA3_224: HashAlgorithm
HASH_ALGORITHM_SHAKE128: HashAlgorithm
HASH_ALGORITHM_SHAKE256: HashAlgorithm
HASH_ALGORITHM_BLAKE2B_256: HashAlgorithm
HASH_ALGORITHM_BLAKE2B_384: HashAlgorithm
HASH_ALGORITHM_BLAKE2B_512: HashAlgorithm
HASH_ALGORITHM_BLAKE2S_256: HashAlgorithm
HASH_ALGORITHM_BLAKE2S_160: HashAlgorithm
HASH_ALGORITHM_BLAKE2S_224: HashAlgorithm
HASH_ALGORITHM_BLAKE3: HashAlgorithm
HASH_ALGORITHM_GOST_R3411_94: HashAlgorithm
HASH_ALGORITHM_GOST_R3411_2012_256: HashAlgorithm
HASH_ALGORITHM_GOST_R3411_2012_512: HashAlgorithm
HASH_ALGORITHM_SHA1: HashAlgorithm
HASH_ALGORITHM_MD5: HashAlgorithm
HASH_ALGORITHM_OTHER: HashAlgorithm
ELLIPTIC_CURVE_UNSPECIFIED: EllipticCurve
ELLIPTIC_CURVE_P256: EllipticCurve
ELLIPTIC_CURVE_P384: EllipticCurve
ELLIPTIC_CURVE_P521: EllipticCurve
ELLIPTIC_CURVE_CURVE25519: EllipticCurve
ELLIPTIC_CURVE_CURVE448: EllipticCurve
ELLIPTIC_CURVE_SECP256K1: EllipticCurve
ELLIPTIC_CURVE_BRAINPOOL_P256R1: EllipticCurve
ELLIPTIC_CURVE_BRAINPOOL_P384R1: EllipticCurve
ELLIPTIC_CURVE_BRAINPOOL_P512R1: EllipticCurve
ELLIPTIC_CURVE_BRAINPOOL_P256T1: EllipticCurve
ELLIPTIC_CURVE_BRAINPOOL_P384T1: EllipticCurve
ELLIPTIC_CURVE_BRAINPOOL_P512T1: EllipticCurve
ELLIPTIC_CURVE_K163: EllipticCurve
ELLIPTIC_CURVE_B163: EllipticCurve
ELLIPTIC_CURVE_K233: EllipticCurve
ELLIPTIC_CURVE_B233: EllipticCurve
ELLIPTIC_CURVE_K283: EllipticCurve
ELLIPTIC_CURVE_B283: EllipticCurve
ELLIPTIC_CURVE_K409: EllipticCurve
ELLIPTIC_CURVE_B409: EllipticCurve
ELLIPTIC_CURVE_K571: EllipticCurve
ELLIPTIC_CURVE_B571: EllipticCurve
PADDING_SCHEME_UNSPECIFIED: PaddingScheme
PADDING_SCHEME_NONE: PaddingScheme
PADDING_SCHEME_PKCS7: PaddingScheme
PADDING_SCHEME_ISO7816: PaddingScheme
PADDING_SCHEME_X923: PaddingScheme
PADDING_SCHEME_ZERO: PaddingScheme
SIGNATURE_FORMAT_UNSPECIFIED: SignatureFormat
SIGNATURE_FORMAT_DER: SignatureFormat
SIGNATURE_FORMAT_IEEE_P1363: SignatureFormat
SIGNATURE_FORMAT_RAW: SignatureFormat
MGF_UNSPECIFIED: MaskGenerationFunction
MGF_MGF1: MaskGenerationFunction
ARGON2_VARIANT_UNSPECIFIED: Argon2Variant
ARGON2_VARIANT_D: Argon2Variant
ARGON2_VARIANT_I: Argon2Variant
ARGON2_VARIANT_ID: Argon2Variant
ED25519_VARIANT_UNSPECIFIED: Ed25519Variant
ED25519_VARIANT_PURE: Ed25519Variant
ED25519_VARIANT_CTX: Ed25519Variant
ED25519_VARIANT_PH: Ed25519Variant
ED448_VARIANT_UNSPECIFIED: Ed448Variant
ED448_VARIANT_PURE: Ed448Variant
ED448_VARIANT_PH: Ed448Variant
KEY_TYPE_UNSPECIFIED: KeyType
KEY_TYPE_SYMMETRIC: KeyType
KEY_TYPE_RSA: KeyType
KEY_TYPE_EC: KeyType
KEY_TYPE_ED25519: KeyType
KEY_TYPE_ED448: KeyType
KEY_TYPE_X25519: KeyType
KEY_TYPE_X448: KeyType
KEY_TYPE_DSA: KeyType
KEY_TYPE_DH: KeyType
KEY_TYPE_ML_KEM: KeyType
KEY_TYPE_ML_DSA: KeyType
KEY_TYPE_SLH_DSA: KeyType
KEY_TYPE_HYBRID: KeyType
KEY_TYPE_GOST: KeyType
KEY_TYPE_OTP: KeyType
KEY_TYPE_VENDOR: KeyType
KEY_TYPE_PQ_EXPERIMENTAL: KeyType
KEY_TYPE_CUSTOM: KeyType
CRYPTO_PRIMITIVE_UNSPECIFIED: CryptoPrimitive
CRYPTO_PRIMITIVE_AE: CryptoPrimitive
CRYPTO_PRIMITIVE_BLOCK_CIPHER: CryptoPrimitive
CRYPTO_PRIMITIVE_STREAM_CIPHER: CryptoPrimitive
CRYPTO_PRIMITIVE_PKE: CryptoPrimitive
CRYPTO_PRIMITIVE_SIGNATURE: CryptoPrimitive
CRYPTO_PRIMITIVE_KEM: CryptoPrimitive
CRYPTO_PRIMITIVE_KEY_AGREE: CryptoPrimitive
CRYPTO_PRIMITIVE_HASH: CryptoPrimitive
CRYPTO_PRIMITIVE_MAC: CryptoPrimitive
CRYPTO_PRIMITIVE_XOF: CryptoPrimitive
CRYPTO_PRIMITIVE_KDF: CryptoPrimitive
CRYPTO_PRIMITIVE_KEY_WRAP: CryptoPrimitive
CRYPTO_PRIMITIVE_OTP: CryptoPrimitive
CRYPTO_PRIMITIVE_DRBG: CryptoPrimitive
CRYPTO_PRIMITIVE_COMBINER: CryptoPrimitive
CRYPTO_PRIMITIVE_OTHER: CryptoPrimitive
ML_DSA_PARAMETER_SET_UNSPECIFIED: MlDsaParameterSet
ML_DSA_44: MlDsaParameterSet
ML_DSA_65: MlDsaParameterSet
ML_DSA_87: MlDsaParameterSet
ML_KEM_PARAMETER_SET_UNSPECIFIED: MlKemParameterSet
ML_KEM_512: MlKemParameterSet
ML_KEM_768: MlKemParameterSet
ML_KEM_1024: MlKemParameterSet
SLH_DSA_HASH_TYPE_UNSPECIFIED: SlhDsaHashType
SLH_DSA_SHA2: SlhDsaHashType
SLH_DSA_SHAKE: SlhDsaHashType
SLH_DSA_PARAMETER_SET_UNSPECIFIED: SlhDsaParameterSet
SLH_DSA_128S: SlhDsaParameterSet
SLH_DSA_128F: SlhDsaParameterSet
SLH_DSA_192S: SlhDsaParameterSet
SLH_DSA_192F: SlhDsaParameterSet
SLH_DSA_256S: SlhDsaParameterSet
SLH_DSA_256F: SlhDsaParameterSet
ECDH_KDF_UNSPECIFIED: EcdhKdfType
ECDH_KDF_HKDF_SHA256: EcdhKdfType
ECDH_KDF_HKDF_SHA384: EcdhKdfType
ECDH_KDF_HKDF_SHA512: EcdhKdfType
ECDH_KDF_X963_SHA256: EcdhKdfType
ECDH_KDF_X963_SHA384: EcdhKdfType
ECDH_KDF_X963_SHA512: EcdhKdfType

class AesGcmParams(_message.Message):
    __slots__ = ("key_size_bits", "iv_size_bits", "tag_size_bits")
    KEY_SIZE_BITS_FIELD_NUMBER: _ClassVar[int]
    IV_SIZE_BITS_FIELD_NUMBER: _ClassVar[int]
    TAG_SIZE_BITS_FIELD_NUMBER: _ClassVar[int]
    key_size_bits: int
    iv_size_bits: int
    tag_size_bits: int
    def __init__(self, key_size_bits: _Optional[int] = ..., iv_size_bits: _Optional[int] = ..., tag_size_bits: _Optional[int] = ...) -> None: ...

class AesCbcParams(_message.Message):
    __slots__ = ("key_size_bits", "iv_size_bits", "padding")
    KEY_SIZE_BITS_FIELD_NUMBER: _ClassVar[int]
    IV_SIZE_BITS_FIELD_NUMBER: _ClassVar[int]
    PADDING_FIELD_NUMBER: _ClassVar[int]
    key_size_bits: int
    iv_size_bits: int
    padding: PaddingScheme
    def __init__(self, key_size_bits: _Optional[int] = ..., iv_size_bits: _Optional[int] = ..., padding: _Optional[_Union[PaddingScheme, str]] = ...) -> None: ...

class AesCtrParams(_message.Message):
    __slots__ = ("key_size_bits", "nonce_size_bits", "counter_bits")
    KEY_SIZE_BITS_FIELD_NUMBER: _ClassVar[int]
    NONCE_SIZE_BITS_FIELD_NUMBER: _ClassVar[int]
    COUNTER_BITS_FIELD_NUMBER: _ClassVar[int]
    key_size_bits: int
    nonce_size_bits: int
    counter_bits: int
    def __init__(self, key_size_bits: _Optional[int] = ..., nonce_size_bits: _Optional[int] = ..., counter_bits: _Optional[int] = ...) -> None: ...

class ChaCha20Poly1305Params(_message.Message):
    __slots__ = ("nonce_size_bits", "block_counter_bits", "extended_nonce")
    NONCE_SIZE_BITS_FIELD_NUMBER: _ClassVar[int]
    BLOCK_COUNTER_BITS_FIELD_NUMBER: _ClassVar[int]
    EXTENDED_NONCE_FIELD_NUMBER: _ClassVar[int]
    nonce_size_bits: int
    block_counter_bits: int
    extended_nonce: bool
    def __init__(self, nonce_size_bits: _Optional[int] = ..., block_counter_bits: _Optional[int] = ..., extended_nonce: _Optional[bool] = ...) -> None: ...

class EcdsaParams(_message.Message):
    __slots__ = ("curve", "hash", "signature_format", "deterministic")
    CURVE_FIELD_NUMBER: _ClassVar[int]
    HASH_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_FORMAT_FIELD_NUMBER: _ClassVar[int]
    DETERMINISTIC_FIELD_NUMBER: _ClassVar[int]
    curve: EllipticCurve
    hash: HashAlgorithm
    signature_format: SignatureFormat
    deterministic: bool
    def __init__(self, curve: _Optional[_Union[EllipticCurve, str]] = ..., hash: _Optional[_Union[HashAlgorithm, str]] = ..., signature_format: _Optional[_Union[SignatureFormat, str]] = ..., deterministic: _Optional[bool] = ...) -> None: ...

class Ed25519Params(_message.Message):
    __slots__ = ("variant",)
    VARIANT_FIELD_NUMBER: _ClassVar[int]
    variant: Ed25519Variant
    def __init__(self, variant: _Optional[_Union[Ed25519Variant, str]] = ...) -> None: ...

class Ed448Params(_message.Message):
    __slots__ = ("variant",)
    VARIANT_FIELD_NUMBER: _ClassVar[int]
    variant: Ed448Variant
    def __init__(self, variant: _Optional[_Union[Ed448Variant, str]] = ...) -> None: ...

class RsaPssParams(_message.Message):
    __slots__ = ("key_size_bits", "hash", "mgf", "mgf_hash", "salt_length_mode", "salt_length_bytes")
    class SaltLengthMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SALT_LENGTH_MODE_HASH_LENGTH: _ClassVar[RsaPssParams.SaltLengthMode]
        SALT_LENGTH_MODE_MAX: _ClassVar[RsaPssParams.SaltLengthMode]
        SALT_LENGTH_MODE_EXPLICIT: _ClassVar[RsaPssParams.SaltLengthMode]
    SALT_LENGTH_MODE_HASH_LENGTH: RsaPssParams.SaltLengthMode
    SALT_LENGTH_MODE_MAX: RsaPssParams.SaltLengthMode
    SALT_LENGTH_MODE_EXPLICIT: RsaPssParams.SaltLengthMode
    KEY_SIZE_BITS_FIELD_NUMBER: _ClassVar[int]
    HASH_FIELD_NUMBER: _ClassVar[int]
    MGF_FIELD_NUMBER: _ClassVar[int]
    MGF_HASH_FIELD_NUMBER: _ClassVar[int]
    SALT_LENGTH_MODE_FIELD_NUMBER: _ClassVar[int]
    SALT_LENGTH_BYTES_FIELD_NUMBER: _ClassVar[int]
    key_size_bits: int
    hash: HashAlgorithm
    mgf: MaskGenerationFunction
    mgf_hash: HashAlgorithm
    salt_length_mode: RsaPssParams.SaltLengthMode
    salt_length_bytes: int
    def __init__(self, key_size_bits: _Optional[int] = ..., hash: _Optional[_Union[HashAlgorithm, str]] = ..., mgf: _Optional[_Union[MaskGenerationFunction, str]] = ..., mgf_hash: _Optional[_Union[HashAlgorithm, str]] = ..., salt_length_mode: _Optional[_Union[RsaPssParams.SaltLengthMode, str]] = ..., salt_length_bytes: _Optional[int] = ...) -> None: ...

class RsaPkcs1v15Params(_message.Message):
    __slots__ = ("key_size_bits", "hash")
    KEY_SIZE_BITS_FIELD_NUMBER: _ClassVar[int]
    HASH_FIELD_NUMBER: _ClassVar[int]
    key_size_bits: int
    hash: HashAlgorithm
    def __init__(self, key_size_bits: _Optional[int] = ..., hash: _Optional[_Union[HashAlgorithm, str]] = ...) -> None: ...

class MlDsaParams(_message.Message):
    __slots__ = ("parameter_set", "deterministic")
    PARAMETER_SET_FIELD_NUMBER: _ClassVar[int]
    DETERMINISTIC_FIELD_NUMBER: _ClassVar[int]
    parameter_set: MlDsaParameterSet
    deterministic: bool
    def __init__(self, parameter_set: _Optional[_Union[MlDsaParameterSet, str]] = ..., deterministic: _Optional[bool] = ...) -> None: ...

class SlhDsaParams(_message.Message):
    __slots__ = ("hash_type", "parameter_set", "deterministic")
    HASH_TYPE_FIELD_NUMBER: _ClassVar[int]
    PARAMETER_SET_FIELD_NUMBER: _ClassVar[int]
    DETERMINISTIC_FIELD_NUMBER: _ClassVar[int]
    hash_type: SlhDsaHashType
    parameter_set: SlhDsaParameterSet
    deterministic: bool
    def __init__(self, hash_type: _Optional[_Union[SlhDsaHashType, str]] = ..., parameter_set: _Optional[_Union[SlhDsaParameterSet, str]] = ..., deterministic: _Optional[bool] = ...) -> None: ...

class MlKemParams(_message.Message):
    __slots__ = ("parameter_set",)
    PARAMETER_SET_FIELD_NUMBER: _ClassVar[int]
    parameter_set: MlKemParameterSet
    def __init__(self, parameter_set: _Optional[_Union[MlKemParameterSet, str]] = ...) -> None: ...

class RsaOaepParams(_message.Message):
    __slots__ = ("key_size_bits", "hash", "mgf", "mgf_hash")
    KEY_SIZE_BITS_FIELD_NUMBER: _ClassVar[int]
    HASH_FIELD_NUMBER: _ClassVar[int]
    MGF_FIELD_NUMBER: _ClassVar[int]
    MGF_HASH_FIELD_NUMBER: _ClassVar[int]
    key_size_bits: int
    hash: HashAlgorithm
    mgf: MaskGenerationFunction
    mgf_hash: HashAlgorithm
    def __init__(self, key_size_bits: _Optional[int] = ..., hash: _Optional[_Union[HashAlgorithm, str]] = ..., mgf: _Optional[_Union[MaskGenerationFunction, str]] = ..., mgf_hash: _Optional[_Union[HashAlgorithm, str]] = ...) -> None: ...

class EcdhParams(_message.Message):
    __slots__ = ("curve", "cofactor_mode", "kdf")
    CURVE_FIELD_NUMBER: _ClassVar[int]
    COFACTOR_MODE_FIELD_NUMBER: _ClassVar[int]
    KDF_FIELD_NUMBER: _ClassVar[int]
    curve: EllipticCurve
    cofactor_mode: bool
    kdf: EcdhKdfType
    def __init__(self, curve: _Optional[_Union[EllipticCurve, str]] = ..., cofactor_mode: _Optional[bool] = ..., kdf: _Optional[_Union[EcdhKdfType, str]] = ...) -> None: ...

class X25519Params(_message.Message):
    __slots__ = ("kdf",)
    KDF_FIELD_NUMBER: _ClassVar[int]
    kdf: EcdhKdfType
    def __init__(self, kdf: _Optional[_Union[EcdhKdfType, str]] = ...) -> None: ...

class X448Params(_message.Message):
    __slots__ = ("kdf",)
    KDF_FIELD_NUMBER: _ClassVar[int]
    kdf: EcdhKdfType
    def __init__(self, kdf: _Optional[_Union[EcdhKdfType, str]] = ...) -> None: ...

class HkdfParams(_message.Message):
    __slots__ = ("hash", "extract", "expand", "salt_size_bytes", "output_length")
    HASH_FIELD_NUMBER: _ClassVar[int]
    EXTRACT_FIELD_NUMBER: _ClassVar[int]
    EXPAND_FIELD_NUMBER: _ClassVar[int]
    SALT_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_LENGTH_FIELD_NUMBER: _ClassVar[int]
    hash: HashAlgorithm
    extract: bool
    expand: bool
    salt_size_bytes: int
    output_length: int
    def __init__(self, hash: _Optional[_Union[HashAlgorithm, str]] = ..., extract: _Optional[bool] = ..., expand: _Optional[bool] = ..., salt_size_bytes: _Optional[int] = ..., output_length: _Optional[int] = ...) -> None: ...

class Pbkdf2Params(_message.Message):
    __slots__ = ("hash", "iterations", "salt_size_bytes", "output_length")
    HASH_FIELD_NUMBER: _ClassVar[int]
    ITERATIONS_FIELD_NUMBER: _ClassVar[int]
    SALT_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_LENGTH_FIELD_NUMBER: _ClassVar[int]
    hash: HashAlgorithm
    iterations: int
    salt_size_bytes: int
    output_length: int
    def __init__(self, hash: _Optional[_Union[HashAlgorithm, str]] = ..., iterations: _Optional[int] = ..., salt_size_bytes: _Optional[int] = ..., output_length: _Optional[int] = ...) -> None: ...

class Argon2Params(_message.Message):
    __slots__ = ("variant", "version", "memory_kib", "iterations", "parallelism", "salt_size_bytes", "output_length")
    VARIANT_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    MEMORY_KIB_FIELD_NUMBER: _ClassVar[int]
    ITERATIONS_FIELD_NUMBER: _ClassVar[int]
    PARALLELISM_FIELD_NUMBER: _ClassVar[int]
    SALT_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_LENGTH_FIELD_NUMBER: _ClassVar[int]
    variant: Argon2Variant
    version: int
    memory_kib: int
    iterations: int
    parallelism: int
    salt_size_bytes: int
    output_length: int
    def __init__(self, variant: _Optional[_Union[Argon2Variant, str]] = ..., version: _Optional[int] = ..., memory_kib: _Optional[int] = ..., iterations: _Optional[int] = ..., parallelism: _Optional[int] = ..., salt_size_bytes: _Optional[int] = ..., output_length: _Optional[int] = ...) -> None: ...

class HmacParams(_message.Message):
    __slots__ = ("hash", "truncation_bits")
    HASH_FIELD_NUMBER: _ClassVar[int]
    TRUNCATION_BITS_FIELD_NUMBER: _ClassVar[int]
    hash: HashAlgorithm
    truncation_bits: int
    def __init__(self, hash: _Optional[_Union[HashAlgorithm, str]] = ..., truncation_bits: _Optional[int] = ...) -> None: ...

class KmacParams(_message.Message):
    __slots__ = ("variant", "output_bits", "customization")
    VARIANT_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_BITS_FIELD_NUMBER: _ClassVar[int]
    CUSTOMIZATION_FIELD_NUMBER: _ClassVar[int]
    variant: int
    output_bits: int
    customization: bytes
    def __init__(self, variant: _Optional[int] = ..., output_bits: _Optional[int] = ..., customization: _Optional[bytes] = ...) -> None: ...

class AesKeyWrapParams(_message.Message):
    __slots__ = ("key_size_bits", "with_padding")
    KEY_SIZE_BITS_FIELD_NUMBER: _ClassVar[int]
    WITH_PADDING_FIELD_NUMBER: _ClassVar[int]
    key_size_bits: int
    with_padding: bool
    def __init__(self, key_size_bits: _Optional[int] = ..., with_padding: _Optional[bool] = ...) -> None: ...

class TripleDesParams(_message.Message):
    __slots__ = ("keying_option", "mode", "iv_size_bits", "padding")
    class KeyingOption(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        KEYING_OPTION_UNSPECIFIED: _ClassVar[TripleDesParams.KeyingOption]
        TWO_KEY: _ClassVar[TripleDesParams.KeyingOption]
        THREE_KEY: _ClassVar[TripleDesParams.KeyingOption]
    KEYING_OPTION_UNSPECIFIED: TripleDesParams.KeyingOption
    TWO_KEY: TripleDesParams.KeyingOption
    THREE_KEY: TripleDesParams.KeyingOption
    class Mode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        MODE_UNSPECIFIED: _ClassVar[TripleDesParams.Mode]
        ECB: _ClassVar[TripleDesParams.Mode]
        CBC: _ClassVar[TripleDesParams.Mode]
    MODE_UNSPECIFIED: TripleDesParams.Mode
    ECB: TripleDesParams.Mode
    CBC: TripleDesParams.Mode
    KEYING_OPTION_FIELD_NUMBER: _ClassVar[int]
    MODE_FIELD_NUMBER: _ClassVar[int]
    IV_SIZE_BITS_FIELD_NUMBER: _ClassVar[int]
    PADDING_FIELD_NUMBER: _ClassVar[int]
    keying_option: TripleDesParams.KeyingOption
    mode: TripleDesParams.Mode
    iv_size_bits: int
    padding: PaddingScheme
    def __init__(self, keying_option: _Optional[_Union[TripleDesParams.KeyingOption, str]] = ..., mode: _Optional[_Union[TripleDesParams.Mode, str]] = ..., iv_size_bits: _Optional[int] = ..., padding: _Optional[_Union[PaddingScheme, str]] = ...) -> None: ...

class DsaParams(_message.Message):
    __slots__ = ("modulus_bits", "subprime_bits", "hash")
    MODULUS_BITS_FIELD_NUMBER: _ClassVar[int]
    SUBPRIME_BITS_FIELD_NUMBER: _ClassVar[int]
    HASH_FIELD_NUMBER: _ClassVar[int]
    modulus_bits: int
    subprime_bits: int
    hash: HashAlgorithm
    def __init__(self, modulus_bits: _Optional[int] = ..., subprime_bits: _Optional[int] = ..., hash: _Optional[_Union[HashAlgorithm, str]] = ...) -> None: ...

class DiffieHellmanParams(_message.Message):
    __slots__ = ("variant", "prime_bits", "kdf", "private_value_length_bits")
    class Variant(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        VARIANT_UNSPECIFIED: _ClassVar[DiffieHellmanParams.Variant]
        PKCS3: _ClassVar[DiffieHellmanParams.Variant]
        X942: _ClassVar[DiffieHellmanParams.Variant]
        X942_MQV: _ClassVar[DiffieHellmanParams.Variant]
    VARIANT_UNSPECIFIED: DiffieHellmanParams.Variant
    PKCS3: DiffieHellmanParams.Variant
    X942: DiffieHellmanParams.Variant
    X942_MQV: DiffieHellmanParams.Variant
    class KdfType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        KDF_UNSPECIFIED: _ClassVar[DiffieHellmanParams.KdfType]
        KDF_NULL: _ClassVar[DiffieHellmanParams.KdfType]
        KDF_SHA1_CONCATENATE: _ClassVar[DiffieHellmanParams.KdfType]
        KDF_SHA256_SP800: _ClassVar[DiffieHellmanParams.KdfType]
        KDF_SHA384_SP800: _ClassVar[DiffieHellmanParams.KdfType]
        KDF_SHA512_SP800: _ClassVar[DiffieHellmanParams.KdfType]
    KDF_UNSPECIFIED: DiffieHellmanParams.KdfType
    KDF_NULL: DiffieHellmanParams.KdfType
    KDF_SHA1_CONCATENATE: DiffieHellmanParams.KdfType
    KDF_SHA256_SP800: DiffieHellmanParams.KdfType
    KDF_SHA384_SP800: DiffieHellmanParams.KdfType
    KDF_SHA512_SP800: DiffieHellmanParams.KdfType
    VARIANT_FIELD_NUMBER: _ClassVar[int]
    PRIME_BITS_FIELD_NUMBER: _ClassVar[int]
    KDF_FIELD_NUMBER: _ClassVar[int]
    PRIVATE_VALUE_LENGTH_BITS_FIELD_NUMBER: _ClassVar[int]
    variant: DiffieHellmanParams.Variant
    prime_bits: int
    kdf: DiffieHellmanParams.KdfType
    private_value_length_bits: int
    def __init__(self, variant: _Optional[_Union[DiffieHellmanParams.Variant, str]] = ..., prime_bits: _Optional[int] = ..., kdf: _Optional[_Union[DiffieHellmanParams.KdfType, str]] = ..., private_value_length_bits: _Optional[int] = ...) -> None: ...

class Sp800108KdfParams(_message.Message):
    __slots__ = ("mode", "prf", "derived_key_length_bytes", "counter_format", "iv_length_bytes")
    class Mode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        MODE_UNSPECIFIED: _ClassVar[Sp800108KdfParams.Mode]
        COUNTER: _ClassVar[Sp800108KdfParams.Mode]
        FEEDBACK: _ClassVar[Sp800108KdfParams.Mode]
        DOUBLE_PIPELINE: _ClassVar[Sp800108KdfParams.Mode]
    MODE_UNSPECIFIED: Sp800108KdfParams.Mode
    COUNTER: Sp800108KdfParams.Mode
    FEEDBACK: Sp800108KdfParams.Mode
    DOUBLE_PIPELINE: Sp800108KdfParams.Mode
    class PrfType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PRF_UNSPECIFIED: _ClassVar[Sp800108KdfParams.PrfType]
        PRF_HMAC_SHA1: _ClassVar[Sp800108KdfParams.PrfType]
        PRF_HMAC_SHA224: _ClassVar[Sp800108KdfParams.PrfType]
        PRF_HMAC_SHA256: _ClassVar[Sp800108KdfParams.PrfType]
        PRF_HMAC_SHA384: _ClassVar[Sp800108KdfParams.PrfType]
        PRF_HMAC_SHA512: _ClassVar[Sp800108KdfParams.PrfType]
        PRF_HMAC_SHA3_224: _ClassVar[Sp800108KdfParams.PrfType]
        PRF_HMAC_SHA3_256: _ClassVar[Sp800108KdfParams.PrfType]
        PRF_HMAC_SHA3_384: _ClassVar[Sp800108KdfParams.PrfType]
        PRF_HMAC_SHA3_512: _ClassVar[Sp800108KdfParams.PrfType]
        PRF_AES_CMAC: _ClassVar[Sp800108KdfParams.PrfType]
        PRF_DES3_CMAC: _ClassVar[Sp800108KdfParams.PrfType]
    PRF_UNSPECIFIED: Sp800108KdfParams.PrfType
    PRF_HMAC_SHA1: Sp800108KdfParams.PrfType
    PRF_HMAC_SHA224: Sp800108KdfParams.PrfType
    PRF_HMAC_SHA256: Sp800108KdfParams.PrfType
    PRF_HMAC_SHA384: Sp800108KdfParams.PrfType
    PRF_HMAC_SHA512: Sp800108KdfParams.PrfType
    PRF_HMAC_SHA3_224: Sp800108KdfParams.PrfType
    PRF_HMAC_SHA3_256: Sp800108KdfParams.PrfType
    PRF_HMAC_SHA3_384: Sp800108KdfParams.PrfType
    PRF_HMAC_SHA3_512: Sp800108KdfParams.PrfType
    PRF_AES_CMAC: Sp800108KdfParams.PrfType
    PRF_DES3_CMAC: Sp800108KdfParams.PrfType
    class CounterFormat(_message.Message):
        __slots__ = ("little_endian", "width_bits")
        LITTLE_ENDIAN_FIELD_NUMBER: _ClassVar[int]
        WIDTH_BITS_FIELD_NUMBER: _ClassVar[int]
        little_endian: bool
        width_bits: int
        def __init__(self, little_endian: _Optional[bool] = ..., width_bits: _Optional[int] = ...) -> None: ...
    MODE_FIELD_NUMBER: _ClassVar[int]
    PRF_FIELD_NUMBER: _ClassVar[int]
    DERIVED_KEY_LENGTH_BYTES_FIELD_NUMBER: _ClassVar[int]
    COUNTER_FORMAT_FIELD_NUMBER: _ClassVar[int]
    IV_LENGTH_BYTES_FIELD_NUMBER: _ClassVar[int]
    mode: Sp800108KdfParams.Mode
    prf: Sp800108KdfParams.PrfType
    derived_key_length_bytes: int
    counter_format: Sp800108KdfParams.CounterFormat
    iv_length_bytes: int
    def __init__(self, mode: _Optional[_Union[Sp800108KdfParams.Mode, str]] = ..., prf: _Optional[_Union[Sp800108KdfParams.PrfType, str]] = ..., derived_key_length_bytes: _Optional[int] = ..., counter_format: _Optional[_Union[Sp800108KdfParams.CounterFormat, _Mapping]] = ..., iv_length_bytes: _Optional[int] = ...) -> None: ...

class Tls12Params(_message.Message):
    __slots__ = ("operation", "prf_hash", "random_info", "key_material")
    class Operation(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        OPERATION_UNSPECIFIED: _ClassVar[Tls12Params.Operation]
        MASTER_KEY_DERIVE: _ClassVar[Tls12Params.Operation]
        KEY_AND_MAC_DERIVE: _ClassVar[Tls12Params.Operation]
        KDF: _ClassVar[Tls12Params.Operation]
        MAC: _ClassVar[Tls12Params.Operation]
    OPERATION_UNSPECIFIED: Tls12Params.Operation
    MASTER_KEY_DERIVE: Tls12Params.Operation
    KEY_AND_MAC_DERIVE: Tls12Params.Operation
    KDF: Tls12Params.Operation
    MAC: Tls12Params.Operation
    class RandomInfo(_message.Message):
        __slots__ = ("client_random_length", "server_random_length")
        CLIENT_RANDOM_LENGTH_FIELD_NUMBER: _ClassVar[int]
        SERVER_RANDOM_LENGTH_FIELD_NUMBER: _ClassVar[int]
        client_random_length: int
        server_random_length: int
        def __init__(self, client_random_length: _Optional[int] = ..., server_random_length: _Optional[int] = ...) -> None: ...
    class KeyMaterialParams(_message.Message):
        __slots__ = ("mac_size_bits", "key_size_bits", "iv_size_bits")
        MAC_SIZE_BITS_FIELD_NUMBER: _ClassVar[int]
        KEY_SIZE_BITS_FIELD_NUMBER: _ClassVar[int]
        IV_SIZE_BITS_FIELD_NUMBER: _ClassVar[int]
        mac_size_bits: int
        key_size_bits: int
        iv_size_bits: int
        def __init__(self, mac_size_bits: _Optional[int] = ..., key_size_bits: _Optional[int] = ..., iv_size_bits: _Optional[int] = ...) -> None: ...
    OPERATION_FIELD_NUMBER: _ClassVar[int]
    PRF_HASH_FIELD_NUMBER: _ClassVar[int]
    RANDOM_INFO_FIELD_NUMBER: _ClassVar[int]
    KEY_MATERIAL_FIELD_NUMBER: _ClassVar[int]
    operation: Tls12Params.Operation
    prf_hash: HashAlgorithm
    random_info: Tls12Params.RandomInfo
    key_material: Tls12Params.KeyMaterialParams
    def __init__(self, operation: _Optional[_Union[Tls12Params.Operation, str]] = ..., prf_hash: _Optional[_Union[HashAlgorithm, str]] = ..., random_info: _Optional[_Union[Tls12Params.RandomInfo, _Mapping]] = ..., key_material: _Optional[_Union[Tls12Params.KeyMaterialParams, _Mapping]] = ...) -> None: ...

class CmacParams(_message.Message):
    __slots__ = ("cipher", "key_size_bits", "output_bits")
    class BlockCipher(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        BLOCK_CIPHER_UNSPECIFIED: _ClassVar[CmacParams.BlockCipher]
        AES: _ClassVar[CmacParams.BlockCipher]
        DES3: _ClassVar[CmacParams.BlockCipher]
    BLOCK_CIPHER_UNSPECIFIED: CmacParams.BlockCipher
    AES: CmacParams.BlockCipher
    DES3: CmacParams.BlockCipher
    CIPHER_FIELD_NUMBER: _ClassVar[int]
    KEY_SIZE_BITS_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_BITS_FIELD_NUMBER: _ClassVar[int]
    cipher: CmacParams.BlockCipher
    key_size_bits: int
    output_bits: int
    def __init__(self, cipher: _Optional[_Union[CmacParams.BlockCipher, str]] = ..., key_size_bits: _Optional[int] = ..., output_bits: _Optional[int] = ...) -> None: ...

class AesCcmParams(_message.Message):
    __slots__ = ("key_size_bits", "nonce_size_bits", "tag_size_bits")
    KEY_SIZE_BITS_FIELD_NUMBER: _ClassVar[int]
    NONCE_SIZE_BITS_FIELD_NUMBER: _ClassVar[int]
    TAG_SIZE_BITS_FIELD_NUMBER: _ClassVar[int]
    key_size_bits: int
    nonce_size_bits: int
    tag_size_bits: int
    def __init__(self, key_size_bits: _Optional[int] = ..., nonce_size_bits: _Optional[int] = ..., tag_size_bits: _Optional[int] = ...) -> None: ...

class AesXtsParams(_message.Message):
    __slots__ = ("key_size_bits", "tweak_size_bytes", "data_unit_size_bytes")
    KEY_SIZE_BITS_FIELD_NUMBER: _ClassVar[int]
    TWEAK_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    DATA_UNIT_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    key_size_bits: int
    tweak_size_bytes: int
    data_unit_size_bytes: int
    def __init__(self, key_size_bits: _Optional[int] = ..., tweak_size_bytes: _Optional[int] = ..., data_unit_size_bytes: _Optional[int] = ...) -> None: ...

class Poly1305Params(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CamelliaParams(_message.Message):
    __slots__ = ("key_size_bits", "mode", "iv_size_bits", "counter_bits", "padding")
    class Mode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        MODE_UNSPECIFIED: _ClassVar[CamelliaParams.Mode]
        ECB: _ClassVar[CamelliaParams.Mode]
        CBC: _ClassVar[CamelliaParams.Mode]
        CTR: _ClassVar[CamelliaParams.Mode]
    MODE_UNSPECIFIED: CamelliaParams.Mode
    ECB: CamelliaParams.Mode
    CBC: CamelliaParams.Mode
    CTR: CamelliaParams.Mode
    KEY_SIZE_BITS_FIELD_NUMBER: _ClassVar[int]
    MODE_FIELD_NUMBER: _ClassVar[int]
    IV_SIZE_BITS_FIELD_NUMBER: _ClassVar[int]
    COUNTER_BITS_FIELD_NUMBER: _ClassVar[int]
    PADDING_FIELD_NUMBER: _ClassVar[int]
    key_size_bits: int
    mode: CamelliaParams.Mode
    iv_size_bits: int
    counter_bits: int
    padding: PaddingScheme
    def __init__(self, key_size_bits: _Optional[int] = ..., mode: _Optional[_Union[CamelliaParams.Mode, str]] = ..., iv_size_bits: _Optional[int] = ..., counter_bits: _Optional[int] = ..., padding: _Optional[_Union[PaddingScheme, str]] = ...) -> None: ...

class AriaParams(_message.Message):
    __slots__ = ("key_size_bits", "mode", "iv_size_bits", "padding")
    class Mode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        MODE_UNSPECIFIED: _ClassVar[AriaParams.Mode]
        ECB: _ClassVar[AriaParams.Mode]
        CBC: _ClassVar[AriaParams.Mode]
    MODE_UNSPECIFIED: AriaParams.Mode
    ECB: AriaParams.Mode
    CBC: AriaParams.Mode
    KEY_SIZE_BITS_FIELD_NUMBER: _ClassVar[int]
    MODE_FIELD_NUMBER: _ClassVar[int]
    IV_SIZE_BITS_FIELD_NUMBER: _ClassVar[int]
    PADDING_FIELD_NUMBER: _ClassVar[int]
    key_size_bits: int
    mode: AriaParams.Mode
    iv_size_bits: int
    padding: PaddingScheme
    def __init__(self, key_size_bits: _Optional[int] = ..., mode: _Optional[_Union[AriaParams.Mode, str]] = ..., iv_size_bits: _Optional[int] = ..., padding: _Optional[_Union[PaddingScheme, str]] = ...) -> None: ...

class SeedParams(_message.Message):
    __slots__ = ("key_size_bits", "mode", "iv_size_bits", "padding")
    class Mode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        MODE_UNSPECIFIED: _ClassVar[SeedParams.Mode]
        ECB: _ClassVar[SeedParams.Mode]
        CBC: _ClassVar[SeedParams.Mode]
    MODE_UNSPECIFIED: SeedParams.Mode
    ECB: SeedParams.Mode
    CBC: SeedParams.Mode
    KEY_SIZE_BITS_FIELD_NUMBER: _ClassVar[int]
    MODE_FIELD_NUMBER: _ClassVar[int]
    IV_SIZE_BITS_FIELD_NUMBER: _ClassVar[int]
    PADDING_FIELD_NUMBER: _ClassVar[int]
    key_size_bits: int
    mode: SeedParams.Mode
    iv_size_bits: int
    padding: PaddingScheme
    def __init__(self, key_size_bits: _Optional[int] = ..., mode: _Optional[_Union[SeedParams.Mode, str]] = ..., iv_size_bits: _Optional[int] = ..., padding: _Optional[_Union[PaddingScheme, str]] = ...) -> None: ...

class Gost28147Params(_message.Message):
    __slots__ = ("mode", "iv_size_bits", "sbox_oid")
    class Mode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        MODE_UNSPECIFIED: _ClassVar[Gost28147Params.Mode]
        ECB: _ClassVar[Gost28147Params.Mode]
        CBC: _ClassVar[Gost28147Params.Mode]
        CFB: _ClassVar[Gost28147Params.Mode]
    MODE_UNSPECIFIED: Gost28147Params.Mode
    ECB: Gost28147Params.Mode
    CBC: Gost28147Params.Mode
    CFB: Gost28147Params.Mode
    MODE_FIELD_NUMBER: _ClassVar[int]
    IV_SIZE_BITS_FIELD_NUMBER: _ClassVar[int]
    SBOX_OID_FIELD_NUMBER: _ClassVar[int]
    mode: Gost28147Params.Mode
    iv_size_bits: int
    sbox_oid: str
    def __init__(self, mode: _Optional[_Union[Gost28147Params.Mode, str]] = ..., iv_size_bits: _Optional[int] = ..., sbox_oid: _Optional[str] = ...) -> None: ...

class Gost3411Params(_message.Message):
    __slots__ = ("initial_value",)
    INITIAL_VALUE_FIELD_NUMBER: _ClassVar[int]
    initial_value: bytes
    def __init__(self, initial_value: _Optional[bytes] = ...) -> None: ...

class Gost3410Params(_message.Message):
    __slots__ = ("version", "key_size_bits", "parameter_set_oid", "digest_param_set_oid")
    class Version(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        VERSION_UNSPECIFIED: _ClassVar[Gost3410Params.Version]
        GOST_2001: _ClassVar[Gost3410Params.Version]
        GOST_2012: _ClassVar[Gost3410Params.Version]
    VERSION_UNSPECIFIED: Gost3410Params.Version
    GOST_2001: Gost3410Params.Version
    GOST_2012: Gost3410Params.Version
    VERSION_FIELD_NUMBER: _ClassVar[int]
    KEY_SIZE_BITS_FIELD_NUMBER: _ClassVar[int]
    PARAMETER_SET_OID_FIELD_NUMBER: _ClassVar[int]
    DIGEST_PARAM_SET_OID_FIELD_NUMBER: _ClassVar[int]
    version: Gost3410Params.Version
    key_size_bits: int
    parameter_set_oid: str
    digest_param_set_oid: str
    def __init__(self, version: _Optional[_Union[Gost3410Params.Version, str]] = ..., key_size_bits: _Optional[int] = ..., parameter_set_oid: _Optional[str] = ..., digest_param_set_oid: _Optional[str] = ...) -> None: ...

class HotpParams(_message.Message):
    __slots__ = ("hash", "digits", "counter_start")
    HASH_FIELD_NUMBER: _ClassVar[int]
    DIGITS_FIELD_NUMBER: _ClassVar[int]
    COUNTER_START_FIELD_NUMBER: _ClassVar[int]
    hash: HashAlgorithm
    digits: int
    counter_start: int
    def __init__(self, hash: _Optional[_Union[HashAlgorithm, str]] = ..., digits: _Optional[int] = ..., counter_start: _Optional[int] = ...) -> None: ...

class TotpParams(_message.Message):
    __slots__ = ("hash", "digits", "time_step_seconds", "t0")
    HASH_FIELD_NUMBER: _ClassVar[int]
    DIGITS_FIELD_NUMBER: _ClassVar[int]
    TIME_STEP_SECONDS_FIELD_NUMBER: _ClassVar[int]
    T0_FIELD_NUMBER: _ClassVar[int]
    hash: HashAlgorithm
    digits: int
    time_step_seconds: int
    t0: int
    def __init__(self, hash: _Optional[_Union[HashAlgorithm, str]] = ..., digits: _Optional[int] = ..., time_step_seconds: _Optional[int] = ..., t0: _Optional[int] = ...) -> None: ...

class X3dhParams(_message.Message):
    __slots__ = ("role", "kdf")
    class Role(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ROLE_UNSPECIFIED: _ClassVar[X3dhParams.Role]
        INITIATOR: _ClassVar[X3dhParams.Role]
        RESPONDER: _ClassVar[X3dhParams.Role]
    ROLE_UNSPECIFIED: X3dhParams.Role
    INITIATOR: X3dhParams.Role
    RESPONDER: X3dhParams.Role
    class X3dhKdfType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        X3DH_KDF_UNSPECIFIED: _ClassVar[X3dhParams.X3dhKdfType]
        X3DH_KDF_SHA256: _ClassVar[X3dhParams.X3dhKdfType]
        X3DH_KDF_SHA512: _ClassVar[X3dhParams.X3dhKdfType]
        X3DH_KDF_BLAKE2B_256: _ClassVar[X3dhParams.X3dhKdfType]
        X3DH_KDF_BLAKE2B_512: _ClassVar[X3dhParams.X3dhKdfType]
    X3DH_KDF_UNSPECIFIED: X3dhParams.X3dhKdfType
    X3DH_KDF_SHA256: X3dhParams.X3dhKdfType
    X3DH_KDF_SHA512: X3dhParams.X3dhKdfType
    X3DH_KDF_BLAKE2B_256: X3dhParams.X3dhKdfType
    X3DH_KDF_BLAKE2B_512: X3dhParams.X3dhKdfType
    ROLE_FIELD_NUMBER: _ClassVar[int]
    KDF_FIELD_NUMBER: _ClassVar[int]
    role: X3dhParams.Role
    kdf: X3dhParams.X3dhKdfType
    def __init__(self, role: _Optional[_Union[X3dhParams.Role, str]] = ..., kdf: _Optional[_Union[X3dhParams.X3dhKdfType, str]] = ...) -> None: ...

class BlowfishParams(_message.Message):
    __slots__ = ("key_size_bits", "iv_size_bits", "padding")
    KEY_SIZE_BITS_FIELD_NUMBER: _ClassVar[int]
    IV_SIZE_BITS_FIELD_NUMBER: _ClassVar[int]
    PADDING_FIELD_NUMBER: _ClassVar[int]
    key_size_bits: int
    iv_size_bits: int
    padding: PaddingScheme
    def __init__(self, key_size_bits: _Optional[int] = ..., iv_size_bits: _Optional[int] = ..., padding: _Optional[_Union[PaddingScheme, str]] = ...) -> None: ...

class TwofishParams(_message.Message):
    __slots__ = ("key_size_bits", "iv_size_bits", "padding")
    KEY_SIZE_BITS_FIELD_NUMBER: _ClassVar[int]
    IV_SIZE_BITS_FIELD_NUMBER: _ClassVar[int]
    PADDING_FIELD_NUMBER: _ClassVar[int]
    key_size_bits: int
    iv_size_bits: int
    padding: PaddingScheme
    def __init__(self, key_size_bits: _Optional[int] = ..., iv_size_bits: _Optional[int] = ..., padding: _Optional[_Union[PaddingScheme, str]] = ...) -> None: ...

class CustomAlgorithm(_message.Message):
    __slots__ = ("vendor", "name", "key_type", "key_size_bits", "generic_params", "typed_params")
    VENDOR_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    KEY_TYPE_FIELD_NUMBER: _ClassVar[int]
    KEY_SIZE_BITS_FIELD_NUMBER: _ClassVar[int]
    GENERIC_PARAMS_FIELD_NUMBER: _ClassVar[int]
    TYPED_PARAMS_FIELD_NUMBER: _ClassVar[int]
    vendor: str
    name: str
    key_type: KeyType
    key_size_bits: int
    generic_params: _struct_pb2.Struct
    typed_params: _any_pb2.Any
    def __init__(self, vendor: _Optional[str] = ..., name: _Optional[str] = ..., key_type: _Optional[_Union[KeyType, str]] = ..., key_size_bits: _Optional[int] = ..., generic_params: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., typed_params: _Optional[_Union[_any_pb2.Any, _Mapping]] = ...) -> None: ...

class VendorAlgorithmRegistry(_message.Message):
    __slots__ = ("vendor_id", "vendor_name", "algorithms", "version", "description", "support_url")
    class AlgorithmsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: CustomAlgorithm
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[CustomAlgorithm, _Mapping]] = ...) -> None: ...
    VENDOR_ID_FIELD_NUMBER: _ClassVar[int]
    VENDOR_NAME_FIELD_NUMBER: _ClassVar[int]
    ALGORITHMS_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    SUPPORT_URL_FIELD_NUMBER: _ClassVar[int]
    vendor_id: str
    vendor_name: str
    algorithms: _containers.MessageMap[str, CustomAlgorithm]
    version: str
    description: str
    support_url: str
    def __init__(self, vendor_id: _Optional[str] = ..., vendor_name: _Optional[str] = ..., algorithms: _Optional[_Mapping[str, CustomAlgorithm]] = ..., version: _Optional[str] = ..., description: _Optional[str] = ..., support_url: _Optional[str] = ...) -> None: ...
