"""
Interface to protobuf data structures.
"""


# ------------------------------
# Dependencies

# >> Internal
#   |> classes
from .annotations import RecordStats

# >> Substrait protocol
#   |> top-level messages
from substrait.algebra_pb2 import ReadRel

#   |> low-level messages
from substrait.algebra_pb2 import RelCommon

# >> Skytether extensions
from skytether.algebra_pb2 import SkyRel


# ------------------------------
# Message types

# >> Attributes shared between many relations
class BaseRelation:

    @classmethod
    def AsProjection(cls, stats=None):
        return cls(RelCommon.Emit, stats)

    @classmethod
    def AsRelation(cls, stats=None):
        return cls(RelCommon.Direct, stats)

    def __init__(self, kind, row_stats=None, **kwargs):
        """
        :kind: is `Emit` for projections and `Direct` otherwise.
        :row_stats: is a `RecordStats`
        """

        super().__init__(**kwargs)

        self.msg = RelCommon()
        self.msg.emit_kind = kind

        if row_stats is not None:
            self.msg.hint = RelCommon.Hint()
            self.msg.hint.stats = row_stats


# >> Read Relations (scan operators)
class ReadRelation:

    @classmethod
    def FromMessage(cls, readrel_msg):
        """
        Populates instance state from the protobuf message, :readrel_msg:.
        """

        print(readrel_msg)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def ToMessage(self):
        """
        Directly creates a protobuf message from instance state.
        """

        # TODO
        '''
        readrel_msg = ReadRel(
             common=RelCommon()
            ,extension_table=ExtensionTable(
                 detail=SkyRel(
                      domain=
                     ,partition=
                 )
             )
        )
        '''
        pass

if __name__ == '__main__':
    print('Testing protocol.py')

    test_rel = ReadRelation('test-relation')
    print(f'Relation name: {test_rel.relname}')
