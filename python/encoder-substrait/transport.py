"""
Layer for communicating protobuf messages, including:
    - file system
    - networks
    - in-memory
"""


# ------------------------------
# Dependencies


# ------------------------------
# Communication mediums

# >> File systems

def FromFile(proto_msg, filepath):
    """
    Reads protobuf data from file at :filepath: and uses it to initialize :proto_msg:.
    This uses the `ParseFromString` function for deserialization. The :proto_msg: argument
    is assumed to be an instance, not a class.
    """

    with open(filepath, 'rb') as file_handle:
        file_data = file_handle.read()
        proto_msg.ParseFromString(file_data)

    return proto_msg


def ToFile(proto_msg, filepath):
    """
    Writes :proto_msg: data to file at :filepath:. This uses the `SerializeToString`
    function for serialization.
    """

    with open(filepath, 'wb') as file_handle:
        file_handle.write(proto_msg.SerializeToString())

    return proto_msg
