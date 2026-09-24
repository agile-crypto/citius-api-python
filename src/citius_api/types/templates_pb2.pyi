from citius_api.buf.validate import validate_pb2 as _validate_pb2
from citius_api.types import common_pb2 as _common_pb2
from citius_api.types import algorithm_params_pb2 as _algorithm_params_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TemplateStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TEMPLATE_STATUS_UNSPECIFIED: _ClassVar[TemplateStatus]
    TEMPLATE_STATUS_ACTIVE: _ClassVar[TemplateStatus]
    TEMPLATE_STATUS_ACCEPTABLE: _ClassVar[TemplateStatus]
    TEMPLATE_STATUS_DEPRECATED: _ClassVar[TemplateStatus]
    TEMPLATE_STATUS_FORBIDDEN: _ClassVar[TemplateStatus]
    TEMPLATE_STATUS_EXPERIMENTAL: _ClassVar[TemplateStatus]
TEMPLATE_STATUS_UNSPECIFIED: TemplateStatus
TEMPLATE_STATUS_ACTIVE: TemplateStatus
TEMPLATE_STATUS_ACCEPTABLE: TemplateStatus
TEMPLATE_STATUS_DEPRECATED: TemplateStatus
TEMPLATE_STATUS_FORBIDDEN: TemplateStatus
TEMPLATE_STATUS_EXPERIMENTAL: TemplateStatus

