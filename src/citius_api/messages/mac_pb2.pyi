from citius_api.messages import metadata_pb2 as _metadata_pb2
from citius_api.types import operation_params_pb2 as _operation_params_pb2
from citius_api.buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GenerateMACRequest(_message.Message):
    __slots__ = ("key_name", "message", "no_params", "customizable_params", "vendor_params", "user_context")
    class UserContextEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    KEY_NAME_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    NO_PARAMS_FIELD_NUMBER: _ClassVar[int]
    CUSTOMIZABLE_PARAMS_FIELD_NUMBER: _ClassVar[int]
    VENDOR_PARAMS_FIELD_NUMBER: _ClassVar[int]
    USER_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    key_name: str
    message: bytes
    no_params: _operation_params_pb2.NoParams
    customizable_params: _operation_params_pb2.CustomizableMacParams
    vendor_params: _operation_params_pb2.VendorMacParams
    user_context: _containers.ScalarMap[str, str]
    def __init__(self, key_name: _Optional[str] = ..., message: _Optional[bytes] = ..., no_params: _Optional[_Union[_operation_params_pb2.NoParams, _Mapping]] = ..., customizable_params: _Optional[_Union[_operation_params_pb2.CustomizableMacParams, _Mapping]] = ..., vendor_params: _Optional[_Union[_operation_params_pb2.VendorMacParams, _Mapping]] = ..., user_context: _Optional[_Mapping[str, str]] = ...) -> None: ...

class GenerateMACResponse(_message.Message):
    __slots__ = ("mac", "metadata")
    MAC_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    mac: bytes
    metadata: _metadata_pb2.OperationMetadata
    def __init__(self, mac: _Optional[bytes] = ..., metadata: _Optional[_Union[_metadata_pb2.OperationMetadata, _Mapping]] = ...) -> None: ...

class VerifyMACRequest(_message.Message):
    __slots__ = ("key_name", "message", "mac", "metadata", "no_params", "customizable_params", "vendor_params", "user_context")
    class UserContextEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    KEY_NAME_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    MAC_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    NO_PARAMS_FIELD_NUMBER: _ClassVar[int]
    CUSTOMIZABLE_PARAMS_FIELD_NUMBER: _ClassVar[int]
    VENDOR_PARAMS_FIELD_NUMBER: _ClassVar[int]
    USER_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    key_name: str
    message: bytes
    mac: bytes
    metadata: _metadata_pb2.OperationMetadata
    no_params: _operation_params_pb2.NoParams
    customizable_params: _operation_params_pb2.CustomizableMacParams
    vendor_params: _operation_params_pb2.VendorMacParams
    user_context: _containers.ScalarMap[str, str]
    def __init__(self, key_name: _Optional[str] = ..., message: _Optional[bytes] = ..., mac: _Optional[bytes] = ..., metadata: _Optional[_Union[_metadata_pb2.OperationMetadata, _Mapping]] = ..., no_params: _Optional[_Union[_operation_params_pb2.NoParams, _Mapping]] = ..., customizable_params: _Optional[_Union[_operation_params_pb2.CustomizableMacParams, _Mapping]] = ..., vendor_params: _Optional[_Union[_operation_params_pb2.VendorMacParams, _Mapping]] = ..., user_context: _Optional[_Mapping[str, str]] = ...) -> None: ...

class VerifyMACResponse(_message.Message):
    __slots__ = ("valid", "metadata")
    VALID_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    valid: bool
    metadata: _metadata_pb2.OperationMetadata
    def __init__(self, valid: _Optional[bool] = ..., metadata: _Optional[_Union[_metadata_pb2.OperationMetadata, _Mapping]] = ...) -> None: ...

class GenerateMACInitRequest(_message.Message):
    __slots__ = ("key_name", "no_params", "customizable_params", "vendor_params", "user_context")
    class UserContextEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    KEY_NAME_FIELD_NUMBER: _ClassVar[int]
    NO_PARAMS_FIELD_NUMBER: _ClassVar[int]
    CUSTOMIZABLE_PARAMS_FIELD_NUMBER: _ClassVar[int]
    VENDOR_PARAMS_FIELD_NUMBER: _ClassVar[int]
    USER_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    key_name: str
    no_params: _operation_params_pb2.NoParams
    customizable_params: _operation_params_pb2.CustomizableMacParams
    vendor_params: _operation_params_pb2.VendorMacParams
    user_context: _containers.ScalarMap[str, str]
    def __init__(self, key_name: _Optional[str] = ..., no_params: _Optional[_Union[_operation_params_pb2.NoParams, _Mapping]] = ..., customizable_params: _Optional[_Union[_operation_params_pb2.CustomizableMacParams, _Mapping]] = ..., vendor_params: _Optional[_Union[_operation_params_pb2.VendorMacParams, _Mapping]] = ..., user_context: _Optional[_Mapping[str, str]] = ...) -> None: ...

