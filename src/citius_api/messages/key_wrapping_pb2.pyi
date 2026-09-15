from citius_api.types import common_pb2 as _common_pb2
from citius_api.messages import metadata_pb2 as _metadata_pb2
from citius_api.messages import key_management_pb2 as _key_management_pb2
from citius_api.types import operation_params_pb2 as _operation_params_pb2
from citius_api.buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class WrapKeyRequest(_message.Message):
    __slots__ = ("key_to_wrap_name", "wrapping_key_name", "format", "no_params", "ka_wrap_params", "gost_wrap_params", "vendor_params", "user_context")
    class UserContextEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    KEY_TO_WRAP_NAME_FIELD_NUMBER: _ClassVar[int]
    WRAPPING_KEY_NAME_FIELD_NUMBER: _ClassVar[int]
    FORMAT_FIELD_NUMBER: _ClassVar[int]
    NO_PARAMS_FIELD_NUMBER: _ClassVar[int]
    KA_WRAP_PARAMS_FIELD_NUMBER: _ClassVar[int]
    GOST_WRAP_PARAMS_FIELD_NUMBER: _ClassVar[int]
    VENDOR_PARAMS_FIELD_NUMBER: _ClassVar[int]
    USER_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    key_to_wrap_name: str
    wrapping_key_name: str
    format: _common_pb2.WrapFormat
    no_params: _operation_params_pb2.NoParams
    ka_wrap_params: _operation_params_pb2.KeyAgreementWrapParams
    gost_wrap_params: _operation_params_pb2.GostWrapOperationParams
    vendor_params: _operation_params_pb2.VendorWrapParams
    user_context: _containers.ScalarMap[str, str]
    def __init__(self, key_to_wrap_name: _Optional[str] = ..., wrapping_key_name: _Optional[str] = ..., format: _Optional[_Union[_common_pb2.WrapFormat, str]] = ..., no_params: _Optional[_Union[_operation_params_pb2.NoParams, _Mapping]] = ..., ka_wrap_params: _Optional[_Union[_operation_params_pb2.KeyAgreementWrapParams, _Mapping]] = ..., gost_wrap_params: _Optional[_Union[_operation_params_pb2.GostWrapOperationParams, _Mapping]] = ..., vendor_params: _Optional[_Union[_operation_params_pb2.VendorWrapParams, _Mapping]] = ..., user_context: _Optional[_Mapping[str, str]] = ...) -> None: ...

class WrapKeyResponse(_message.Message):
    __slots__ = ("wrapped_key", "metadata")
    WRAPPED_KEY_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    wrapped_key: bytes
    metadata: _metadata_pb2.OperationMetadata
    def __init__(self, wrapped_key: _Optional[bytes] = ..., metadata: _Optional[_Union[_metadata_pb2.OperationMetadata, _Mapping]] = ...) -> None: ...

class UnwrapKeyRequest(_message.Message):
    __slots__ = ("wrapped_key", "wrapping_key_name", "unwrapped_key_name", "unwrapped_key_template_id", "format", "metadata", "no_params", "ka_wrap_params", "gost_wrap_params", "vendor_params", "user_context")
    class UserContextEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    WRAPPED_KEY_FIELD_NUMBER: _ClassVar[int]
    WRAPPING_KEY_NAME_FIELD_NUMBER: _ClassVar[int]
    UNWRAPPED_KEY_NAME_FIELD_NUMBER: _ClassVar[int]
    UNWRAPPED_KEY_TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    FORMAT_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    NO_PARAMS_FIELD_NUMBER: _ClassVar[int]
    KA_WRAP_PARAMS_FIELD_NUMBER: _ClassVar[int]
    GOST_WRAP_PARAMS_FIELD_NUMBER: _ClassVar[int]
    VENDOR_PARAMS_FIELD_NUMBER: _ClassVar[int]
    USER_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    wrapped_key: bytes
    wrapping_key_name: str
    unwrapped_key_name: str
    unwrapped_key_template_id: str
    format: _common_pb2.WrapFormat
    metadata: _metadata_pb2.OperationMetadata
    no_params: _operation_params_pb2.NoParams
    ka_wrap_params: _operation_params_pb2.KeyAgreementWrapParams
    gost_wrap_params: _operation_params_pb2.GostWrapOperationParams
    vendor_params: _operation_params_pb2.VendorWrapParams
    user_context: _containers.ScalarMap[str, str]
    def __init__(self, wrapped_key: _Optional[bytes] = ..., wrapping_key_name: _Optional[str] = ..., unwrapped_key_name: _Optional[str] = ..., unwrapped_key_template_id: _Optional[str] = ..., format: _Optional[_Union[_common_pb2.WrapFormat, str]] = ..., metadata: _Optional[_Union[_metadata_pb2.OperationMetadata, _Mapping]] = ..., no_params: _Optional[_Union[_operation_params_pb2.NoParams, _Mapping]] = ..., ka_wrap_params: _Optional[_Union[_operation_params_pb2.KeyAgreementWrapParams, _Mapping]] = ..., gost_wrap_params: _Optional[_Union[_operation_params_pb2.GostWrapOperationParams, _Mapping]] = ..., vendor_params: _Optional[_Union[_operation_params_pb2.VendorWrapParams, _Mapping]] = ..., user_context: _Optional[_Mapping[str, str]] = ...) -> None: ...

class UnwrapKeyResponse(_message.Message):
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
