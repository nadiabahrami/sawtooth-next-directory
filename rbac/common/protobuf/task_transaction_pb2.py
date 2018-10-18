# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: task_transaction.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='task_transaction.proto',
  package='',
  syntax='proto3',
  serialized_pb=_b('\n\x16task_transaction.proto\"n\n\x13ProposeAddTaskOwner\x12\x13\n\x0bproposal_id\x18\x01 \x01(\t\x12\x0f\n\x07task_id\x18\x02 \x01(\t\x12\x0f\n\x07user_id\x18\x03 \x01(\t\x12\x0e\n\x06reason\x18\x04 \x01(\t\x12\x10\n\x08metadata\x18\x05 \x01(\t\"q\n\x16ProposeRemoveTaskOwner\x12\x13\n\x0bproposal_id\x18\x01 \x01(\t\x12\x0f\n\x07task_id\x18\x02 \x01(\t\x12\x0f\n\x07user_id\x18\x03 \x01(\t\x12\x0e\n\x06reason\x18\x04 \x01(\t\x12\x10\n\x08metadata\x18\x05 \x01(\t\"n\n\x13ProposeAddTaskAdmin\x12\x13\n\x0bproposal_id\x18\x01 \x01(\t\x12\x0f\n\x07task_id\x18\x02 \x01(\t\x12\x0f\n\x07user_id\x18\x03 \x01(\t\x12\x0e\n\x06reason\x18\x04 \x01(\t\x12\x10\n\x08metadata\x18\x05 \x01(\t\"q\n\x16ProposeRemoveTaskAdmin\x12\x13\n\x0bproposal_id\x18\x01 \x01(\t\x12\x0f\n\x07task_id\x18\x02 \x01(\t\x12\x0f\n\x07user_id\x18\x03 \x01(\t\x12\x0e\n\x06reason\x18\x04 \x01(\t\x12\x10\n\x08metadata\x18\x05 \x01(\t\"\\\n\x13\x43onfirmAddTaskOwner\x12\x13\n\x0bproposal_id\x18\x01 \x01(\t\x12\x0f\n\x07task_id\x18\x02 \x01(\t\x12\x0f\n\x07user_id\x18\x03 \x01(\t\x12\x0e\n\x06reason\x18\x04 \x01(\t\"_\n\x16\x43onfirmRemoveTaskOwner\x12\x13\n\x0bproposal_id\x18\x01 \x01(\t\x12\x0f\n\x07task_id\x18\x02 \x01(\t\x12\x0f\n\x07user_id\x18\x03 \x01(\t\x12\x0e\n\x06reason\x18\x04 \x01(\t\"\\\n\x13\x43onfirmAddTaskAdmin\x12\x13\n\x0bproposal_id\x18\x01 \x01(\t\x12\x0f\n\x07task_id\x18\x02 \x01(\t\x12\x0f\n\x07user_id\x18\x03 \x01(\t\x12\x0e\n\x06reason\x18\x04 \x01(\t\"_\n\x16\x43onfirmRemoveTaskAdmin\x12\x13\n\x0bproposal_id\x18\x01 \x01(\t\x12\x0f\n\x07task_id\x18\x02 \x01(\t\x12\x0f\n\x07user_id\x18\x03 \x01(\t\x12\x0e\n\x06reason\x18\x04 \x01(\t\"[\n\x12RejectAddTaskOwner\x12\x13\n\x0bproposal_id\x18\x01 \x01(\t\x12\x0f\n\x07task_id\x18\x02 \x01(\t\x12\x0f\n\x07user_id\x18\x03 \x01(\t\x12\x0e\n\x06reason\x18\x04 \x01(\t\"^\n\x15RejectRemoveTaskOwner\x12\x13\n\x0bproposal_id\x18\x01 \x01(\t\x12\x0f\n\x07task_id\x18\x02 \x01(\t\x12\x0f\n\x07user_id\x18\x03 \x01(\t\x12\x0e\n\x06reason\x18\x04 \x01(\t\"[\n\x12RejectAddTaskAdmin\x12\x13\n\x0bproposal_id\x18\x01 \x01(\t\x12\x0f\n\x07task_id\x18\x02 \x01(\t\x12\x0f\n\x07user_id\x18\x03 \x01(\t\x12\x0e\n\x06reason\x18\x04 \x01(\t\"^\n\x15RejectRemoveTaskAdmin\x12\x13\n\x0bproposal_id\x18\x01 \x01(\t\x12\x0f\n\x07task_id\x18\x02 \x01(\t\x12\x0f\n\x07user_id\x18\x03 \x01(\t\x12\x0e\n\x06reason\x18\x04 \x01(\t\"]\n\nCreateTask\x12\x0f\n\x07task_id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0e\n\x06\x61\x64mins\x18\x03 \x03(\t\x12\x0e\n\x06owners\x18\x04 \x03(\t\x12\x10\n\x08metadata\x18\x05 \x01(\t\"b\n\nUpdateTask\x12\x0f\n\x07task_id\x18\x01 \x01(\t\x12\x10\n\x08new_name\x18\x02 \x01(\t\x12\x1b\n\x13old_metadata_sha512\x18\x03 \x01(\t\x12\x14\n\x0cnew_metadata\x18\x04 \x01(\tb\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_PROPOSEADDTASKOWNER = _descriptor.Descriptor(
  name='ProposeAddTaskOwner',
  full_name='ProposeAddTaskOwner',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='proposal_id', full_name='ProposeAddTaskOwner.proposal_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='task_id', full_name='ProposeAddTaskOwner.task_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='user_id', full_name='ProposeAddTaskOwner.user_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='reason', full_name='ProposeAddTaskOwner.reason', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='metadata', full_name='ProposeAddTaskOwner.metadata', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=26,
  serialized_end=136,
)