class GenerateMACInitResponse(_message.Message):
    __slots__ = ("success", "operation_id")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    OPERATION_ID_FIELD_NUMBER: _ClassVar[int]
    success: bool
    operation_id: str
    def __init__(self, success: _Optional[bool] = ..., operation_id: _Optional[str] = ...) -> None: ...

class GenerateMACUpdateRequest(_message.Message):
    __slots__ = ("operation_id", "data_chunk")
    OPERATION_ID_FIELD_NUMBER: _ClassVar[int]
    DATA_CHUNK_FIELD_NUMBER: _ClassVar[int]
    operation_id: str
    data_chunk: bytes
    def __init__(self, operation_id: _Optional[str] = ..., data_chunk: _Optional[bytes] = ...) -> None: ...

class GenerateMACUpdateResponse(_message.Message):
    __slots__ = ("success",)
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    success: bool
    def __init__(self, success: _Optional[bool] = ...) -> None: ...

class GenerateMACFinalRequest(_message.Message):
    __slots__ = ("operation_id",)
    OPERATION_ID_FIELD_NUMBER: _ClassVar[int]
    operation_id: str
    def __init__(self, operation_id: _Optional[str] = ...) -> None: ...

class GenerateMACFinalResponse(_message.Message):
    __slots__ = ("mac", "metadata")
    MAC_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    mac: bytes
    metadata: _metadata_pb2.OperationMetadata
    def __init__(self, mac: _Optional[bytes] = ..., metadata: _Optional[_Union[_metadata_pb2.OperationMetadata, _Mapping]] = ...) -> None: ...

class VerifyMACInitRequest(_message.Message):
    __slots__ = ("key_name", "no_params", "customizable_params", "vendor_params", "metadata", "user_context")
    class UserContextEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    KEY_NAME_FIELD_NUMBER: _ClassVar[int]
    NO_PARAMS_FIELD_NUMBER: _ClassVar[int]
    CUSTOMIZABLE_PARAMS_FIELD_NUMBER: _ClassVar[int]
    VENDOR_PARAMS_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    USER_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    key_name: str
    no_params: _operation_params_pb2.NoParams
    customizable_params: _operation_params_pb2.CustomizableMacParams
    vendor_params: _operation_params_pb2.VendorMacParams
    metadata: _metadata_pb2.OperationMetadata
    user_context: _containers.ScalarMap[str, str]
    def __init__(self, key_name: _Optional[str] = ..., no_params: _Optional[_Union[_operation_params_pb2.NoParams, _Mapping]] = ..., customizable_params: _Optional[_Union[_operation_params_pb2.CustomizableMacParams, _Mapping]] = ..., vendor_params: _Optional[_Union[_operation_params_pb2.VendorMacParams, _Mapping]] = ..., metadata: _Optional[_Union[_metadata_pb2.OperationMetadata, _Mapping]] = ..., user_context: _Optional[_Mapping[str, str]] = ...) -> None: ...

class VerifyMACInitResponse(_message.Message):
    __slots__ = ("success", "operation_id")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    OPERATION_ID_FIELD_NUMBER: _ClassVar[int]
    success: bool
    operation_id: str
    def __init__(self, success: _Optional[bool] = ..., operation_id: _Optional[str] = ...) -> None: ...

class VerifyMACUpdateRequest(_message.Message):
    __slots__ = ("operation_id", "data_chunk")
    OPERATION_ID_FIELD_NUMBER: _ClassVar[int]
    DATA_CHUNK_FIELD_NUMBER: _ClassVar[int]
    operation_id: str
    data_chunk: bytes
    def __init__(self, operation_id: _Optional[str] = ..., data_chunk: _Optional[bytes] = ...) -> None: ...

class VerifyMACUpdateResponse(_message.Message):
    __slots__ = ("success",)
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    success: bool
    def __init__(self, success: _Optional[bool] = ...) -> None: ...

class VerifyMACFinalRequest(_message.Message):
    __slots__ = ("operation_id", "mac")
    OPERATION_ID_FIELD_NUMBER: _ClassVar[int]
    MAC_FIELD_NUMBER: _ClassVar[int]
    operation_id: str
    mac: bytes
    def __init__(self, operation_id: _Optional[str] = ..., mac: _Optional[bytes] = ...) -> None: ...

class VerifyMACFinalResponse(_message.Message):
    __slots__ = ("valid", "metadata")
    VALID_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    valid: bool
    metadata: _metadata_pb2.OperationMetadata
    def __init__(self, valid: _Optional[bool] = ..., metadata: _Optional[_Union[_metadata_pb2.OperationMetadata, _Mapping]] = ...) -> None: ...
