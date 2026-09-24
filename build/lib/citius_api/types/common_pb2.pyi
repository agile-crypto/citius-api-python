from citius_api.buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SignatureScope(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SIGNATURE_SCOPE_UNSPECIFIED: _ClassVar[SignatureScope]
    SIGNATURE_SCOPE_STANDARD: _ClassVar[SignatureScope]
    SIGNATURE_SCOPE_WITH_CONTEXT: _ClassVar[SignatureScope]
    SIGNATURE_SCOPE_PREHASHED: _ClassVar[SignatureScope]
    SIGNATURE_SCOPE_PREHASHED_WITH_CONTEXT: _ClassVar[SignatureScope]

class AeadScope(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    AEAD_SCOPE_UNSPECIFIED: _ClassVar[AeadScope]
    AEAD_SCOPE_STANDARD: _ClassVar[AeadScope]
    AEAD_SCOPE_DETERMINISTIC: _ClassVar[AeadScope]
    AEAD_SCOPE_STREAMING: _ClassVar[AeadScope]

class MacScope(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MAC_SCOPE_UNSPECIFIED: _ClassVar[MacScope]
    MAC_SCOPE_STANDARD: _ClassVar[MacScope]
    MAC_SCOPE_STREAMING: _ClassVar[MacScope]

class KemScope(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    KEM_SCOPE_UNSPECIFIED: _ClassVar[KemScope]
    KEM_SCOPE_STANDARD: _ClassVar[KemScope]
    KEM_SCOPE_HYBRID: _ClassVar[KemScope]

class KeyAgreementScope(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    KEY_AGREEMENT_SCOPE_UNSPECIFIED: _ClassVar[KeyAgreementScope]
    KEY_AGREEMENT_SCOPE_STANDARD: _ClassVar[KeyAgreementScope]
    KEY_AGREEMENT_SCOPE_HYBRID: _ClassVar[KeyAgreementScope]

class KdfScope(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    KDF_SCOPE_UNSPECIFIED: _ClassVar[KdfScope]
    KDF_SCOPE_EXTRACT_EXPAND: _ClassVar[KdfScope]
    KDF_SCOPE_PASSWORD: _ClassVar[KdfScope]
    KDF_SCOPE_AGREEMENT: _ClassVar[KdfScope]
    KDF_SCOPE_COUNTER: _ClassVar[KdfScope]
    KDF_SCOPE_TLS: _ClassVar[KdfScope]
    KDF_SCOPE_GOST: _ClassVar[KdfScope]
    KDF_SCOPE_VENDOR: _ClassVar[KdfScope]

class HashScope(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    HASH_SCOPE_UNSPECIFIED: _ClassVar[HashScope]
    HASH_SCOPE_STANDARD: _ClassVar[HashScope]
    HASH_SCOPE_XOF: _ClassVar[HashScope]

class KeyWrappingScope(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    KEY_WRAPPING_SCOPE_UNSPECIFIED: _ClassVar[KeyWrappingScope]
    KEY_WRAPPING_SCOPE_STANDARD: _ClassVar[KeyWrappingScope]
    KEY_WRAPPING_SCOPE_WITH_PADDING: _ClassVar[KeyWrappingScope]

class SymmetricCipherScope(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SYMMETRIC_CIPHER_SCOPE_UNSPECIFIED: _ClassVar[SymmetricCipherScope]
    SYMMETRIC_CIPHER_SCOPE_BLOCK: _ClassVar[SymmetricCipherScope]
    SYMMETRIC_CIPHER_SCOPE_STREAM: _ClassVar[SymmetricCipherScope]

class DiskEncryptionScope(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DISK_ENCRYPTION_SCOPE_UNSPECIFIED: _ClassVar[DiskEncryptionScope]
    DISK_ENCRYPTION_SCOPE_STANDARD: _ClassVar[DiskEncryptionScope]

class GenericSecretScope(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    GENERIC_SECRET_SCOPE_UNSPECIFIED: _ClassVar[GenericSecretScope]
    GENERIC_SECRET_SCOPE_STANDARD: _ClassVar[GenericSecretScope]

class AsymmetricEncryptionScope(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ASYMMETRIC_ENCRYPTION_SCOPE_UNSPECIFIED: _ClassVar[AsymmetricEncryptionScope]
    ASYMMETRIC_ENCRYPTION_SCOPE_STANDARD: _ClassVar[AsymmetricEncryptionScope]
    ASYMMETRIC_ENCRYPTION_SCOPE_RAW: _ClassVar[AsymmetricEncryptionScope]

class KeyLifecycleState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    KEY_LIFECYCLE_STATE_UNSPECIFIED: _ClassVar[KeyLifecycleState]
    KEY_LIFECYCLE_STATE_PRE_ACTIVE: _ClassVar[KeyLifecycleState]
    KEY_LIFECYCLE_STATE_ACTIVE: _ClassVar[KeyLifecycleState]
    KEY_LIFECYCLE_STATE_SUSPENDED: _ClassVar[KeyLifecycleState]
    KEY_LIFECYCLE_STATE_DEACTIVATED: _ClassVar[KeyLifecycleState]
    KEY_LIFECYCLE_STATE_COMPROMISED: _ClassVar[KeyLifecycleState]
    KEY_LIFECYCLE_STATE_DESTROYED: _ClassVar[KeyLifecycleState]
    KEY_LIFECYCLE_STATE_DESTROYED_COMPROMISED: _ClassVar[KeyLifecycleState]

class KeyOrigin(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    KEY_ORIGIN_UNSPECIFIED: _ClassVar[KeyOrigin]
    KEY_ORIGIN_GENERATED: _ClassVar[KeyOrigin]
    KEY_ORIGIN_IMPORTED: _ClassVar[KeyOrigin]
    KEY_ORIGIN_DERIVED: _ClassVar[KeyOrigin]
    KEY_ORIGIN_UNWRAPPED: _ClassVar[KeyOrigin]

class NistSecurityLevel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NIST_SECURITY_LEVEL_UNSPECIFIED: _ClassVar[NistSecurityLevel]
    NIST_SECURITY_LEVEL_1: _ClassVar[NistSecurityLevel]
    NIST_SECURITY_LEVEL_2: _ClassVar[NistSecurityLevel]
    NIST_SECURITY_LEVEL_3: _ClassVar[NistSecurityLevel]
    NIST_SECURITY_LEVEL_4: _ClassVar[NistSecurityLevel]
    NIST_SECURITY_LEVEL_5: _ClassVar[NistSecurityLevel]

class NistStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NIST_STATUS_UNSPECIFIED: _ClassVar[NistStatus]
    NIST_STATUS_APPROVED: _ClassVar[NistStatus]
    NIST_STATUS_RECOMMENDED: _ClassVar[NistStatus]
    NIST_STATUS_ACCEPTABLE: _ClassVar[NistStatus]
    NIST_STATUS_DEPRECATED: _ClassVar[NistStatus]
    NIST_STATUS_FORBIDDEN: _ClassVar[NistStatus]

class WrapFormat(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    WRAP_FORMAT_UNSPECIFIED: _ClassVar[WrapFormat]
    WRAP_FORMAT_PKCS8: _ClassVar[WrapFormat]
    WRAP_FORMAT_PKCS1: _ClassVar[WrapFormat]
    WRAP_FORMAT_RAW: _ClassVar[WrapFormat]
    WRAP_FORMAT_SPKI: _ClassVar[WrapFormat]
    WRAP_FORMAT_SEC1: _ClassVar[WrapFormat]

class KeyFormat(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    KEY_FORMAT_UNSPECIFIED: _ClassVar[KeyFormat]
    KEY_FORMAT_RAW: _ClassVar[KeyFormat]
    KEY_FORMAT_WRAPPED: _ClassVar[KeyFormat]
    KEY_FORMAT_PKCS8: _ClassVar[KeyFormat]
    KEY_FORMAT_SPKI: _ClassVar[KeyFormat]
    KEY_FORMAT_JWK: _ClassVar[KeyFormat]
    KEY_FORMAT_PEM: _ClassVar[KeyFormat]
    KEY_FORMAT_SEC1: _ClassVar[KeyFormat]

class CryptoErrorCode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CRYPTO_ERROR_UNSPECIFIED: _ClassVar[CryptoErrorCode]
    CRYPTO_ERROR_KEY_NOT_FOUND: _ClassVar[CryptoErrorCode]
    CRYPTO_ERROR_KEY_EXPIRED: _ClassVar[CryptoErrorCode]
    CRYPTO_ERROR_KEY_VERSION_MISMATCH: _ClassVar[CryptoErrorCode]
    CRYPTO_ERROR_KEY_NOT_EXPORTABLE: _ClassVar[CryptoErrorCode]
    CRYPTO_ERROR_KEY_OPERATION_NOT_ALLOWED: _ClassVar[CryptoErrorCode]
    CRYPTO_ERROR_INVALID_KEY_STATE_TRANSITION: _ClassVar[CryptoErrorCode]
    CRYPTO_ERROR_TEMPLATE_NOT_FOUND: _ClassVar[CryptoErrorCode]
    CRYPTO_ERROR_TEMPLATE_DEPRECATED: _ClassVar[CryptoErrorCode]
    CRYPTO_ERROR_TEMPLATE_FORBIDDEN: _ClassVar[CryptoErrorCode]
    CRYPTO_ERROR_NO_MATCHING_TEMPLATE: _ClassVar[CryptoErrorCode]
    CRYPTO_ERROR_PROVIDER_NOT_FOUND: _ClassVar[CryptoErrorCode]
    CRYPTO_ERROR_PROVIDER_UNAVAILABLE: _ClassVar[CryptoErrorCode]
    CRYPTO_ERROR_PROVIDER_INCOMPATIBLE: _ClassVar[CryptoErrorCode]
    CRYPTO_ERROR_NO_MATCHING_PROVIDER: _ClassVar[CryptoErrorCode]
    CRYPTO_ERROR_POLICY_NOT_FOUND: _ClassVar[CryptoErrorCode]
    CRYPTO_ERROR_POLICY_VIOLATION: _ClassVar[CryptoErrorCode]
    CRYPTO_ERROR_POLICY_VERSION_CONFLICT: _ClassVar[CryptoErrorCode]
    CRYPTO_ERROR_INVALID_OPERATION_STATE: _ClassVar[CryptoErrorCode]
    CRYPTO_ERROR_OPERATION_EXPIRED: _ClassVar[CryptoErrorCode]
    CRYPTO_ERROR_AUTHENTICATION_FAILED: _ClassVar[CryptoErrorCode]
    CRYPTO_ERROR_SIGNATURE_INVALID: _ClassVar[CryptoErrorCode]
    CRYPTO_ERROR_INCOMPATIBLE_PARAMETERS: _ClassVar[CryptoErrorCode]
    CRYPTO_ERROR_MIGRATION_NOT_FEASIBLE: _ClassVar[CryptoErrorCode]
    CRYPTO_ERROR_KEY_NOT_EXTRACTABLE: _ClassVar[CryptoErrorCode]
    CRYPTO_ERROR_INVALID_KEY_MATERIAL: _ClassVar[CryptoErrorCode]
    CRYPTO_ERROR_KEY_SIZE_MISMATCH: _ClassVar[CryptoErrorCode]
    CRYPTO_ERROR_INSUFFICIENT_ENTROPY: _ClassVar[CryptoErrorCode]
    CRYPTO_ERROR_RATE_LIMITED: _ClassVar[CryptoErrorCode]
    CRYPTO_ERROR_CONCURRENT_ACCESS: _ClassVar[CryptoErrorCode]

class CryptoOperation(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CRYPTO_OPERATION_UNSPECIFIED: _ClassVar[CryptoOperation]
    CRYPTO_OPERATION_CREATE_KEY: _ClassVar[CryptoOperation]
    CRYPTO_OPERATION_READ_KEY: _ClassVar[CryptoOperation]
    CRYPTO_OPERATION_DELETE_KEY: _ClassVar[CryptoOperation]
    CRYPTO_OPERATION_ROTATE_KEY: _ClassVar[CryptoOperation]
    CRYPTO_OPERATION_TRANSFORM_KEY: _ClassVar[CryptoOperation]
    CRYPTO_OPERATION_IMPORT_KEY: _ClassVar[CryptoOperation]
    CRYPTO_OPERATION_EXPORT_KEY: _ClassVar[CryptoOperation]
    CRYPTO_OPERATION_UPDATE_KEY_POLICY: _ClassVar[CryptoOperation]
    CRYPTO_OPERATION_MIGRATE_KEY: _ClassVar[CryptoOperation]
    CRYPTO_OPERATION_UPDATE_KEY_STATE: _ClassVar[CryptoOperation]
    CRYPTO_OPERATION_ENCRYPT: _ClassVar[CryptoOperation]
    CRYPTO_OPERATION_DECRYPT: _ClassVar[CryptoOperation]
    CRYPTO_OPERATION_SIGN: _ClassVar[CryptoOperation]
    CRYPTO_OPERATION_VERIFY: _ClassVar[CryptoOperation]
    CRYPTO_OPERATION_DIGEST_SIGN: _ClassVar[CryptoOperation]
    CRYPTO_OPERATION_DIGEST_VERIFY: _ClassVar[CryptoOperation]
    CRYPTO_OPERATION_WRAP_KEY: _ClassVar[CryptoOperation]
    CRYPTO_OPERATION_UNWRAP_KEY: _ClassVar[CryptoOperation]
    CRYPTO_OPERATION_DERIVE_KEY: _ClassVar[CryptoOperation]
    CRYPTO_OPERATION_GENERATE_MAC: _ClassVar[CryptoOperation]
    CRYPTO_OPERATION_VERIFY_MAC: _ClassVar[CryptoOperation]
    CRYPTO_OPERATION_DIGEST: _ClassVar[CryptoOperation]
    CRYPTO_OPERATION_ENCAPSULATE: _ClassVar[CryptoOperation]
    CRYPTO_OPERATION_DECAPSULATE: _ClassVar[CryptoOperation]
    CRYPTO_OPERATION_KEY_AGREEMENT: _ClassVar[CryptoOperation]
    CRYPTO_OPERATION_GENERATE_RANDOM: _ClassVar[CryptoOperation]
    CRYPTO_OPERATION_SEED_RANDOM: _ClassVar[CryptoOperation]
    CRYPTO_OPERATION_DIGEST_ENCRYPT: _ClassVar[CryptoOperation]
    CRYPTO_OPERATION_DECRYPT_DIGEST: _ClassVar[CryptoOperation]
    CRYPTO_OPERATION_SIGN_ENCRYPT: _ClassVar[CryptoOperation]
    CRYPTO_OPERATION_DECRYPT_VERIFY: _ClassVar[CryptoOperation]
SIGNATURE_SCOPE_UNSPECIFIED: SignatureScope
SIGNATURE_SCOPE_STANDARD: SignatureScope
SIGNATURE_SCOPE_WITH_CONTEXT: SignatureScope
SIGNATURE_SCOPE_PREHASHED: SignatureScope
SIGNATURE_SCOPE_PREHASHED_WITH_CONTEXT: SignatureScope
AEAD_SCOPE_UNSPECIFIED: AeadScope
AEAD_SCOPE_STANDARD: AeadScope
AEAD_SCOPE_DETERMINISTIC: AeadScope
AEAD_SCOPE_STREAMING: AeadScope
MAC_SCOPE_UNSPECIFIED: MacScope
MAC_SCOPE_STANDARD: MacScope
MAC_SCOPE_STREAMING: MacScope
KEM_SCOPE_UNSPECIFIED: KemScope
KEM_SCOPE_STANDARD: KemScope
KEM_SCOPE_HYBRID: KemScope
KEY_AGREEMENT_SCOPE_UNSPECIFIED: KeyAgreementScope
KEY_AGREEMENT_SCOPE_STANDARD: KeyAgreementScope
KEY_AGREEMENT_SCOPE_HYBRID: KeyAgreementScope
KDF_SCOPE_UNSPECIFIED: KdfScope
KDF_SCOPE_EXTRACT_EXPAND: KdfScope
KDF_SCOPE_PASSWORD: KdfScope
KDF_SCOPE_AGREEMENT: KdfScope
KDF_SCOPE_COUNTER: KdfScope
KDF_SCOPE_TLS: KdfScope
KDF_SCOPE_GOST: KdfScope
KDF_SCOPE_VENDOR: KdfScope
HASH_SCOPE_UNSPECIFIED: HashScope
HASH_SCOPE_STANDARD: HashScope
HASH_SCOPE_XOF: HashScope
KEY_WRAPPING_SCOPE_UNSPECIFIED: KeyWrappingScope
KEY_WRAPPING_SCOPE_STANDARD: KeyWrappingScope
KEY_WRAPPING_SCOPE_WITH_PADDING: KeyWrappingScope
SYMMETRIC_CIPHER_SCOPE_UNSPECIFIED: SymmetricCipherScope
SYMMETRIC_CIPHER_SCOPE_BLOCK: SymmetricCipherScope
SYMMETRIC_CIPHER_SCOPE_STREAM: SymmetricCipherScope
DISK_ENCRYPTION_SCOPE_UNSPECIFIED: DiskEncryptionScope
DISK_ENCRYPTION_SCOPE_STANDARD: DiskEncryptionScope
GENERIC_SECRET_SCOPE_UNSPECIFIED: GenericSecretScope
GENERIC_SECRET_SCOPE_STANDARD: GenericSecretScope
ASYMMETRIC_ENCRYPTION_SCOPE_UNSPECIFIED: AsymmetricEncryptionScope
ASYMMETRIC_ENCRYPTION_SCOPE_STANDARD: AsymmetricEncryptionScope
ASYMMETRIC_ENCRYPTION_SCOPE_RAW: AsymmetricEncryptionScope
KEY_LIFECYCLE_STATE_UNSPECIFIED: KeyLifecycleState
KEY_LIFECYCLE_STATE_PRE_ACTIVE: KeyLifecycleState
KEY_LIFECYCLE_STATE_ACTIVE: KeyLifecycleState
KEY_LIFECYCLE_STATE_SUSPENDED: KeyLifecycleState
KEY_LIFECYCLE_STATE_DEACTIVATED: KeyLifecycleState
KEY_LIFECYCLE_STATE_COMPROMISED: KeyLifecycleState
KEY_LIFECYCLE_STATE_DESTROYED: KeyLifecycleState
KEY_LIFECYCLE_STATE_DESTROYED_COMPROMISED: KeyLifecycleState
KEY_ORIGIN_UNSPECIFIED: KeyOrigin
KEY_ORIGIN_GENERATED: KeyOrigin
KEY_ORIGIN_IMPORTED: KeyOrigin
KEY_ORIGIN_DERIVED: KeyOrigin
KEY_ORIGIN_UNWRAPPED: KeyOrigin
NIST_SECURITY_LEVEL_UNSPECIFIED: NistSecurityLevel
NIST_SECURITY_LEVEL_1: NistSecurityLevel
NIST_SECURITY_LEVEL_2: NistSecurityLevel
NIST_SECURITY_LEVEL_3: NistSecurityLevel
NIST_SECURITY_LEVEL_4: NistSecurityLevel
NIST_SECURITY_LEVEL_5: NistSecurityLevel
NIST_STATUS_UNSPECIFIED: NistStatus
NIST_STATUS_APPROVED: NistStatus
NIST_STATUS_RECOMMENDED: NistStatus
NIST_STATUS_ACCEPTABLE: NistStatus
NIST_STATUS_DEPRECATED: NistStatus
NIST_STATUS_FORBIDDEN: NistStatus
WRAP_FORMAT_UNSPECIFIED: WrapFormat
WRAP_FORMAT_PKCS8: WrapFormat
WRAP_FORMAT_PKCS1: WrapFormat
WRAP_FORMAT_RAW: WrapFormat
WRAP_FORMAT_SPKI: WrapFormat
WRAP_FORMAT_SEC1: WrapFormat
KEY_FORMAT_UNSPECIFIED: KeyFormat
KEY_FORMAT_RAW: KeyFormat
KEY_FORMAT_WRAPPED: KeyFormat
KEY_FORMAT_PKCS8: KeyFormat
KEY_FORMAT_SPKI: KeyFormat
KEY_FORMAT_JWK: KeyFormat
KEY_FORMAT_PEM: KeyFormat
KEY_FORMAT_SEC1: KeyFormat
CRYPTO_ERROR_UNSPECIFIED: CryptoErrorCode
CRYPTO_ERROR_KEY_NOT_FOUND: CryptoErrorCode
CRYPTO_ERROR_KEY_EXPIRED: CryptoErrorCode
CRYPTO_ERROR_KEY_VERSION_MISMATCH: CryptoErrorCode
CRYPTO_ERROR_KEY_NOT_EXPORTABLE: CryptoErrorCode
CRYPTO_ERROR_KEY_OPERATION_NOT_ALLOWED: CryptoErrorCode
CRYPTO_ERROR_INVALID_KEY_STATE_TRANSITION: CryptoErrorCode
CRYPTO_ERROR_TEMPLATE_NOT_FOUND: CryptoErrorCode
CRYPTO_ERROR_TEMPLATE_DEPRECATED: CryptoErrorCode
CRYPTO_ERROR_TEMPLATE_FORBIDDEN: CryptoErrorCode
CRYPTO_ERROR_NO_MATCHING_TEMPLATE: CryptoErrorCode
CRYPTO_ERROR_PROVIDER_NOT_FOUND: CryptoErrorCode
CRYPTO_ERROR_PROVIDER_UNAVAILABLE: CryptoErrorCode
CRYPTO_ERROR_PROVIDER_INCOMPATIBLE: CryptoErrorCode
CRYPTO_ERROR_NO_MATCHING_PROVIDER: CryptoErrorCode
CRYPTO_ERROR_POLICY_NOT_FOUND: CryptoErrorCode
CRYPTO_ERROR_POLICY_VIOLATION: CryptoErrorCode
CRYPTO_ERROR_POLICY_VERSION_CONFLICT: CryptoErrorCode
CRYPTO_ERROR_INVALID_OPERATION_STATE: CryptoErrorCode
CRYPTO_ERROR_OPERATION_EXPIRED: CryptoErrorCode
CRYPTO_ERROR_AUTHENTICATION_FAILED: CryptoErrorCode
CRYPTO_ERROR_SIGNATURE_INVALID: CryptoErrorCode
CRYPTO_ERROR_INCOMPATIBLE_PARAMETERS: CryptoErrorCode
CRYPTO_ERROR_MIGRATION_NOT_FEASIBLE: CryptoErrorCode
CRYPTO_ERROR_KEY_NOT_EXTRACTABLE: CryptoErrorCode
CRYPTO_ERROR_INVALID_KEY_MATERIAL: CryptoErrorCode
CRYPTO_ERROR_KEY_SIZE_MISMATCH: CryptoErrorCode
CRYPTO_ERROR_INSUFFICIENT_ENTROPY: CryptoErrorCode
CRYPTO_ERROR_RATE_LIMITED: CryptoErrorCode
CRYPTO_ERROR_CONCURRENT_ACCESS: CryptoErrorCode
CRYPTO_OPERATION_UNSPECIFIED: CryptoOperation
CRYPTO_OPERATION_CREATE_KEY: CryptoOperation
CRYPTO_OPERATION_READ_KEY: CryptoOperation
CRYPTO_OPERATION_DELETE_KEY: CryptoOperation
CRYPTO_OPERATION_ROTATE_KEY: CryptoOperation
CRYPTO_OPERATION_TRANSFORM_KEY: CryptoOperation
CRYPTO_OPERATION_IMPORT_KEY: CryptoOperation
CRYPTO_OPERATION_EXPORT_KEY: CryptoOperation
CRYPTO_OPERATION_UPDATE_KEY_POLICY: CryptoOperation
CRYPTO_OPERATION_MIGRATE_KEY: CryptoOperation
CRYPTO_OPERATION_UPDATE_KEY_STATE: CryptoOperation
CRYPTO_OPERATION_ENCRYPT: CryptoOperation
CRYPTO_OPERATION_DECRYPT: CryptoOperation
CRYPTO_OPERATION_SIGN: CryptoOperation
CRYPTO_OPERATION_VERIFY: CryptoOperation
CRYPTO_OPERATION_DIGEST_SIGN: CryptoOperation
CRYPTO_OPERATION_DIGEST_VERIFY: CryptoOperation
CRYPTO_OPERATION_WRAP_KEY: CryptoOperation
CRYPTO_OPERATION_UNWRAP_KEY: CryptoOperation
CRYPTO_OPERATION_DERIVE_KEY: CryptoOperation
CRYPTO_OPERATION_GENERATE_MAC: CryptoOperation
CRYPTO_OPERATION_VERIFY_MAC: CryptoOperation
CRYPTO_OPERATION_DIGEST: CryptoOperation
CRYPTO_OPERATION_ENCAPSULATE: CryptoOperation
CRYPTO_OPERATION_DECAPSULATE: CryptoOperation
CRYPTO_OPERATION_KEY_AGREEMENT: CryptoOperation
CRYPTO_OPERATION_GENERATE_RANDOM: CryptoOperation
CRYPTO_OPERATION_SEED_RANDOM: CryptoOperation
CRYPTO_OPERATION_DIGEST_ENCRYPT: CryptoOperation
CRYPTO_OPERATION_DECRYPT_DIGEST: CryptoOperation
CRYPTO_OPERATION_SIGN_ENCRYPT: CryptoOperation
CRYPTO_OPERATION_DECRYPT_VERIFY: CryptoOperation

class UniversalSecurityProperties(_message.Message):
    __slots__ = ("security_strength_bits", "nist_security_level", "quantum_safe", "nist_status", "fips_approved")
    SECURITY_STRENGTH_BITS_FIELD_NUMBER: _ClassVar[int]
    NIST_SECURITY_LEVEL_FIELD_NUMBER: _ClassVar[int]
    QUANTUM_SAFE_FIELD_NUMBER: _ClassVar[int]
    NIST_STATUS_FIELD_NUMBER: _ClassVar[int]
    FIPS_APPROVED_FIELD_NUMBER: _ClassVar[int]
    security_strength_bits: int
    nist_security_level: NistSecurityLevel
    quantum_safe: bool
    nist_status: NistStatus
    fips_approved: bool
    def __init__(self, security_strength_bits: _Optional[int] = ..., nist_security_level: _Optional[_Union[NistSecurityLevel, str]] = ..., quantum_safe: _Optional[bool] = ..., nist_status: _Optional[_Union[NistStatus, str]] = ..., fips_approved: _Optional[bool] = ...) -> None: ...

class SignatureScopeSpec(_message.Message):
    __slots__ = ("scope", "security", "non_malleable", "deterministic", "additional_properties")
    class AdditionalPropertiesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    SCOPE_FIELD_NUMBER: _ClassVar[int]
    SECURITY_FIELD_NUMBER: _ClassVar[int]
    NON_MALLEABLE_FIELD_NUMBER: _ClassVar[int]
    DETERMINISTIC_FIELD_NUMBER: _ClassVar[int]
    ADDITIONAL_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    scope: SignatureScope
    security: UniversalSecurityProperties
    non_malleable: bool
    deterministic: bool
    additional_properties: _containers.ScalarMap[str, str]
    def __init__(self, scope: _Optional[_Union[SignatureScope, str]] = ..., security: _Optional[_Union[UniversalSecurityProperties, _Mapping]] = ..., non_malleable: _Optional[bool] = ..., deterministic: _Optional[bool] = ..., additional_properties: _Optional[_Mapping[str, str]] = ...) -> None: ...

class AeadScopeSpec(_message.Message):
    __slots__ = ("scope", "security", "nonce_misuse_resistant", "additional_properties")
    class AdditionalPropertiesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    SCOPE_FIELD_NUMBER: _ClassVar[int]
    SECURITY_FIELD_NUMBER: _ClassVar[int]
    NONCE_MISUSE_RESISTANT_FIELD_NUMBER: _ClassVar[int]
    ADDITIONAL_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    scope: AeadScope
    security: UniversalSecurityProperties
    nonce_misuse_resistant: bool
    additional_properties: _containers.ScalarMap[str, str]
    def __init__(self, scope: _Optional[_Union[AeadScope, str]] = ..., security: _Optional[_Union[UniversalSecurityProperties, _Mapping]] = ..., nonce_misuse_resistant: _Optional[bool] = ..., additional_properties: _Optional[_Mapping[str, str]] = ...) -> None: ...

class MacScopeSpec(_message.Message):
    __slots__ = ("scope", "security", "additional_properties")
    class AdditionalPropertiesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    SCOPE_FIELD_NUMBER: _ClassVar[int]
    SECURITY_FIELD_NUMBER: _ClassVar[int]
    ADDITIONAL_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    scope: MacScope
    security: UniversalSecurityProperties
    additional_properties: _containers.ScalarMap[str, str]
    def __init__(self, scope: _Optional[_Union[MacScope, str]] = ..., security: _Optional[_Union[UniversalSecurityProperties, _Mapping]] = ..., additional_properties: _Optional[_Mapping[str, str]] = ...) -> None: ...

class KemScopeSpec(_message.Message):
    __slots__ = ("scope", "security", "additional_properties")
    class AdditionalPropertiesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    SCOPE_FIELD_NUMBER: _ClassVar[int]
    SECURITY_FIELD_NUMBER: _ClassVar[int]
    ADDITIONAL_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    scope: KemScope
    security: UniversalSecurityProperties
    additional_properties: _containers.ScalarMap[str, str]
    def __init__(self, scope: _Optional[_Union[KemScope, str]] = ..., security: _Optional[_Union[UniversalSecurityProperties, _Mapping]] = ..., additional_properties: _Optional[_Mapping[str, str]] = ...) -> None: ...

class KeyAgreementScopeSpec(_message.Message):
    __slots__ = ("scope", "security", "forward_secrecy", "additional_properties")
    class AdditionalPropertiesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    SCOPE_FIELD_NUMBER: _ClassVar[int]
    SECURITY_FIELD_NUMBER: _ClassVar[int]
    FORWARD_SECRECY_FIELD_NUMBER: _ClassVar[int]
    ADDITIONAL_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    scope: KeyAgreementScope
    security: UniversalSecurityProperties
    forward_secrecy: bool
    additional_properties: _containers.ScalarMap[str, str]
    def __init__(self, scope: _Optional[_Union[KeyAgreementScope, str]] = ..., security: _Optional[_Union[UniversalSecurityProperties, _Mapping]] = ..., forward_secrecy: _Optional[bool] = ..., additional_properties: _Optional[_Mapping[str, str]] = ...) -> None: ...

class KdfScopeSpec(_message.Message):
    __slots__ = ("scope", "security", "memory_hard", "additional_properties")
    class AdditionalPropertiesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    SCOPE_FIELD_NUMBER: _ClassVar[int]
    SECURITY_FIELD_NUMBER: _ClassVar[int]
    MEMORY_HARD_FIELD_NUMBER: _ClassVar[int]
    ADDITIONAL_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    scope: KdfScope
    security: UniversalSecurityProperties
    memory_hard: bool
    additional_properties: _containers.ScalarMap[str, str]
    def __init__(self, scope: _Optional[_Union[KdfScope, str]] = ..., security: _Optional[_Union[UniversalSecurityProperties, _Mapping]] = ..., memory_hard: _Optional[bool] = ..., additional_properties: _Optional[_Mapping[str, str]] = ...) -> None: ...

class HashScopeSpec(_message.Message):
    __slots__ = ("scope", "security", "additional_properties")
    class AdditionalPropertiesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    SCOPE_FIELD_NUMBER: _ClassVar[int]
    SECURITY_FIELD_NUMBER: _ClassVar[int]
    ADDITIONAL_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    scope: HashScope
    security: UniversalSecurityProperties
    additional_properties: _containers.ScalarMap[str, str]
    def __init__(self, scope: _Optional[_Union[HashScope, str]] = ..., security: _Optional[_Union[UniversalSecurityProperties, _Mapping]] = ..., additional_properties: _Optional[_Mapping[str, str]] = ...) -> None: ...

class KeyWrappingScopeSpec(_message.Message):
    __slots__ = ("scope", "security", "additional_properties")
    class AdditionalPropertiesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    SCOPE_FIELD_NUMBER: _ClassVar[int]
    SECURITY_FIELD_NUMBER: _ClassVar[int]
    ADDITIONAL_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    scope: KeyWrappingScope
    security: UniversalSecurityProperties
    additional_properties: _containers.ScalarMap[str, str]
    def __init__(self, scope: _Optional[_Union[KeyWrappingScope, str]] = ..., security: _Optional[_Union[UniversalSecurityProperties, _Mapping]] = ..., additional_properties: _Optional[_Mapping[str, str]] = ...) -> None: ...

class SymmetricCipherScopeSpec(_message.Message):
    __slots__ = ("scope", "security", "additional_properties")
    class AdditionalPropertiesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    SCOPE_FIELD_NUMBER: _ClassVar[int]
    SECURITY_FIELD_NUMBER: _ClassVar[int]
    ADDITIONAL_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    scope: SymmetricCipherScope
    security: UniversalSecurityProperties
    additional_properties: _containers.ScalarMap[str, str]
    def __init__(self, scope: _Optional[_Union[SymmetricCipherScope, str]] = ..., security: _Optional[_Union[UniversalSecurityProperties, _Mapping]] = ..., additional_properties: _Optional[_Mapping[str, str]] = ...) -> None: ...

class DiskEncryptionScopeSpec(_message.Message):
    __slots__ = ("scope", "security", "additional_properties")
    class AdditionalPropertiesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    SCOPE_FIELD_NUMBER: _ClassVar[int]
    SECURITY_FIELD_NUMBER: _ClassVar[int]
    ADDITIONAL_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    scope: DiskEncryptionScope
    security: UniversalSecurityProperties
    additional_properties: _containers.ScalarMap[str, str]
    def __init__(self, scope: _Optional[_Union[DiskEncryptionScope, str]] = ..., security: _Optional[_Union[UniversalSecurityProperties, _Mapping]] = ..., additional_properties: _Optional[_Mapping[str, str]] = ...) -> None: ...

class GenericSecretScopeSpec(_message.Message):
    __slots__ = ("scope", "security", "additional_properties")
    class AdditionalPropertiesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    SCOPE_FIELD_NUMBER: _ClassVar[int]
    SECURITY_FIELD_NUMBER: _ClassVar[int]
    ADDITIONAL_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    scope: GenericSecretScope
    security: UniversalSecurityProperties
    additional_properties: _containers.ScalarMap[str, str]
    def __init__(self, scope: _Optional[_Union[GenericSecretScope, str]] = ..., security: _Optional[_Union[UniversalSecurityProperties, _Mapping]] = ..., additional_properties: _Optional[_Mapping[str, str]] = ...) -> None: ...

class AsymmetricEncryptionScopeSpec(_message.Message):
    __slots__ = ("scope", "security", "additional_properties")
    class AdditionalPropertiesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    SCOPE_FIELD_NUMBER: _ClassVar[int]
    SECURITY_FIELD_NUMBER: _ClassVar[int]
    ADDITIONAL_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    scope: AsymmetricEncryptionScope
    security: UniversalSecurityProperties
    additional_properties: _containers.ScalarMap[str, str]
    def __init__(self, scope: _Optional[_Union[AsymmetricEncryptionScope, str]] = ..., security: _Optional[_Union[UniversalSecurityProperties, _Mapping]] = ..., additional_properties: _Optional[_Mapping[str, str]] = ...) -> None: ...

class ScopeSpecification(_message.Message):
    __slots__ = ("signature", "aead", "mac", "kem", "key_agreement", "kdf", "hash", "key_wrapping", "symmetric_cipher", "generic_secret", "disk_encryption", "asymmetric_encryption")
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    AEAD_FIELD_NUMBER: _ClassVar[int]
    MAC_FIELD_NUMBER: _ClassVar[int]
    KEM_FIELD_NUMBER: _ClassVar[int]
    KEY_AGREEMENT_FIELD_NUMBER: _ClassVar[int]
    KDF_FIELD_NUMBER: _ClassVar[int]
    HASH_FIELD_NUMBER: _ClassVar[int]
    KEY_WRAPPING_FIELD_NUMBER: _ClassVar[int]
    SYMMETRIC_CIPHER_FIELD_NUMBER: _ClassVar[int]
    GENERIC_SECRET_FIELD_NUMBER: _ClassVar[int]
    DISK_ENCRYPTION_FIELD_NUMBER: _ClassVar[int]
    ASYMMETRIC_ENCRYPTION_FIELD_NUMBER: _ClassVar[int]
    signature: SignatureScopeSpec
    aead: AeadScopeSpec
    mac: MacScopeSpec
    kem: KemScopeSpec
    key_agreement: KeyAgreementScopeSpec
    kdf: KdfScopeSpec
    hash: HashScopeSpec
    key_wrapping: KeyWrappingScopeSpec
    symmetric_cipher: SymmetricCipherScopeSpec
    generic_secret: GenericSecretScopeSpec
    disk_encryption: DiskEncryptionScopeSpec
    asymmetric_encryption: AsymmetricEncryptionScopeSpec
    def __init__(self, signature: _Optional[_Union[SignatureScopeSpec, _Mapping]] = ..., aead: _Optional[_Union[AeadScopeSpec, _Mapping]] = ..., mac: _Optional[_Union[MacScopeSpec, _Mapping]] = ..., kem: _Optional[_Union[KemScopeSpec, _Mapping]] = ..., key_agreement: _Optional[_Union[KeyAgreementScopeSpec, _Mapping]] = ..., kdf: _Optional[_Union[KdfScopeSpec, _Mapping]] = ..., hash: _Optional[_Union[HashScopeSpec, _Mapping]] = ..., key_wrapping: _Optional[_Union[KeyWrappingScopeSpec, _Mapping]] = ..., symmetric_cipher: _Optional[_Union[SymmetricCipherScopeSpec, _Mapping]] = ..., generic_secret: _Optional[_Union[GenericSecretScopeSpec, _Mapping]] = ..., disk_encryption: _Optional[_Union[DiskEncryptionScopeSpec, _Mapping]] = ..., asymmetric_encryption: _Optional[_Union[AsymmetricEncryptionScopeSpec, _Mapping]] = ...) -> None: ...

class FormalSecurityNotions(_message.Message):
    __slots__ = ("ind_cpa", "ind_cca1", "ind_cca2", "nm_cpa", "int_ctxt", "int_ptxt", "euf_cma", "suf_cma", "prf", "preimage_resistant", "second_preimage_resistant", "collision_resistant", "ow_cca", "ind_cca_kem")
    IND_CPA_FIELD_NUMBER: _ClassVar[int]
    IND_CCA1_FIELD_NUMBER: _ClassVar[int]
    IND_CCA2_FIELD_NUMBER: _ClassVar[int]
    NM_CPA_FIELD_NUMBER: _ClassVar[int]
    INT_CTXT_FIELD_NUMBER: _ClassVar[int]
    INT_PTXT_FIELD_NUMBER: _ClassVar[int]
    EUF_CMA_FIELD_NUMBER: _ClassVar[int]
    SUF_CMA_FIELD_NUMBER: _ClassVar[int]
    PRF_FIELD_NUMBER: _ClassVar[int]
    PREIMAGE_RESISTANT_FIELD_NUMBER: _ClassVar[int]
    SECOND_PREIMAGE_RESISTANT_FIELD_NUMBER: _ClassVar[int]
    COLLISION_RESISTANT_FIELD_NUMBER: _ClassVar[int]
    OW_CCA_FIELD_NUMBER: _ClassVar[int]
    IND_CCA_KEM_FIELD_NUMBER: _ClassVar[int]
    ind_cpa: bool
    ind_cca1: bool
    ind_cca2: bool
    nm_cpa: bool
    int_ctxt: bool
    int_ptxt: bool
    euf_cma: bool
    suf_cma: bool
    prf: bool
    preimage_resistant: bool
    second_preimage_resistant: bool
    collision_resistant: bool
    ow_cca: bool
    ind_cca_kem: bool
    def __init__(self, ind_cpa: _Optional[bool] = ..., ind_cca1: _Optional[bool] = ..., ind_cca2: _Optional[bool] = ..., nm_cpa: _Optional[bool] = ..., int_ctxt: _Optional[bool] = ..., int_ptxt: _Optional[bool] = ..., euf_cma: _Optional[bool] = ..., suf_cma: _Optional[bool] = ..., prf: _Optional[bool] = ..., preimage_resistant: _Optional[bool] = ..., second_preimage_resistant: _Optional[bool] = ..., collision_resistant: _Optional[bool] = ..., ow_cca: _Optional[bool] = ..., ind_cca_kem: _Optional[bool] = ...) -> None: ...

class PracticalSecurityOutcomes(_message.Message):
    __slots__ = ("confidentiality", "integrity", "authenticity", "non_repudiation")
    CONFIDENTIALITY_FIELD_NUMBER: _ClassVar[int]
    INTEGRITY_FIELD_NUMBER: _ClassVar[int]
    AUTHENTICITY_FIELD_NUMBER: _ClassVar[int]
    NON_REPUDIATION_FIELD_NUMBER: _ClassVar[int]
    confidentiality: bool
    integrity: bool
    authenticity: bool
    non_repudiation: bool
    def __init__(self, confidentiality: _Optional[bool] = ..., integrity: _Optional[bool] = ..., authenticity: _Optional[bool] = ..., non_repudiation: _Optional[bool] = ...) -> None: ...

class OperationalBounds(_message.Message):
    __slots__ = ("authentication_strength_bits", "max_messages_per_key", "max_plaintext_bytes_per_key", "attack_success_probability")
    AUTHENTICATION_STRENGTH_BITS_FIELD_NUMBER: _ClassVar[int]
    MAX_MESSAGES_PER_KEY_FIELD_NUMBER: _ClassVar[int]
    MAX_PLAINTEXT_BYTES_PER_KEY_FIELD_NUMBER: _ClassVar[int]
    ATTACK_SUCCESS_PROBABILITY_FIELD_NUMBER: _ClassVar[int]
    authentication_strength_bits: int
    max_messages_per_key: int
    max_plaintext_bytes_per_key: int
    attack_success_probability: str
    def __init__(self, authentication_strength_bits: _Optional[int] = ..., max_messages_per_key: _Optional[int] = ..., max_plaintext_bytes_per_key: _Optional[int] = ..., attack_success_probability: _Optional[str] = ...) -> None: ...

class SecurityGuarantees(_message.Message):
    __slots__ = ("formal", "practical", "bounds", "additional_properties")
    class AdditionalPropertiesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    FORMAL_FIELD_NUMBER: _ClassVar[int]
    PRACTICAL_FIELD_NUMBER: _ClassVar[int]
    BOUNDS_FIELD_NUMBER: _ClassVar[int]
    ADDITIONAL_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    formal: FormalSecurityNotions
    practical: PracticalSecurityOutcomes
    bounds: OperationalBounds
    additional_properties: _containers.ScalarMap[str, str]
    def __init__(self, formal: _Optional[_Union[FormalSecurityNotions, _Mapping]] = ..., practical: _Optional[_Union[PracticalSecurityOutcomes, _Mapping]] = ..., bounds: _Optional[_Union[OperationalBounds, _Mapping]] = ..., additional_properties: _Optional[_Mapping[str, str]] = ...) -> None: ...
