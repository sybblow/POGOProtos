# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/platform/requests/plat_eight_request.proto

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
  name='pogoprotos/networking/platform/requests/plat_eight_request.proto',
  package='pogoprotos.networking.platform.requests',
  syntax='proto3',
  serialized_pb=_b('\n@pogoprotos/networking/platform/requests/plat_eight_request.proto\x12\'pogoprotos.networking.platform.requests\"\"\n\x10PlatEightRequest\x12\x0e\n\x06\x66ield1\x18\x01 \x01(\tb\x06proto3')
)




_PLATEIGHTREQUEST = _descriptor.Descriptor(
  name='PlatEightRequest',
  full_name='pogoprotos.networking.platform.requests.PlatEightRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='field1', full_name='pogoprotos.networking.platform.requests.PlatEightRequest.field1', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=109,
  serialized_end=143,
)

DESCRIPTOR.message_types_by_name['PlatEightRequest'] = _PLATEIGHTREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PlatEightRequest = _reflection.GeneratedProtocolMessageType('PlatEightRequest', (_message.Message,), dict(
  DESCRIPTOR = _PLATEIGHTREQUEST,
  __module__ = 'pogoprotos.networking.platform.requests.plat_eight_request_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.platform.requests.PlatEightRequest)
  ))
_sym_db.RegisterMessage(PlatEightRequest)


# @@protoc_insertion_point(module_scope)
