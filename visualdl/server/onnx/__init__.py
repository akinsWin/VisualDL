from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import google.protobuf.message

from .onnx_pb2 import ModelProto


def load(obj):
    '''
    Loads a binary protobuf that stores onnx model

    @params
    Takes a file-like object (has "read" function)
    or a string containing a file name
    @return ONNX ModelProto object
    '''
    if hasattr(obj, 'read') and callable(obj.read):
        s = obj.read()
    else:
        with open(obj, 'rb') as f:
            s = f.read()
    return load_from_string(s)


def load_from_string(s):
    '''
    Loads a binary string that stores onnx model

    @params
    Takes a string object containing protobuf
    @return ONNX ModelProto object
    '''
    model = ModelProto()
    decoded = model.ParseFromString(s)
    # in python implementation ParseFromString returns None
    if decoded is not None and decoded != len(s):
        raise google.protobuf.message.DecodeError(
            "Protobuf decoding consumed too few bytes: {} out of {}".format(
                decoded, len(s)))
    return model
