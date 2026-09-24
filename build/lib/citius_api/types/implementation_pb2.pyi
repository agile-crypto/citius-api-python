import datetime

from google.protobuf import timestamp_pb2 as _timestamp_pb2
from citius_api.buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Fips140Level(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    FIPS_140_LEVEL_UNSPECIFIED: _ClassVar[Fips140Level]
    FIPS_140_LEVEL_1: _ClassVar[Fips140Level]
    FIPS_140_LEVEL_2: _ClassVar[Fips140Level]
    FIPS_140_LEVEL_3: _ClassVar[Fips140Level]
    FIPS_140_LEVEL_4: _ClassVar[Fips140Level]
FIPS_140_LEVEL_UNSPECIFIED: Fips140Level
FIPS_140_LEVEL_1: Fips140Level
FIPS_140_LEVEL_2: Fips140Level
FIPS_140_LEVEL_3: Fips140Level
FIPS_140_LEVEL_4: Fips140Level

class ImplementationProperties(_message.Message):
    __slots__ = ("fips_140", "common_criteria_certified", "audits", "formally_verified", "verification_framework", "memory_safe_language", "implementation_language", "constant_time", "side_channel_hardened", "hardware_accelerated", "hardware_features", "no_known_cve", "unpatched_cves", "additional")
    class AdditionalEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    FIPS_140_FIELD_NUMBER: _ClassVar[int]
    COMMON_CRITERIA_CERTIFIED_FIELD_NUMBER: _ClassVar[int]
    AUDITS_FIELD_NUMBER: _ClassVar[int]
    FORMALLY_VERIFIED_FIELD_NUMBER: _ClassVar[int]
    VERIFICATION_FRAMEWORK_FIELD_NUMBER: _ClassVar[int]
    MEMORY_SAFE_LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    IMPLEMENTATION_LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    CONSTANT_TIME_FIELD_NUMBER: _ClassVar[int]
    SIDE_CHANNEL_HARDENED_FIELD_NUMBER: _ClassVar[int]
    HARDWARE_ACCELERATED_FIELD_NUMBER: _ClassVar[int]
    HARDWARE_FEATURES_FIELD_NUMBER: _ClassVar[int]
    NO_KNOWN_CVE_FIELD_NUMBER: _ClassVar[int]
    UNPATCHED_CVES_FIELD_NUMBER: _ClassVar[int]
    ADDITIONAL_FIELD_NUMBER: _ClassVar[int]
    fips_140: Fips140Certification
    common_criteria_certified: bool
    audits: _containers.RepeatedCompositeFieldContainer[AuditReport]
    formally_verified: bool
    verification_framework: str
    memory_safe_language: bool
    implementation_language: str
    constant_time: bool
    side_channel_hardened: bool
    hardware_accelerated: bool
    hardware_features: _containers.RepeatedScalarFieldContainer[str]
    no_known_cve: bool
    unpatched_cves: _containers.RepeatedScalarFieldContainer[str]
    additional: _containers.ScalarMap[str, str]
    def __init__(self, fips_140: _Optional[_Union[Fips140Certification, _Mapping]] = ..., common_criteria_certified: _Optional[bool] = ..., audits: _Optional[_Iterable[_Union[AuditReport, _Mapping]]] = ..., formally_verified: _Optional[bool] = ..., verification_framework: _Optional[str] = ..., memory_safe_language: _Optional[bool] = ..., implementation_language: _Optional[str] = ..., constant_time: _Optional[bool] = ..., side_channel_hardened: _Optional[bool] = ..., hardware_accelerated: _Optional[bool] = ..., hardware_features: _Optional[_Iterable[str]] = ..., no_known_cve: _Optional[bool] = ..., unpatched_cves: _Optional[_Iterable[str]] = ..., additional: _Optional[_Mapping[str, str]] = ...) -> None: ...

class Fips140Certification(_message.Message):
    __slots__ = ("certified", "level", "certificate_number", "module_name", "validation_date", "expiration_date")
    CERTIFIED_FIELD_NUMBER: _ClassVar[int]
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    CERTIFICATE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    MODULE_NAME_FIELD_NUMBER: _ClassVar[int]
    VALIDATION_DATE_FIELD_NUMBER: _ClassVar[int]
    EXPIRATION_DATE_FIELD_NUMBER: _ClassVar[int]
    certified: bool
    level: Fips140Level
    certificate_number: str
    module_name: str
    validation_date: _timestamp_pb2.Timestamp
    expiration_date: _timestamp_pb2.Timestamp
    def __init__(self, certified: _Optional[bool] = ..., level: _Optional[_Union[Fips140Level, str]] = ..., certificate_number: _Optional[str] = ..., module_name: _Optional[str] = ..., validation_date: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., expiration_date: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class AuditReport(_message.Message):
    __slots__ = ("auditor", "report_date", "report_id", "scope", "findings_summary", "report_url")
    AUDITOR_FIELD_NUMBER: _ClassVar[int]
    REPORT_DATE_FIELD_NUMBER: _ClassVar[int]
    REPORT_ID_FIELD_NUMBER: _ClassVar[int]
    SCOPE_FIELD_NUMBER: _ClassVar[int]
    FINDINGS_SUMMARY_FIELD_NUMBER: _ClassVar[int]
    REPORT_URL_FIELD_NUMBER: _ClassVar[int]
    auditor: str
    report_date: _timestamp_pb2.Timestamp
    report_id: str
    scope: str
    findings_summary: str
    report_url: str
    def __init__(self, auditor: _Optional[str] = ..., report_date: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., report_id: _Optional[str] = ..., scope: _Optional[str] = ..., findings_summary: _Optional[str] = ..., report_url: _Optional[str] = ...) -> None: ...

class ProviderTemplateSupport(_message.Message):
    __slots__ = ("template_id", "implementation", "notes", "disabled")
    TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    IMPLEMENTATION_FIELD_NUMBER: _ClassVar[int]
    NOTES_FIELD_NUMBER: _ClassVar[int]
    DISABLED_FIELD_NUMBER: _ClassVar[int]
    template_id: str
    implementation: ImplementationProperties
    notes: str
    disabled: bool
    def __init__(self, template_id: _Optional[str] = ..., implementation: _Optional[_Union[ImplementationProperties, _Mapping]] = ..., notes: _Optional[str] = ..., disabled: _Optional[bool] = ...) -> None: ...

class ProviderRequirements(_message.Message):
    __slots__ = ("fips_140_certified", "min_fips_level", "common_criteria_certified", "formally_verified", "memory_safe", "constant_time", "side_channel_hardened", "no_known_cve", "prefer_hardware_accelerated", "additional")
    class AdditionalEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    FIPS_140_CERTIFIED_FIELD_NUMBER: _ClassVar[int]
    MIN_FIPS_LEVEL_FIELD_NUMBER: _ClassVar[int]
    COMMON_CRITERIA_CERTIFIED_FIELD_NUMBER: _ClassVar[int]
    FORMALLY_VERIFIED_FIELD_NUMBER: _ClassVar[int]
    MEMORY_SAFE_FIELD_NUMBER: _ClassVar[int]
    CONSTANT_TIME_FIELD_NUMBER: _ClassVar[int]
    SIDE_CHANNEL_HARDENED_FIELD_NUMBER: _ClassVar[int]
    NO_KNOWN_CVE_FIELD_NUMBER: _ClassVar[int]
    PREFER_HARDWARE_ACCELERATED_FIELD_NUMBER: _ClassVar[int]
    ADDITIONAL_FIELD_NUMBER: _ClassVar[int]
    fips_140_certified: bool
    min_fips_level: Fips140Level
    common_criteria_certified: bool
    formally_verified: bool
    memory_safe: bool
    constant_time: bool
    side_channel_hardened: bool
    no_known_cve: bool
    prefer_hardware_accelerated: bool
    additional: _containers.ScalarMap[str, str]
    def __init__(self, fips_140_certified: _Optional[bool] = ..., min_fips_level: _Optional[_Union[Fips140Level, str]] = ..., common_criteria_certified: _Optional[bool] = ..., formally_verified: _Optional[bool] = ..., memory_safe: _Optional[bool] = ..., constant_time: _Optional[bool] = ..., side_channel_hardened: _Optional[bool] = ..., no_known_cve: _Optional[bool] = ..., prefer_hardware_accelerated: _Optional[bool] = ..., additional: _Optional[_Mapping[str, str]] = ...) -> None: ...

class ProviderInstance(_message.Message):
    __slots__ = ("instance_id", "provider_id", "display_name", "description", "configuration", "disabled", "implementation_override")
    class ConfigurationEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_ID_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CONFIGURATION_FIELD_NUMBER: _ClassVar[int]
    DISABLED_FIELD_NUMBER: _ClassVar[int]
    IMPLEMENTATION_OVERRIDE_FIELD_NUMBER: _ClassVar[int]
    instance_id: str
    provider_id: str
    display_name: str
    description: str
    configuration: _containers.ScalarMap[str, str]
    disabled: bool
    implementation_override: ImplementationProperties
    def __init__(self, instance_id: _Optional[str] = ..., provider_id: _Optional[str] = ..., display_name: _Optional[str] = ..., description: _Optional[str] = ..., configuration: _Optional[_Mapping[str, str]] = ..., disabled: _Optional[bool] = ..., implementation_override: _Optional[_Union[ImplementationProperties, _Mapping]] = ...) -> None: ...