_PROPOSEREMOVETASKOWNER = _descriptor.Descriptor(
  name='ProposeRemoveTaskOwner',
  full_name='ProposeRemoveTaskOwner',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='proposal_id', full_name='ProposeRemoveTaskOwner.proposal_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='task_id', full_name='ProposeRemoveTaskOwner.task_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='user_id', full_name='ProposeRemoveTaskOwner.user_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='reason', full_name='ProposeRemoveTaskOwner.reason', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='metadata', full_name='ProposeRemoveTaskOwner.metadata', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=138,
  serialized_end=251,
)


_PROPOSEADDTASKADMIN = _descriptor.Descriptor(
  name='ProposeAddTaskAdmin',
  full_name='ProposeAddTaskAdmin',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='proposal_id', full_name='ProposeAddTaskAdmin.proposal_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='task_id', full_name='ProposeAddTaskAdmin.task_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='user_id', full_name='ProposeAddTaskAdmin.user_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='reason', full_name='ProposeAddTaskAdmin.reason', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='metadata', full_name='ProposeAddTaskAdmin.metadata', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=253,
  serialized_end=363,
)


_PROPOSEREMOVETASKADMIN = _descriptor.Descriptor(
  name='ProposeRemoveTaskAdmin',
  full_name='ProposeRemoveTaskAdmin',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='proposal_id', full_name='ProposeRemoveTaskAdmin.proposal_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='task_id', full_name='ProposeRemoveTaskAdmin.task_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='user_id', full_name='ProposeRemoveTaskAdmin.user_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='reason', full_name='ProposeRemoveTaskAdmin.reason', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='metadata', full_name='ProposeRemoveTaskAdmin.metadata', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=365,
  serialized_end=478,
)


_CONFIRMADDTASKOWNER = _descriptor.Descriptor(
  name='ConfirmAddTaskOwner',
  full_name='ConfirmAddTaskOwner',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='proposal_id', full_name='ConfirmAddTaskOwner.proposal_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='task_id', full_name='ConfirmAddTaskOwner.task_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='user_id', full_name='ConfirmAddTaskOwner.user_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='reason', full_name='ConfirmAddTaskOwner.reason', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=480,
  serialized_end=572,
)


