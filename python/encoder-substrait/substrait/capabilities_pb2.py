# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: substrait/capabilities.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1csubstrait/capabilities.proto\x12\tsubstrait\"\xec\x02\n\x0c\x43\x61pabilities\x12-\n\x12substrait_versions\x18\x01 \x03(\tR\x11substraitVersions\x12?\n\x1c\x61\x64vanced_extension_type_urls\x18\x02 \x03(\tR\x19\x61\x64vancedExtensionTypeUrls\x12T\n\x11simple_extensions\x18\x03 \x03(\x0b\x32\'.substrait.Capabilities.SimpleExtensionR\x10simpleExtensions\x1a\x95\x01\n\x0fSimpleExtension\x12\x10\n\x03uri\x18\x01 \x01(\tR\x03uri\x12#\n\rfunction_keys\x18\x02 \x03(\tR\x0c\x66unctionKeys\x12\x1b\n\ttype_keys\x18\x03 \x03(\tR\x08typeKeys\x12.\n\x13type_variation_keys\x18\x04 \x03(\tR\x11typeVariationKeysBW\n\x12io.substrait.protoP\x01Z*github.com/substrait-io/substrait-go/proto\xaa\x02\x12Substrait.Protobufb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'substrait.capabilities_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\022io.substrait.protoP\001Z*github.com/substrait-io/substrait-go/proto\252\002\022Substrait.Protobuf'
  _CAPABILITIES._serialized_start=44
  _CAPABILITIES._serialized_end=408
  _CAPABILITIES_SIMPLEEXTENSION._serialized_start=259
  _CAPABILITIES_SIMPLEEXTENSION._serialized_end=408
# @@protoc_insertion_point(module_scope)
