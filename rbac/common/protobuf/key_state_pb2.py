# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: key_state.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='key_state.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x0fkey_state.proto\"\"\n\x0cKeyContainer\x12\x12\n\x04keys\x18\x02 \x03(\x0b\x32\x04.Key\"&\n\x03Key\x12\x0e\n\x06key_id\x18\x01 \x01(\t\x12\x0f\n\x07next_id\x18\x02 \x01(\tb\x06proto3')
)




_KEYCONTAINER = _descriptor.Descriptor(
  name='KeyContainer',
  full_name='KeyContainer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='keys', full_name='KeyContainer.keys', index=0,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=19,
  serialized_end=53,
)


_KEY = _descriptor.Descriptor(
  name='Key',
  full_name='Key',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key_id', full_name='Key.key_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='next_id', full_name='Key.next_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=55,
  serialized_end=93,
)

_KEYCONTAINER.fields_by_name['keys'].message_type = _KEY
DESCRIPTOR.message_types_by_name['KeyContainer'] = _KEYCONTAINER
DESCRIPTOR.message_types_by_name['Key'] = _KEY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

KeyContainer = _reflection.GeneratedProtocolMessageType('KeyContainer', (_message.Message,), dict(
  DESCRIPTOR = _KEYCONTAINER,
  __module__ = 'key_state_pb2'
  # @@protoc_insertion_point(class_scope:KeyContainer)
  ))
_sym_db.RegisterMessage(KeyContainer)

Key = _reflection.GeneratedProtocolMessageType('Key', (_message.Message,), dict(
  DESCRIPTOR = _KEY,
  __module__ = 'key_state_pb2'
  # @@protoc_insertion_point(class_scope:Key)
  ))
_sym_db.RegisterMessage(Key)


# @@protoc_insertion_point(module_scope)