class AlgorithmDetails(_message.Message):
    __slots__ = ("oid", "primitive", "aes_gcm", "aes_cbc", "aes_ctr", "chacha20_poly1305", "aes_ccm", "aes_xts", "triple_des", "blowfish", "twofish", "ecdsa", "ed25519", "ed448", "rsa_pss", "rsa_pkcs1v15", "dsa", "ml_dsa", "slh_dsa", "gost3410", "ml_kem", "rsa_oaep", "hkdf", "pbkdf2", "argon2", "sp800_108_kdf", "tls12", "hmac", "kmac", "cmac", "gost3411", "poly1305", "aes_key_wrap", "ecdh", "x25519", "x448", "diffie_hellman", "x3dh", "camellia", "aria", "seed", "gost28147", "hotp", "totp", "custom", "hybrid")
    OID_FIELD_NUMBER: _ClassVar[int]
    PRIMITIVE_FIELD_NUMBER: _ClassVar[int]
    AES_GCM_FIELD_NUMBER: _ClassVar[int]
    AES_CBC_FIELD_NUMBER: _ClassVar[int]
    AES_CTR_FIELD_NUMBER: _ClassVar[int]
    CHACHA20_POLY1305_FIELD_NUMBER: _ClassVar[int]
    AES_CCM_FIELD_NUMBER: _ClassVar[int]
    AES_XTS_FIELD_NUMBER: _ClassVar[int]
    TRIPLE_DES_FIELD_NUMBER: _ClassVar[int]
    BLOWFISH_FIELD_NUMBER: _ClassVar[int]
    TWOFISH_FIELD_NUMBER: _ClassVar[int]
    ECDSA_FIELD_NUMBER: _ClassVar[int]
    ED25519_FIELD_NUMBER: _ClassVar[int]
    ED448_FIELD_NUMBER: _ClassVar[int]
    RSA_PSS_FIELD_NUMBER: _ClassVar[int]
    RSA_PKCS1V15_FIELD_NUMBER: _ClassVar[int]
    DSA_FIELD_NUMBER: _ClassVar[int]
    ML_DSA_FIELD_NUMBER: _ClassVar[int]
    SLH_DSA_FIELD_NUMBER: _ClassVar[int]
    GOST3410_FIELD_NUMBER: _ClassVar[int]
    ML_KEM_FIELD_NUMBER: _ClassVar[int]
    RSA_OAEP_FIELD_NUMBER: _ClassVar[int]
    HKDF_FIELD_NUMBER: _ClassVar[int]
    PBKDF2_FIELD_NUMBER: _ClassVar[int]
    ARGON2_FIELD_NUMBER: _ClassVar[int]
    SP800_108_KDF_FIELD_NUMBER: _ClassVar[int]
    TLS12_FIELD_NUMBER: _ClassVar[int]
    HMAC_FIELD_NUMBER: _ClassVar[int]
    KMAC_FIELD_NUMBER: _ClassVar[int]
    CMAC_FIELD_NUMBER: _ClassVar[int]
    GOST3411_FIELD_NUMBER: _ClassVar[int]
    POLY1305_FIELD_NUMBER: _ClassVar[int]
    AES_KEY_WRAP_FIELD_NUMBER: _ClassVar[int]
    ECDH_FIELD_NUMBER: _ClassVar[int]
    X25519_FIELD_NUMBER: _ClassVar[int]
    X448_FIELD_NUMBER: _ClassVar[int]
    DIFFIE_HELLMAN_FIELD_NUMBER: _ClassVar[int]
    X3DH_FIELD_NUMBER: _ClassVar[int]
    CAMELLIA_FIELD_NUMBER: _ClassVar[int]
    ARIA_FIELD_NUMBER: _ClassVar[int]
    SEED_FIELD_NUMBER: _ClassVar[int]
    GOST28147_FIELD_NUMBER: _ClassVar[int]
    HOTP_FIELD_NUMBER: _ClassVar[int]
    TOTP_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_FIELD_NUMBER: _ClassVar[int]
    HYBRID_FIELD_NUMBER: _ClassVar[int]
    oid: str
    primitive: _algorithm_params_pb2.CryptoPrimitive
    aes_gcm: _algorithm_params_pb2.AesGcmParams
    aes_cbc: _algorithm_params_pb2.AesCbcParams
    aes_ctr: _algorithm_params_pb2.AesCtrParams
    chacha20_poly1305: _algorithm_params_pb2.ChaCha20Poly1305Params
    aes_ccm: _algorithm_params_pb2.AesCcmParams
    aes_xts: _algorithm_params_pb2.AesXtsParams
    triple_des: _algorithm_params_pb2.TripleDesParams
    blowfish: _algorithm_params_pb2.BlowfishParams
    twofish: _algorithm_params_pb2.TwofishParams
    ecdsa: _algorithm_params_pb2.EcdsaParams
    ed25519: _algorithm_params_pb2.Ed25519Params
    ed448: _algorithm_params_pb2.Ed448Params
    rsa_pss: _algorithm_params_pb2.RsaPssParams
    rsa_pkcs1v15: _algorithm_params_pb2.RsaPkcs1v15Params
    dsa: _algorithm_params_pb2.DsaParams
    ml_dsa: _algorithm_params_pb2.MlDsaParams
    slh_dsa: _algorithm_params_pb2.SlhDsaParams
    gost3410: _algorithm_params_pb2.Gost3410Params
    ml_kem: _algorithm_params_pb2.MlKemParams
    rsa_oaep: _algorithm_params_pb2.RsaOaepParams
    hkdf: _algorithm_params_pb2.HkdfParams
    pbkdf2: _algorithm_params_pb2.Pbkdf2Params
    argon2: _algorithm_params_pb2.Argon2Params
    sp800_108_kdf: _algorithm_params_pb2.Sp800108KdfParams
    tls12: _algorithm_params_pb2.Tls12Params
    hmac: _algorithm_params_pb2.HmacParams
    kmac: _algorithm_params_pb2.KmacParams
    cmac: _algorithm_params_pb2.CmacParams
    gost3411: _algorithm_params_pb2.Gost3411Params
    poly1305: _algorithm_params_pb2.Poly1305Params
    aes_key_wrap: _algorithm_params_pb2.AesKeyWrapParams
    ecdh: _algorithm_params_pb2.EcdhParams
    x25519: _algorithm_params_pb2.X25519Params
    x448: _algorithm_params_pb2.X448Params
    diffie_hellman: _algorithm_params_pb2.DiffieHellmanParams
    x3dh: _algorithm_params_pb2.X3dhParams
    camellia: _algorithm_params_pb2.CamelliaParams
    aria: _algorithm_params_pb2.AriaParams
    seed: _algorithm_params_pb2.SeedParams
    gost28147: _algorithm_params_pb2.Gost28147Params
    hotp: _algorithm_params_pb2.HotpParams
    totp: _algorithm_params_pb2.TotpParams
    custom: _algorithm_params_pb2.CustomAlgorithm
    hybrid: HybridAlgorithmParams
    def __init__(self, oid: _Optional[str] = ..., primitive: _Optional[_Union[_algorithm_params_pb2.CryptoPrimitive, str]] = ..., aes_gcm: _Optional[_Union[_algorithm_params_pb2.AesGcmParams, _Mapping]] = ..., aes_cbc: _Optional[_Union[_algorithm_params_pb2.AesCbcParams, _Mapping]] = ..., aes_ctr: _Optional[_Union[_algorithm_params_pb2.AesCtrParams, _Mapping]] = ..., chacha20_poly1305: _Optional[_Union[_algorithm_params_pb2.ChaCha20Poly1305Params, _Mapping]] = ..., aes_ccm: _Optional[_Union[_algorithm_params_pb2.AesCcmParams, _Mapping]] = ..., aes_xts: _Optional[_Union[_algorithm_params_pb2.AesXtsParams, _Mapping]] = ..., triple_des: _Optional[_Union[_algorithm_params_pb2.TripleDesParams, _Mapping]] = ..., blowfish: _Optional[_Union[_algorithm_params_pb2.BlowfishParams, _Mapping]] = ..., twofish: _Optional[_Union[_algorithm_params_pb2.TwofishParams, _Mapping]] = ..., ecdsa: _Optional[_Union[_algorithm_params_pb2.EcdsaParams, _Mapping]] = ..., ed25519: _Optional[_Union[_algorithm_params_pb2.Ed25519Params, _Mapping]] = ..., ed448: _Optional[_Union[_algorithm_params_pb2.Ed448Params, _Mapping]] = ..., rsa_pss: _Optional[_Union[_algorithm_params_pb2.RsaPssParams, _Mapping]] = ..., rsa_pkcs1v15: _Optional[_Union[_algorithm_params_pb2.RsaPkcs1v15Params, _Mapping]] = ..., dsa: _Optional[_Union[_algorithm_params_pb2.DsaParams, _Mapping]] = ..., ml_dsa: _Optional[_Union[_algorithm_params_pb2.MlDsaParams, _Mapping]] = ..., slh_dsa: _Optional[_Union[_algorithm_params_pb2.SlhDsaParams, _Mapping]] = ..., gost3410: _Optional[_Union[_algorithm_params_pb2.Gost3410Params, _Mapping]] = ..., ml_kem: _Optional[_Union[_algorithm_params_pb2.MlKemParams, _Mapping]] = ..., rsa_oaep: _Optional[_Union[_algorithm_params_pb2.RsaOaepParams, _Mapping]] = ..., hkdf: _Optional[_Union[_algorithm_params_pb2.HkdfParams, _Mapping]] = ..., pbkdf2: _Optional[_Union[_algorithm_params_pb2.Pbkdf2Params, _Mapping]] = ..., argon2: _Optional[_Union[_algorithm_params_pb2.Argon2Params, _Mapping]] = ..., sp800_108_kdf: _Optional[_Union[_algorithm_params_pb2.Sp800108KdfParams, _Mapping]] = ..., tls12: _Optional[_Union[_algorithm_params_pb2.Tls12Params, _Mapping]] = ..., hmac: _Optional[_Union[_algorithm_params_pb2.HmacParams, _Mapping]] = ..., kmac: _Optional[_Union[_algorithm_params_pb2.KmacParams, _Mapping]] = ..., cmac: _Optional[_Union[_algorithm_params_pb2.CmacParams, _Mapping]] = ..., gost3411: _Optional[_Union[_algorithm_params_pb2.Gost3411Params, _Mapping]] = ..., poly1305: _Optional[_Union[_algorithm_params_pb2.Poly1305Params, _Mapping]] = ..., aes_key_wrap: _Optional[_Union[_algorithm_params_pb2.AesKeyWrapParams, _Mapping]] = ..., ecdh: _Optional[_Union[_algorithm_params_pb2.EcdhParams, _Mapping]] = ..., x25519: _Optional[_Union[_algorithm_params_pb2.X25519Params, _Mapping]] = ..., x448: _Optional[_Union[_algorithm_params_pb2.X448Params, _Mapping]] = ..., diffie_hellman: _Optional[_Union[_algorithm_params_pb2.DiffieHellmanParams, _Mapping]] = ..., x3dh: _Optional[_Union[_algorithm_params_pb2.X3dhParams, _Mapping]] = ..., camellia: _Optional[_Union[_algorithm_params_pb2.CamelliaParams, _Mapping]] = ..., aria: _Optional[_Union[_algorithm_params_pb2.AriaParams, _Mapping]] = ..., seed: _Optional[_Union[_algorithm_params_pb2.SeedParams, _Mapping]] = ..., gost28147: _Optional[_Union[_algorithm_params_pb2.Gost28147Params, _Mapping]] = ..., hotp: _Optional[_Union[_algorithm_params_pb2.HotpParams, _Mapping]] = ..., totp: _Optional[_Union[_algorithm_params_pb2.TotpParams, _Mapping]] = ..., custom: _Optional[_Union[_algorithm_params_pb2.CustomAlgorithm, _Mapping]] = ..., hybrid: _Optional[_Union[HybridAlgorithmParams, _Mapping]] = ...) -> None: ...

