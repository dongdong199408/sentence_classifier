# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: label_classifier.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='label_classifier.proto',
  package='label_class',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x16label_classifier.proto\x12\x0blabel_class\"\x1e\n\x05Label\x12\x15\n\rlabel_message\x18\x01 \x01(\t\"L\n\x0bLabel_class\x12\x15\n\rlabel_message\x18\x01 \x01(\t\x12\x12\n\ntype_class\x18\x02 \x01(\t\x12\x12\n\nsimilarity\x18\x03 \x01(\x02\x32Q\n\tLabelType\x12\x44\n\x0eRun_classifier\x12\x12.label_class.Label\x1a\x18.label_class.Label_class\"\x00(\x01\x30\x01\x62\x06proto3')
)




_LABEL = _descriptor.Descriptor(
  name='Label',
  full_name='label_class.Label',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='label_message', full_name='label_class.Label.label_message', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=39,
  serialized_end=69,
)


_LABEL_CLASS = _descriptor.Descriptor(
  name='Label_class',
  full_name='label_class.Label_class',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='label_message', full_name='label_class.Label_class.label_message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type_class', full_name='label_class.Label_class.type_class', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='similarity', full_name='label_class.Label_class.similarity', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=71,
  serialized_end=147,
)

DESCRIPTOR.message_types_by_name['Label'] = _LABEL
DESCRIPTOR.message_types_by_name['Label_class'] = _LABEL_CLASS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Label = _reflection.GeneratedProtocolMessageType('Label', (_message.Message,), {
  'DESCRIPTOR' : _LABEL,
  '__module__' : 'label_classifier_pb2'
  # @@protoc_insertion_point(class_scope:label_class.Label)
  })
_sym_db.RegisterMessage(Label)

Label_class = _reflection.GeneratedProtocolMessageType('Label_class', (_message.Message,), {
  'DESCRIPTOR' : _LABEL_CLASS,
  '__module__' : 'label_classifier_pb2'
  # @@protoc_insertion_point(class_scope:label_class.Label_class)
  })
_sym_db.RegisterMessage(Label_class)



_LABELTYPE = _descriptor.ServiceDescriptor(
  name='LabelType',
  full_name='label_class.LabelType',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=149,
  serialized_end=230,
  methods=[
  _descriptor.MethodDescriptor(
    name='Run_classifier',
    full_name='label_class.LabelType.Run_classifier',
    index=0,
    containing_service=None,
    input_type=_LABEL,
    output_type=_LABEL_CLASS,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_LABELTYPE)

DESCRIPTOR.services_by_name['LabelType'] = _LABELTYPE

# @@protoc_insertion_point(module_scope)