_CONFIRMREMOVETASKOWNER = _descriptor.Descriptor(
  name='ConfirmRemoveTaskOwner',
  full_name='ConfirmRemoveTaskOwner',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='proposal_id', full_name='ConfirmRemoveTaskOwner.proposal_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='task_id', full_name='ConfirmRemoveTaskOwner.task_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='user_id', full_name='ConfirmRemoveTaskOwner.user_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='reason', full_name='ConfirmRemoveTaskOwner.reason', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=574,
  serialized_end=669,
)


_CONFIRMADDTASKADMIN = _descriptor.Descriptor(
  name='ConfirmAddTaskAdmin',
  full_name='ConfirmAddTaskAdmin',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='proposal_id', full_name='ConfirmAddTaskAdmin.proposal_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='task_id', full_name='ConfirmAddTaskAdmin.task_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='user_id', full_name='ConfirmAddTaskAdmin.user_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='reason', full_name='ConfirmAddTaskAdmin.reason', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=671,
  serialized_end=763,
)


_CONFIRMREMOVETASKADMIN = _descriptor.Descriptor(
  name='ConfirmRemoveTaskAdmin',
  full_name='ConfirmRemoveTaskAdmin',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='proposal_id', full_name='ConfirmRemoveTaskAdmin.proposal_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='task_id', full_name='ConfirmRemoveTaskAdmin.task_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='user_id', full_name='ConfirmRemoveTaskAdmin.user_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='reason', full_name='ConfirmRemoveTaskAdmin.reason', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=765,
  serialized_end=860,
)


_REJECTADDTASKOWNER = _descriptor.Descriptor(
  name='RejectAddTaskOwner',
  full_name='RejectAddTaskOwner',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='proposal_id', full_name='RejectAddTaskOwner.proposal_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='task_id', full_name='RejectAddTaskOwner.task_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='user_id', full_name='RejectAddTaskOwner.user_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='reason', full_name='RejectAddTaskOwner.reason', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=862,
  serialized_end=953,
)


_REJECTREMOVETASKOWNER = _descriptor.Descriptor(
  name='RejectRemoveTaskOwner',
  full_name='RejectRemoveTaskOwner',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='proposal_id', full_name='RejectRemoveTaskOwner.proposal_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='task_id', full_name='RejectRemoveTaskOwner.task_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='user_id', full_name='RejectRemoveTaskOwner.user_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='reason', full_name='RejectRemoveTaskOwner.reason', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=955,
  serialized_end=1049,
)


_REJECTADDTASKADMIN = _descriptor.Descriptor(
  name='RejectAddTaskAdmin',
  full_name='RejectAddTaskAdmin',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='proposal_id', full_name='RejectAddTaskAdmin.proposal_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='task_id', full_name='RejectAddTaskAdmin.task_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='user_id', full_name='RejectAddTaskAdmin.user_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='reason', full_name='RejectAddTaskAdmin.reason', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1051,
  serialized_end=1142,
)


_REJECTREMOVETASKADMIN = _descriptor.Descriptor(
  name='RejectRemoveTaskAdmin',
  full_name='RejectRemoveTaskAdmin',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='proposal_id', full_name='RejectRemoveTaskAdmin.proposal_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='task_id', full_name='RejectRemoveTaskAdmin.task_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='user_id', full_name='RejectRemoveTaskAdmin.user_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='reason', full_name='RejectRemoveTaskAdmin.reason', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1144,
  serialized_end=1238,
)


_CREATETASK = _descriptor.Descriptor(
  name='CreateTask',
  full_name='CreateTask',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='task_id', full_name='CreateTask.task_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='CreateTask.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='admins', full_name='CreateTask.admins', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='owners', full_name='CreateTask.owners', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='metadata', full_name='CreateTask.metadata', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1240,
  serialized_end=1333,
)


