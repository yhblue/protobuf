# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: message.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)




DESCRIPTOR = _descriptor.FileDescriptor(
  name='message.proto',
  package='',
  serialized_pb='\n\rmessage.proto\":\n\x08Hero_msg\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\x0f\n\x07point_x\x18\x02 \x02(\t\x12\x0f\n\x07point_y\x18\x03 \x02(\t')




_HERO_MSG = _descriptor.Descriptor(
  name='Hero_msg',
  full_name='Hero_msg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='Hero_msg.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='point_x', full_name='Hero_msg.point_x', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='point_y', full_name='Hero_msg.point_y', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
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
  extension_ranges=[],
  serialized_start=17,
  serialized_end=75,
)

DESCRIPTOR.message_types_by_name['Hero_msg'] = _HERO_MSG

class Hero_msg(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _HERO_MSG

  # @@protoc_insertion_point(class_scope:Hero_msg)


# @@protoc_insertion_point(module_scope)
