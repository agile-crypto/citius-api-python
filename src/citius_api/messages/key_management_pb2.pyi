import datetime

from google.protobuf import timestamp_pb2 as _timestamp_pb2
from citius_api.types import common_pb2 as _common_pb2
from citius_api.types import templates_pb2 as _templates_pb2
from citius_api.types import implementation_pb2 as _implementation_pb2
from citius_api.types import providers_pb2 as _providers_pb2
from citius_api.buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MigrationStrategy(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MIGRATION_STRATEGY_UNSPECIFIED: _ClassVar[MigrationStrategy]
    MIGRATION_STRATEGY_PROVIDER_SWITCH: _ClassVar[MigrationStrategy]
    MIGRATION_STRATEGY_EXTRACT_AND_IMPORT: _ClassVar[MigrationStrategy]
    MIGRATION_STRATEGY_WRAPPED_TRANSFER: _ClassVar[MigrationStrategy]
    MIGRATION_STRATEGY_REKEY_AND_ARCHIVE: _ClassVar[MigrationStrategy]
    MIGRATION_STRATEGY_REKEY_AND_DESTROY: _ClassVar[MigrationStrategy]
MIGRATION_STRATEGY_UNSPECIFIED: MigrationStrategy
MIGRATION_STRATEGY_PROVIDER_SWITCH: MigrationStrategy
MIGRATION_STRATEGY_EXTRACT_AND_IMPORT: MigrationStrategy
MIGRATION_STRATEGY_WRAPPED_TRANSFER: MigrationStrategy
MIGRATION_STRATEGY_REKEY_AND_ARCHIVE: MigrationStrategy
MIGRATION_STRATEGY_REKEY_AND_DESTROY: MigrationStrategy

class CreateKeyRequest(_message.Message):
    __slots__ = ("name", "policy", "provider_id", "provider_configuration", "scope_spec", "template_id", "provider_requirements", "activation_time", "expiration_time")
    class ProviderConfigurationEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    POLICY_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_ID_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_CONFIGURATION_FIELD_NUMBER: _ClassVar[int]
    SCOPE_SPEC_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_REQUIREMENTS_FIELD_NUMBER: _ClassVar[int]
    ACTIVATION_TIME_FIELD_NUMBER: _ClassVar[int]
    EXPIRATION_TIME_FIELD_NUMBER: _ClassVar[int]
    name: str
    policy: str
    provider_id: str
    provider_configuration: _containers.ScalarMap[str, str]
    scope_spec: _common_pb2.ScopeSpecification
    template_id: str
    provider_requirements: _implementation_pb2.ProviderRequirements
    activation_time: _timestamp_pb2.Timestamp
    expiration_time: _timestamp_pb2.Timestamp
    def __init__(self, name: _Optional[str] = ..., policy: _Optional[str] = ..., provider_id: _Optional[str] = ..., provider_configuration: _Optional[_Mapping[str, str]] = ..., scope_spec: _Optional[_Union[_common_pb2.ScopeSpecification, _Mapping]] = ..., template_id: _Optional[str] = ..., provider_requirements: _Optional[_Union[_implementation_pb2.ProviderRequirements, _Mapping]] = ..., activation_time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., expiration_time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class CreateKeyResponse(_message.Message):
    __slots__ = ("success", "message", "key_metadata", "security_guarantees", "implementation_properties")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    KEY_METADATA_FIELD_NUMBER: _ClassVar[int]
    SECURITY_GUARANTEES_FIELD_NUMBER: _ClassVar[int]
    IMPLEMENTATION_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    success: bool
    message: str
    key_metadata: KeyMetadata
    security_guarantees: _common_pb2.SecurityGuarantees
    implementation_properties: _implementation_pb2.ImplementationProperties
    def __init__(self, success: _Optional[bool] = ..., message: _Optional[str] = ..., key_metadata: _Optional[_Union[KeyMetadata, _Mapping]] = ..., security_guarantees: _Optional[_Union[_common_pb2.SecurityGuarantees, _Mapping]] = ..., implementation_properties: _Optional[_Union[_implementation_pb2.ImplementationProperties, _Mapping]] = ...) -> None: ...

class KeyMetadata(_message.Message):
    __slots__ = ("name", "version", "key_id", "template_id", "scope_spec", "provider", "created_time", "updated_time", "policy", "provider_metadata", "template_info", "implementation_properties", "extractable", "lifecycle_state", "public_key_bytes", "public_key_format", "activation_time", "expiration_time", "origin")
    class ProviderMetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    KEY_ID_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    SCOPE_SPEC_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_FIELD_NUMBER: _ClassVar[int]
    CREATED_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATED_TIME_FIELD_NUMBER: _ClassVar[int]
    POLICY_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_METADATA_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_INFO_FIELD_NUMBER: _ClassVar[int]
    IMPLEMENTATION_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    EXTRACTABLE_FIELD_NUMBER: _ClassVar[int]
    LIFECYCLE_STATE_FIELD_NUMBER: _ClassVar[int]
    PUBLIC_KEY_BYTES_FIELD_NUMBER: _ClassVar[int]
    PUBLIC_KEY_FORMAT_FIELD_NUMBER: _ClassVar[int]
    ACTIVATION_TIME_FIELD_NUMBER: _ClassVar[int]
    EXPIRATION_TIME_FIELD_NUMBER: _ClassVar[int]
    ORIGIN_FIELD_NUMBER: _ClassVar[int]
    name: str
    version: int
    key_id: str
    template_id: str
    scope_spec: _common_pb2.ScopeSpecification
    provider: str
    created_time: _timestamp_pb2.Timestamp
    updated_time: _timestamp_pb2.Timestamp
    policy: str
    provider_metadata: _containers.ScalarMap[str, str]
    template_info: _templates_pb2.TemplateInfo
    implementation_properties: _implementation_pb2.ImplementationProperties
    extractable: bool
    lifecycle_state: _common_pb2.KeyLifecycleState
    public_key_bytes: bytes
    public_key_format: _common_pb2.KeyFormat
    activation_time: _timestamp_pb2.Timestamp
    expiration_time: _timestamp_pb2.Timestamp
    origin: _common_pb2.KeyOrigin
    def __init__(self, name: _Optional[str] = ..., version: _Optional[int] = ..., key_id: _Optional[str] = ..., template_id: _Optional[str] = ..., scope_spec: _Optional[_Union[_common_pb2.ScopeSpecification, _Mapping]] = ..., provider: _Optional[str] = ..., created_time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., policy: _Optional[str] = ..., provider_metadata: _Optional[_Mapping[str, str]] = ..., template_info: _Optional[_Union[_templates_pb2.TemplateInfo, _Mapping]] = ..., implementation_properties: _Optional[_Union[_implementation_pb2.ImplementationProperties, _Mapping]] = ..., extractable: _Optional[bool] = ..., lifecycle_state: _Optional[_Union[_common_pb2.KeyLifecycleState, str]] = ..., public_key_bytes: _Optional[bytes] = ..., public_key_format: _Optional[_Union[_common_pb2.KeyFormat, str]] = ..., activation_time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., expiration_time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., origin: _Optional[_Union[_common_pb2.KeyOrigin, str]] = ...) -> None: ...

class ReadKeyRequest(_message.Message):
    __slots__ = ("name", "version")
    NAME_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    name: str
    version: int
    def __init__(self, name: _Optional[str] = ..., version: _Optional[int] = ...) -> None: ...

class ReadKeyResponse(_message.Message):
    __slots__ = ("key_metadata",)
    KEY_METADATA_FIELD_NUMBER: _ClassVar[int]
    key_metadata: KeyMetadata
    def __init__(self, key_metadata: _Optional[_Union[KeyMetadata, _Mapping]] = ...) -> None: ...

class ListKeysRequest(_message.Message):
    __slots__ = ("scope_spec", "provider_id", "policy", "lifecycle_state", "page_size", "page_token")
    SCOPE_SPEC_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_ID_FIELD_NUMBER: _ClassVar[int]
    POLICY_FIELD_NUMBER: _ClassVar[int]
    LIFECYCLE_STATE_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    scope_spec: _common_pb2.ScopeSpecification
    provider_id: str
    policy: str
    lifecycle_state: _common_pb2.KeyLifecycleState
    page_size: int
    page_token: str
    def __init__(self, scope_spec: _Optional[_Union[_common_pb2.ScopeSpecification, _Mapping]] = ..., provider_id: _Optional[str] = ..., policy: _Optional[str] = ..., lifecycle_state: _Optional[_Union[_common_pb2.KeyLifecycleState, str]] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class ListKeysResponse(_message.Message):
    __slots__ = ("keys", "next_page_token")
    KEYS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    keys: _containers.RepeatedCompositeFieldContainer[KeyMetadata]
    next_page_token: str
    def __init__(self, keys: _Optional[_Iterable[_Union[KeyMetadata, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class DeleteKeyRequest(_message.Message):
    __slots__ = ("name", "remove_metadata")
    NAME_FIELD_NUMBER: _ClassVar[int]
    REMOVE_METADATA_FIELD_NUMBER: _ClassVar[int]
    name: str
    remove_metadata: bool
    def __init__(self, name: _Optional[str] = ..., remove_metadata: _Optional[bool] = ...) -> None: ...

class DeleteKeyResponse(_message.Message):
    __slots__ = ("success", "message")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    success: bool
    message: str
    def __init__(self, success: _Optional[bool] = ..., message: _Optional[str] = ...) -> None: ...

class RotateKeyRequest(_message.Message):
    __slots__ = ("name", "reason")
    NAME_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    name: str
    reason: str
    def __init__(self, name: _Optional[str] = ..., reason: _Optional[str] = ...) -> None: ...

class UpdateKeyStateRequest(_message.Message):
    __slots__ = ("name", "target_state", "reason")
    NAME_FIELD_NUMBER: _ClassVar[int]
    TARGET_STATE_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    name: str
    target_state: _common_pb2.KeyLifecycleState
    reason: str
    def __init__(self, name: _Optional[str] = ..., target_state: _Optional[_Union[_common_pb2.KeyLifecycleState, str]] = ..., reason: _Optional[str] = ...) -> None: ...

class UpdateKeyStateResponse(_message.Message):
    __slots__ = ("success", "message", "key_metadata")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    KEY_METADATA_FIELD_NUMBER: _ClassVar[int]
    success: bool
    message: str
    key_metadata: KeyMetadata
    def __init__(self, success: _Optional[bool] = ..., message: _Optional[str] = ..., key_metadata: _Optional[_Union[KeyMetadata, _Mapping]] = ...) -> None: ...

class RotateKeyResponse(_message.Message):
    __slots__ = ("success", "message", "new_key_metadata")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    NEW_KEY_METADATA_FIELD_NUMBER: _ClassVar[int]
    success: bool
    message: str
    new_key_metadata: KeyMetadata
    def __init__(self, success: _Optional[bool] = ..., message: _Optional[str] = ..., new_key_metadata: _Optional[_Union[KeyMetadata, _Mapping]] = ...) -> None: ...

class ExportKeyRequest(_message.Message):
    __slots__ = ("name", "format", "wrapping_key_name")
    NAME_FIELD_NUMBER: _ClassVar[int]
    FORMAT_FIELD_NUMBER: _ClassVar[int]
    WRAPPING_KEY_NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    format: _common_pb2.KeyFormat
    wrapping_key_name: str
    def __init__(self, name: _Optional[str] = ..., format: _Optional[_Union[_common_pb2.KeyFormat, str]] = ..., wrapping_key_name: _Optional[str] = ...) -> None: ...

class ExportKeyResponse(_message.Message):
    __slots__ = ("key_material", "format", "key_metadata", "key_check_value")
    KEY_MATERIAL_FIELD_NUMBER: _ClassVar[int]
    FORMAT_FIELD_NUMBER: _ClassVar[int]
    KEY_METADATA_FIELD_NUMBER: _ClassVar[int]
    KEY_CHECK_VALUE_FIELD_NUMBER: _ClassVar[int]
    key_material: bytes
    format: _common_pb2.KeyFormat
    key_metadata: KeyMetadata
    key_check_value: bytes
    def __init__(self, key_material: _Optional[bytes] = ..., format: _Optional[_Union[_common_pb2.KeyFormat, str]] = ..., key_metadata: _Optional[_Union[KeyMetadata, _Mapping]] = ..., key_check_value: _Optional[bytes] = ...) -> None: ...

class ImportKeyRequest(_message.Message):
    __slots__ = ("name", "policy_name", "key_material", "format", "unwrapping_key_name", "provider_id", "provider_configuration", "template_id", "key_attestation")
    class ProviderConfigurationEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    POLICY_NAME_FIELD_NUMBER: _ClassVar[int]
    KEY_MATERIAL_FIELD_NUMBER: _ClassVar[int]
    FORMAT_FIELD_NUMBER: _ClassVar[int]
    UNWRAPPING_KEY_NAME_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_ID_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_CONFIGURATION_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    KEY_ATTESTATION_FIELD_NUMBER: _ClassVar[int]
    name: str
    policy_name: str
    key_material: bytes
    format: _common_pb2.KeyFormat
    unwrapping_key_name: str
    provider_id: str
    provider_configuration: _containers.ScalarMap[str, str]
    template_id: str
    key_attestation: bytes
    def __init__(self, name: _Optional[str] = ..., policy_name: _Optional[str] = ..., key_material: _Optional[bytes] = ..., format: _Optional[_Union[_common_pb2.KeyFormat, str]] = ..., unwrapping_key_name: _Optional[str] = ..., provider_id: _Optional[str] = ..., provider_configuration: _Optional[_Mapping[str, str]] = ..., template_id: _Optional[str] = ..., key_attestation: _Optional[bytes] = ...) -> None: ...

class ImportKeyResponse(_message.Message):
    __slots__ = ("success", "message", "key_metadata")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    KEY_METADATA_FIELD_NUMBER: _ClassVar[int]
    success: bool
    message: str
    key_metadata: KeyMetadata
    def __init__(self, success: _Optional[bool] = ..., message: _Optional[str] = ..., key_metadata: _Optional[_Union[KeyMetadata, _Mapping]] = ...) -> None: ...

class TransformKeyRequest(_message.Message):
    __slots__ = ("name", "retain_key_bytes", "scope_spec", "template_id")
    NAME_FIELD_NUMBER: _ClassVar[int]
    RETAIN_KEY_BYTES_FIELD_NUMBER: _ClassVar[int]
    SCOPE_SPEC_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    retain_key_bytes: bool
    scope_spec: _common_pb2.ScopeSpecification
    template_id: str
    def __init__(self, name: _Optional[str] = ..., retain_key_bytes: _Optional[bool] = ..., scope_spec: _Optional[_Union[_common_pb2.ScopeSpecification, _Mapping]] = ..., template_id: _Optional[str] = ...) -> None: ...

class TransformKeyResponse(_message.Message):
    __slots__ = ("success", "message", "key_metadata")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    KEY_METADATA_FIELD_NUMBER: _ClassVar[int]
    success: bool
    message: str
    key_metadata: KeyMetadata
    def __init__(self, success: _Optional[bool] = ..., message: _Optional[str] = ..., key_metadata: _Optional[_Union[KeyMetadata, _Mapping]] = ...) -> None: ...

class UpdateKeyPolicyRequest(_message.Message):
    __slots__ = ("name", "new_policy")
    NAME_FIELD_NUMBER: _ClassVar[int]
    NEW_POLICY_FIELD_NUMBER: _ClassVar[int]
    name: str
    new_policy: str
    def __init__(self, name: _Optional[str] = ..., new_policy: _Optional[str] = ...) -> None: ...

class UpdateKeyPolicyResponse(_message.Message):
    __slots__ = ("success", "message", "key_metadata")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    KEY_METADATA_FIELD_NUMBER: _ClassVar[int]
    success: bool
    message: str
    key_metadata: KeyMetadata
    def __init__(self, success: _Optional[bool] = ..., message: _Optional[str] = ..., key_metadata: _Optional[_Union[KeyMetadata, _Mapping]] = ...) -> None: ...

class MigrateKeyRequest(_message.Message):
    __slots__ = ("name", "target_instance_id", "provider_target", "strategy", "scope_spec", "template_id")
    NAME_FIELD_NUMBER: _ClassVar[int]
    TARGET_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_TARGET_FIELD_NUMBER: _ClassVar[int]
    STRATEGY_FIELD_NUMBER: _ClassVar[int]
    SCOPE_SPEC_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    target_instance_id: str
    provider_target: ProviderTarget
    strategy: MigrationStrategy
    scope_spec: _common_pb2.ScopeSpecification
    template_id: str
    def __init__(self, name: _Optional[str] = ..., target_instance_id: _Optional[str] = ..., provider_target: _Optional[_Union[ProviderTarget, _Mapping]] = ..., strategy: _Optional[_Union[MigrationStrategy, str]] = ..., scope_spec: _Optional[_Union[_common_pb2.ScopeSpecification, _Mapping]] = ..., template_id: _Optional[str] = ...) -> None: ...

class ProviderTarget(_message.Message):
    __slots__ = ("provider_id", "configuration")
    class ConfigurationEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    PROVIDER_ID_FIELD_NUMBER: _ClassVar[int]
    CONFIGURATION_FIELD_NUMBER: _ClassVar[int]
    provider_id: str
    configuration: _containers.ScalarMap[str, str]
    def __init__(self, provider_id: _Optional[str] = ..., configuration: _Optional[_Mapping[str, str]] = ...) -> None: ...

class MigrateKeyResponse(_message.Message):
    __slots__ = ("success", "message", "key_metadata", "archived_key_info", "result")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    KEY_METADATA_FIELD_NUMBER: _ClassVar[int]
    ARCHIVED_KEY_INFO_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    success: bool
    message: str
    key_metadata: KeyMetadata
    archived_key_info: ArchivedKeyInfo
    result: MigrationResult
    def __init__(self, success: _Optional[bool] = ..., message: _Optional[str] = ..., key_metadata: _Optional[_Union[KeyMetadata, _Mapping]] = ..., archived_key_info: _Optional[_Union[ArchivedKeyInfo, _Mapping]] = ..., result: _Optional[_Union[MigrationResult, _Mapping]] = ...) -> None: ...

class ArchivedKeyInfo(_message.Message):
    __slots__ = ("archived_key_name", "provider_id", "allowed_operations", "expiration_time")
    ARCHIVED_KEY_NAME_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_ID_FIELD_NUMBER: _ClassVar[int]
    ALLOWED_OPERATIONS_FIELD_NUMBER: _ClassVar[int]
    EXPIRATION_TIME_FIELD_NUMBER: _ClassVar[int]
    archived_key_name: str
    provider_id: str
    allowed_operations: _containers.RepeatedScalarFieldContainer[_common_pb2.CryptoOperation]
    expiration_time: _timestamp_pb2.Timestamp
    def __init__(self, archived_key_name: _Optional[str] = ..., provider_id: _Optional[str] = ..., allowed_operations: _Optional[_Iterable[_Union[_common_pb2.CryptoOperation, str]]] = ..., expiration_time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class MigrationResult(_message.Message):
    __slots__ = ("strategy_used", "key_bytes_preserved", "source_provider_id", "source_instance_id", "target_provider_id", "target_instance_id", "target_implementation", "wrapping_key_name")
    STRATEGY_USED_FIELD_NUMBER: _ClassVar[int]
    KEY_BYTES_PRESERVED_FIELD_NUMBER: _ClassVar[int]
    SOURCE_PROVIDER_ID_FIELD_NUMBER: _ClassVar[int]
    SOURCE_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    TARGET_PROVIDER_ID_FIELD_NUMBER: _ClassVar[int]
    TARGET_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    TARGET_IMPLEMENTATION_FIELD_NUMBER: _ClassVar[int]
    WRAPPING_KEY_NAME_FIELD_NUMBER: _ClassVar[int]
    strategy_used: MigrationStrategy
    key_bytes_preserved: bool
    source_provider_id: str
    source_instance_id: str
    target_provider_id: str
    target_instance_id: str
    target_implementation: _implementation_pb2.ImplementationProperties
    wrapping_key_name: str
    def __init__(self, strategy_used: _Optional[_Union[MigrationStrategy, str]] = ..., key_bytes_preserved: _Optional[bool] = ..., source_provider_id: _Optional[str] = ..., source_instance_id: _Optional[str] = ..., target_provider_id: _Optional[str] = ..., target_instance_id: _Optional[str] = ..., target_implementation: _Optional[_Union[_implementation_pb2.ImplementationProperties, _Mapping]] = ..., wrapping_key_name: _Optional[str] = ...) -> None: ...

class ValidateKeyOperationRequest(_message.Message):
    __slots__ = ("name", "transform", "migrate")
    NAME_FIELD_NUMBER: _ClassVar[int]
    TRANSFORM_FIELD_NUMBER: _ClassVar[int]
    MIGRATE_FIELD_NUMBER: _ClassVar[int]
    name: str
    transform: ValidateTransformIntent
    migrate: ValidateMigrateIntent
    def __init__(self, name: _Optional[str] = ..., transform: _Optional[_Union[ValidateTransformIntent, _Mapping]] = ..., migrate: _Optional[_Union[ValidateMigrateIntent, _Mapping]] = ...) -> None: ...

class ValidateTransformIntent(_message.Message):
    __slots__ = ("scope_spec", "template_id", "prefer_retain_bytes")
    SCOPE_SPEC_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    PREFER_RETAIN_BYTES_FIELD_NUMBER: _ClassVar[int]
    scope_spec: _common_pb2.ScopeSpecification
    template_id: str
    prefer_retain_bytes: bool
    def __init__(self, scope_spec: _Optional[_Union[_common_pb2.ScopeSpecification, _Mapping]] = ..., template_id: _Optional[str] = ..., prefer_retain_bytes: _Optional[bool] = ...) -> None: ...

class ValidateMigrateIntent(_message.Message):
    __slots__ = ("target_instance_id", "target_provider_id", "preferred_strategy")
    TARGET_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    TARGET_PROVIDER_ID_FIELD_NUMBER: _ClassVar[int]
    PREFERRED_STRATEGY_FIELD_NUMBER: _ClassVar[int]
    target_instance_id: str
    target_provider_id: str
    preferred_strategy: MigrationStrategy
    def __init__(self, target_instance_id: _Optional[str] = ..., target_provider_id: _Optional[str] = ..., preferred_strategy: _Optional[_Union[MigrationStrategy, str]] = ...) -> None: ...

class ValidateKeyOperationResponse(_message.Message):
    __slots__ = ("current_state", "options", "recommended_strategy", "recommendation_reason")
    CURRENT_STATE_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    RECOMMENDED_STRATEGY_FIELD_NUMBER: _ClassVar[int]
    RECOMMENDATION_REASON_FIELD_NUMBER: _ClassVar[int]
    current_state: KeyState
    options: _containers.RepeatedCompositeFieldContainer[StrategyOption]
    recommended_strategy: MigrationStrategy
    recommendation_reason: str
    def __init__(self, current_state: _Optional[_Union[KeyState, _Mapping]] = ..., options: _Optional[_Iterable[_Union[StrategyOption, _Mapping]]] = ..., recommended_strategy: _Optional[_Union[MigrationStrategy, str]] = ..., recommendation_reason: _Optional[str] = ...) -> None: ...

class KeyState(_message.Message):
    __slots__ = ("template_id", "provider_id", "instance_id", "extractable", "provider_type", "implementation")
    TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_ID_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    EXTRACTABLE_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_TYPE_FIELD_NUMBER: _ClassVar[int]
    IMPLEMENTATION_FIELD_NUMBER: _ClassVar[int]
    template_id: str
    provider_id: str
    instance_id: str
    extractable: bool
    provider_type: _providers_pb2.ProviderType
    implementation: _implementation_pb2.ImplementationProperties
    def __init__(self, template_id: _Optional[str] = ..., provider_id: _Optional[str] = ..., instance_id: _Optional[str] = ..., extractable: _Optional[bool] = ..., provider_type: _Optional[_Union[_providers_pb2.ProviderType, str]] = ..., implementation: _Optional[_Union[_implementation_pb2.ImplementationProperties, _Mapping]] = ...) -> None: ...

class StrategyOption(_message.Message):
    __slots__ = ("strategy", "feasible", "infeasibility_reason", "security_notes", "complexity_level")
    STRATEGY_FIELD_NUMBER: _ClassVar[int]
    FEASIBLE_FIELD_NUMBER: _ClassVar[int]
    INFEASIBILITY_REASON_FIELD_NUMBER: _ClassVar[int]
    SECURITY_NOTES_FIELD_NUMBER: _ClassVar[int]
    COMPLEXITY_LEVEL_FIELD_NUMBER: _ClassVar[int]
    strategy: MigrationStrategy
    feasible: bool
    infeasibility_reason: str
    security_notes: _containers.RepeatedScalarFieldContainer[str]
    complexity_level: int
    def __init__(self, strategy: _Optional[_Union[MigrationStrategy, str]] = ..., feasible: _Optional[bool] = ..., infeasibility_reason: _Optional[str] = ..., security_notes: _Optional[_Iterable[str]] = ..., complexity_level: _Optional[int] = ...) -> None: ...