_UPDATETASK = _descriptor.Descriptor(
  name='UpdateTask',
  full_name='UpdateTask',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='task_id', full_name='UpdateTask.task_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='new_name', full_name='UpdateTask.new_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='old_metadata_sha512', full_name='UpdateTask.old_metadata_sha512', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='new_metadata', full_name='UpdateTask.new_metadata', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1335,
  serialized_end=1433,
)

DESCRIPTOR.message_types_by_name['ProposeAddTaskOwner'] = _PROPOSEADDTASKOWNER
DESCRIPTOR.message_types_by_name['ProposeRemoveTaskOwner'] = _PROPOSEREMOVETASKOWNER
DESCRIPTOR.message_types_by_name['ProposeAddTaskAdmin'] = _PROPOSEADDTASKADMIN
DESCRIPTOR.message_types_by_name['ProposeRemoveTaskAdmin'] = _PROPOSEREMOVETASKADMIN
DESCRIPTOR.message_types_by_name['ConfirmAddTaskOwner'] = _CONFIRMADDTASKOWNER
DESCRIPTOR.message_types_by_name['ConfirmRemoveTaskOwner'] = _CONFIRMREMOVETASKOWNER
DESCRIPTOR.message_types_by_name['ConfirmAddTaskAdmin'] = _CONFIRMADDTASKADMIN
DESCRIPTOR.message_types_by_name['ConfirmRemoveTaskAdmin'] = _CONFIRMREMOVETASKADMIN
DESCRIPTOR.message_types_by_name['RejectAddTaskOwner'] = _REJECTADDTASKOWNER
DESCRIPTOR.message_types_by_name['RejectRemoveTaskOwner'] = _REJECTREMOVETASKOWNER
DESCRIPTOR.message_types_by_name['RejectAddTaskAdmin'] = _REJECTADDTASKADMIN
DESCRIPTOR.message_types_by_name['RejectRemoveTaskAdmin'] = _REJECTREMOVETASKADMIN
DESCRIPTOR.message_types_by_name['CreateTask'] = _CREATETASK
DESCRIPTOR.message_types_by_name['UpdateTask'] = _UPDATETASK

ProposeAddTaskOwner = _reflection.GeneratedProtocolMessageType('ProposeAddTaskOwner', (_message.Message,), dict(
  DESCRIPTOR = _PROPOSEADDTASKOWNER,
  __module__ = 'task_transaction_pb2'
  # @@protoc_insertion_point(class_scope:ProposeAddTaskOwner)
  ))
_sym_db.RegisterMessage(ProposeAddTaskOwner)

ProposeRemoveTaskOwner = _reflection.GeneratedProtocolMessageType('ProposeRemoveTaskOwner', (_message.Message,), dict(
  DESCRIPTOR = _PROPOSEREMOVETASKOWNER,
  __module__ = 'task_transaction_pb2'
  # @@protoc_insertion_point(class_scope:ProposeRemoveTaskOwner)
  ))
_sym_db.RegisterMessage(ProposeRemoveTaskOwner)

ProposeAddTaskAdmin = _reflection.GeneratedProtocolMessageType('ProposeAddTaskAdmin', (_message.Message,), dict(
  DESCRIPTOR = _PROPOSEADDTASKADMIN,
  __module__ = 'task_transaction_pb2'
  # @@protoc_insertion_point(class_scope:ProposeAddTaskAdmin)
  ))
_sym_db.RegisterMessage(ProposeAddTaskAdmin)

ProposeRemoveTaskAdmin = _reflection.GeneratedProtocolMessageType('ProposeRemoveTaskAdmin', (_message.Message,), dict(
  DESCRIPTOR = _PROPOSEREMOVETASKADMIN,
  __module__ = 'task_transaction_pb2'
  # @@protoc_insertion_point(class_scope:ProposeRemoveTaskAdmin)
  ))
_sym_db.RegisterMessage(ProposeRemoveTaskAdmin)

ConfirmAddTaskOwner = _reflection.GeneratedProtocolMessageType('ConfirmAddTaskOwner', (_message.Message,), dict(
  DESCRIPTOR = _CONFIRMADDTASKOWNER,
  __module__ = 'task_transaction_pb2'
  # @@protoc_insertion_point(class_scope:ConfirmAddTaskOwner)
  ))