class HybridAlgorithmParams(_message.Message):
    __slots__ = ("combiner_strategy", "components", "total_key_size_bits")
    class CombinerStrategy(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        COMBINER_UNSPECIFIED: _ClassVar[HybridAlgorithmParams.CombinerStrategy]
        COMBINER_CONCATENATION: _ClassVar[HybridAlgorithmParams.CombinerStrategy]
        COMBINER_NESTING: _ClassVar[HybridAlgorithmParams.CombinerStrategy]
        COMBINER_KDF_COMBINATION: _ClassVar[HybridAlgorithmParams.CombinerStrategy]
    COMBINER_UNSPECIFIED: HybridAlgorithmParams.CombinerStrategy
    COMBINER_CONCATENATION: HybridAlgorithmParams.CombinerStrategy
    COMBINER_NESTING: HybridAlgorithmParams.CombinerStrategy
    COMBINER_KDF_COMBINATION: HybridAlgorithmParams.CombinerStrategy
    COMBINER_STRATEGY_FIELD_NUMBER: _ClassVar[int]
    COMPONENTS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_KEY_SIZE_BITS_FIELD_NUMBER: _ClassVar[int]
    combiner_strategy: HybridAlgorithmParams.CombinerStrategy
    components: _containers.RepeatedCompositeFieldContainer[HybridComponent]
    total_key_size_bits: int
    def __init__(self, combiner_strategy: _Optional[_Union[HybridAlgorithmParams.CombinerStrategy, str]] = ..., components: _Optional[_Iterable[_Union[HybridComponent, _Mapping]]] = ..., total_key_size_bits: _Optional[int] = ...) -> None: ...

class HybridComponent(_message.Message):
    __slots__ = ("algorithm", "label", "order")
    ALGORITHM_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    ORDER_FIELD_NUMBER: _ClassVar[int]
    algorithm: AlgorithmDetails
    label: str
    order: int
    def __init__(self, algorithm: _Optional[_Union[AlgorithmDetails, _Mapping]] = ..., label: _Optional[str] = ..., order: _Optional[int] = ...) -> None: ...

class ScopedCapabilities(_message.Message):
    __slots__ = ("scope", "operations", "security_guarantees")
    SCOPE_FIELD_NUMBER: _ClassVar[int]
    OPERATIONS_FIELD_NUMBER: _ClassVar[int]
    SECURITY_GUARANTEES_FIELD_NUMBER: _ClassVar[int]
    scope: _common_pb2.ScopeSpecification
    operations: _containers.RepeatedScalarFieldContainer[_common_pb2.CryptoOperation]
    security_guarantees: _common_pb2.SecurityGuarantees
    def __init__(self, scope: _Optional[_Union[_common_pb2.ScopeSpecification, _Mapping]] = ..., operations: _Optional[_Iterable[_Union[_common_pb2.CryptoOperation, str]]] = ..., security_guarantees: _Optional[_Union[_common_pb2.SecurityGuarantees, _Mapping]] = ...) -> None: ...

class TemplateInfo(_message.Message):
    __slots__ = ("template_id", "display_name", "description", "scoped_capabilities", "algorithm", "status", "deprecation_notice", "standards", "cyclonedx", "security_guarantees", "key_material_family")
    TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    SCOPED_CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    ALGORITHM_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    DEPRECATION_NOTICE_FIELD_NUMBER: _ClassVar[int]
    STANDARDS_FIELD_NUMBER: _ClassVar[int]
    CYCLONEDX_FIELD_NUMBER: _ClassVar[int]
    SECURITY_GUARANTEES_FIELD_NUMBER: _ClassVar[int]
    KEY_MATERIAL_FAMILY_FIELD_NUMBER: _ClassVar[int]
    template_id: str
    display_name: str
    description: str
    scoped_capabilities: _containers.RepeatedCompositeFieldContainer[ScopedCapabilities]
    algorithm: AlgorithmDetails
    status: TemplateStatus
    deprecation_notice: str
    standards: _containers.RepeatedScalarFieldContainer[str]
    cyclonedx: CycloneDXAlgorithmProperties
    security_guarantees: _common_pb2.SecurityGuarantees
    key_material_family: str
    def __init__(self, template_id: _Optional[str] = ..., display_name: _Optional[str] = ..., description: _Optional[str] = ..., scoped_capabilities: _Optional[_Iterable[_Union[ScopedCapabilities, _Mapping]]] = ..., algorithm: _Optional[_Union[AlgorithmDetails, _Mapping]] = ..., status: _Optional[_Union[TemplateStatus, str]] = ..., deprecation_notice: _Optional[str] = ..., standards: _Optional[_Iterable[str]] = ..., cyclonedx: _Optional[_Union[CycloneDXAlgorithmProperties, _Mapping]] = ..., security_guarantees: _Optional[_Union[_common_pb2.SecurityGuarantees, _Mapping]] = ..., key_material_family: _Optional[str] = ...) -> None: ...

class CycloneDXAlgorithmProperties(_message.Message):
    __slots__ = ("name", "primitive", "algorithm_family", "parameter_set_identifier", "elliptic_curve", "mode", "padding", "crypto_functions", "classical_security_level", "nist_quantum_security_level", "certification_level", "execution_environment", "implementation_platform", "oid")
    NAME_FIELD_NUMBER: _ClassVar[int]
    PRIMITIVE_FIELD_NUMBER: _ClassVar[int]
    ALGORITHM_FAMILY_FIELD_NUMBER: _ClassVar[int]
    PARAMETER_SET_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    ELLIPTIC_CURVE_FIELD_NUMBER: _ClassVar[int]
    MODE_FIELD_NUMBER: _ClassVar[int]
    PADDING_FIELD_NUMBER: _ClassVar[int]
    CRYPTO_FUNCTIONS_FIELD_NUMBER: _ClassVar[int]
    CLASSICAL_SECURITY_LEVEL_FIELD_NUMBER: _ClassVar[int]
    NIST_QUANTUM_SECURITY_LEVEL_FIELD_NUMBER: _ClassVar[int]
    CERTIFICATION_LEVEL_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_ENVIRONMENT_FIELD_NUMBER: _ClassVar[int]
    IMPLEMENTATION_PLATFORM_FIELD_NUMBER: _ClassVar[int]
    OID_FIELD_NUMBER: _ClassVar[int]
    name: str
    primitive: str
    algorithm_family: str
    parameter_set_identifier: str
    elliptic_curve: str
    mode: str
    padding: str
    crypto_functions: _containers.RepeatedScalarFieldContainer[str]
    classical_security_level: int
    nist_quantum_security_level: int
    certification_level: _containers.RepeatedScalarFieldContainer[str]
    execution_environment: str
    implementation_platform: str
    oid: str
    def __init__(self, name: _Optional[str] = ..., primitive: _Optional[str] = ..., algorithm_family: _Optional[str] = ..., parameter_set_identifier: _Optional[str] = ..., elliptic_curve: _Optional[str] = ..., mode: _Optional[str] = ..., padding: _Optional[str] = ..., crypto_functions: _Optional[_Iterable[str]] = ..., classical_security_level: _Optional[int] = ..., nist_quantum_security_level: _Optional[int] = ..., certification_level: _Optional[_Iterable[str]] = ..., execution_environment: _Optional[str] = ..., implementation_platform: _Optional[str] = ..., oid: _Optional[str] = ...) -> None: ...

class ScopeInfo(_message.Message):
    __slots__ = ("specification", "name", "description", "typical_use_cases", "supported_operations")
    SPECIFICATION_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    TYPICAL_USE_CASES_FIELD_NUMBER: _ClassVar[int]
    SUPPORTED_OPERATIONS_FIELD_NUMBER: _ClassVar[int]
    specification: _common_pb2.ScopeSpecification
    name: str
    description: str
    typical_use_cases: _containers.RepeatedScalarFieldContainer[str]
    supported_operations: _containers.RepeatedScalarFieldContainer[_common_pb2.CryptoOperation]
    def __init__(self, specification: _Optional[_Union[_common_pb2.ScopeSpecification, _Mapping]] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., typical_use_cases: _Optional[_Iterable[str]] = ..., supported_operations: _Optional[_Iterable[_Union[_common_pb2.CryptoOperation, str]]] = ...) -> None: ...
