from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AeadOutput(_message.Message):
    __slots__ = ("nonce", "tag_length_bytes")
    NONCE_FIELD_NUMBER: _ClassVar[int]
    TAG_LENGTH_BYTES_FIELD_NUMBER: _ClassVar[int]
    nonce: bytes
    tag_length_bytes: int
    def __init__(self, nonce: _Optional[bytes] = ..., tag_length_bytes: _Optional[int] = ...) -> None: ...

class BlockCipherOutput(_message.Message):
    __slots__ = ("iv",)
    IV_FIELD_NUMBER: _ClassVar[int]
    iv: bytes
    def __init__(self, iv: _Optional[bytes] = ...) -> None: ...

class CounterModeOutput(_message.Message):
    __slots__ = ("counter_block", "counter_bits")
    COUNTER_BLOCK_FIELD_NUMBER: _ClassVar[int]
    COUNTER_BITS_FIELD_NUMBER: _ClassVar[int]
    counter_block: bytes
    counter_bits: int
    def __init__(self, counter_block: _Optional[bytes] = ..., counter_bits: _Optional[int] = ...) -> None: ...

class StreamCipherOutput(_message.Message):
    __slots__ = ("nonce", "block_counter")
    NONCE_FIELD_NUMBER: _ClassVar[int]
    BLOCK_COUNTER_FIELD_NUMBER: _ClassVar[int]
    nonce: bytes
    block_counter: bytes
    def __init__(self, nonce: _Optional[bytes] = ..., block_counter: _Optional[bytes] = ...) -> None: ...

class KdfOutput(_message.Message):
    __slots__ = ("salt", "iv")
    SALT_FIELD_NUMBER: _ClassVar[int]
    IV_FIELD_NUMBER: _ClassVar[int]
    salt: bytes
    iv: bytes
    def __init__(self, salt: _Optional[bytes] = ..., iv: _Optional[bytes] = ...) -> None: ...

class NoAlgorithmOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class VendorOutput(_message.Message):
    __slots__ = ("parameters",)
    class ParametersEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: bytes
        def __init__(self, key: _Optional[str] = ..., value: _Optional[bytes] = ...) -> None: ...
    PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    parameters: _containers.ScalarMap[str, bytes]
    def __init__(self, parameters: _Optional[_Mapping[str, bytes]] = ...) -> None: ...

class ProviderOutput(_message.Message):
    __slots__ = ("no_output", "aead_output", "block_cipher_output", "counter_mode_output", "stream_cipher_output", "kdf_output", "vendor_output", "encoding")
    NO_OUTPUT_FIELD_NUMBER: _ClassVar[int]
    AEAD_OUTPUT_FIELD_NUMBER: _ClassVar[int]
    BLOCK_CIPHER_OUTPUT_FIELD_NUMBER: _ClassVar[int]
    COUNTER_MODE_OUTPUT_FIELD_NUMBER: _ClassVar[int]
    STREAM_CIPHER_OUTPUT_FIELD_NUMBER: _ClassVar[int]
    KDF_OUTPUT_FIELD_NUMBER: _ClassVar[int]
    VENDOR_OUTPUT_FIELD_NUMBER: _ClassVar[int]
    ENCODING_FIELD_NUMBER: _ClassVar[int]
    no_output: NoAlgorithmOutput
    aead_output: AeadOutput
    block_cipher_output: BlockCipherOutput
    counter_mode_output: CounterModeOutput
    stream_cipher_output: StreamCipherOutput
    kdf_output: KdfOutput
    vendor_output: VendorOutput
    encoding: str
    def __init__(self, no_output: _Optional[_Union[NoAlgorithmOutput, _Mapping]] = ..., aead_output: _Optional[_Union[AeadOutput, _Mapping]] = ..., block_cipher_output: _Optional[_Union[BlockCipherOutput, _Mapping]] = ..., counter_mode_output: _Optional[_Union[CounterModeOutput, _Mapping]] = ..., stream_cipher_output: _Optional[_Union[StreamCipherOutput, _Mapping]] = ..., kdf_output: _Optional[_Union[KdfOutput, _Mapping]] = ..., vendor_output: _Optional[_Union[VendorOutput, _Mapping]] = ..., encoding: _Optional[str] = ...) -> None: ...

class OperationMetadata(_message.Message):
    __slots__ = ("key_version", "provider_output", "api_version", "user_context")
    class UserContextEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    KEY_VERSION_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_OUTPUT_FIELD_NUMBER: _ClassVar[int]
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    USER_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    key_version: int
    provider_output: ProviderOutput
    api_version: str
    user_context: _containers.ScalarMap[str, str]
    def __init__(self, key_version: _Optional[int] = ..., provider_output: _Optional[_Union[ProviderOutput, _Mapping]] = ..., api_version: _Optional[str] = ..., user_context: _Optional[_Mapping[str, str]] = ...) -> None: ...