_sym_db.RegisterMessage(ConfirmAddTaskOwner)

ConfirmRemoveTaskOwner = _reflection.GeneratedProtocolMessageType('ConfirmRemoveTaskOwner', (_message.Message,), dict(
  DESCRIPTOR = _CONFIRMREMOVETASKOWNER,
  __module__ = 'task_transaction_pb2'
  # @@protoc_insertion_point(class_scope:ConfirmRemoveTaskOwner)
  ))
_sym_db.RegisterMessage(ConfirmRemoveTaskOwner)

ConfirmAddTaskAdmin = _reflection.GeneratedProtocolMessageType('ConfirmAddTaskAdmin', (_message.Message,), dict(
  DESCRIPTOR = _CONFIRMADDTASKADMIN,
  __module__ = 'task_transaction_pb2'
  # @@protoc_insertion_point(class_scope:ConfirmAddTaskAdmin)
  ))
_sym_db.RegisterMessage(ConfirmAddTaskAdmin)

ConfirmRemoveTaskAdmin = _reflection.GeneratedProtocolMessageType('ConfirmRemoveTaskAdmin', (_message.Message,), dict(
  DESCRIPTOR = _CONFIRMREMOVETASKADMIN,
  __module__ = 'task_transaction_pb2'
  # @@protoc_insertion_point(class_scope:ConfirmRemoveTaskAdmin)
  ))
_sym_db.RegisterMessage(ConfirmRemoveTaskAdmin)

RejectAddTaskOwner = _reflection.GeneratedProtocolMessageType('RejectAddTaskOwner', (_message.Message,), dict(
  DESCRIPTOR = _REJECTADDTASKOWNER,
  __module__ = 'task_transaction_pb2'
  # @@protoc_insertion_point(class_scope:RejectAddTaskOwner)
  ))
_sym_db.RegisterMessage(RejectAddTaskOwner)

RejectRemoveTaskOwner = _reflection.GeneratedProtocolMessageType('RejectRemoveTaskOwner', (_message.Message,), dict(
  DESCRIPTOR = _REJECTREMOVETASKOWNER,
  __module__ = 'task_transaction_pb2'
  # @@protoc_insertion_point(class_scope:RejectRemoveTaskOwner)
  ))
_sym_db.RegisterMessage(RejectRemoveTaskOwner)

RejectAddTaskAdmin = _reflection.GeneratedProtocolMessageType('RejectAddTaskAdmin', (_message.Message,), dict(
  DESCRIPTOR = _REJECTADDTASKADMIN,
  __module__ = 'task_transaction_pb2'
  # @@protoc_insertion_point(class_scope:RejectAddTaskAdmin)
  ))
_sym_db.RegisterMessage(RejectAddTaskAdmin)

RejectRemoveTaskAdmin = _reflection.GeneratedProtocolMessageType('RejectRemoveTaskAdmin', (_message.Message,), dict(
  DESCRIPTOR = _REJECTREMOVETASKADMIN,
  __module__ = 'task_transaction_pb2'
  # @@protoc_insertion_point(class_scope:RejectRemoveTaskAdmin)
  ))
_sym_db.RegisterMessage(RejectRemoveTaskAdmin)

CreateTask = _reflection.GeneratedProtocolMessageType('CreateTask', (_message.Message,), dict(
  DESCRIPTOR = _CREATETASK,
  __module__ = 'task_transaction_pb2'
  # @@protoc_insertion_point(class_scope:CreateTask)
  ))
_sym_db.RegisterMessage(CreateTask)

UpdateTask = _reflection.GeneratedProtocolMessageType('UpdateTask', (_message.Message,), dict(
  DESCRIPTOR = _UPDATETASK,
  __module__ = 'task_transaction_pb2'
  # @@protoc_insertion_point(class_scope:UpdateTask)
  ))
_sym_db.RegisterMessage(UpdateTask)


# @@protoc_insertion_point(module_scope)
