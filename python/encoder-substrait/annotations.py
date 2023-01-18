"""
Properties and utilities that affect how a query plan should execute.
"""


# ------------------------------
# Dependencies

# >> Standard classes
from dataclasses import dataclass

# >> Substrait protocol
#   |> low-level messages
from substrait.algebra_pb2.RelCommon.Hint import Stats


# ------------------------------
# Properties

# >> For relations
@dataclass
class RecordStats:
    """ Interface to RelCommon.Hint.Stats protobuf message. """
    count: int = 0
    size: int = 0

    def FillMessage(self, rel_msg):
        """
        Populates RelCommon.Hint.Stats properties of a relation message, :rel_msg:.

        Returns the relation message for convenience.
        """

        rel_msg.common.hint.stats.row_count   = self.count
        rel_msg.common.hint.stats.record_size = self.size

        return rel_msg


@dataclass
class ExecutionStats:
    """
    *Experimental* interface to RelCommon.Hint.ExecutionStats protobuf message.

    This message encapsulates information about whether the relation was executed and
    statistics about the execution. We would like to enable the following decisions:
        - has the execution been deferred (from a sub-plan)
        - should the execution be deferred (to a super-plan)
        - how has execution changed compared to previous executions

    Attributes:
        - executed: boolean of whether the sub-plan rooted at this relation was executed
        - runtime: total execution time (milliseconds) of the sub-plan rooted at this
                   relation
    """

    executed: bool = False
    runtime: int = 0

    def FillMessage(self, rel_msg):
        """
        Populates RelCommon.Hint.ExecutionStats properties of a relation message,
        :rel_msg:.

        Returns the relation message for convenience.
        """

        rel_msg.common.hint.execstats.executed = self.executed
        rel_msg.common.hint.execstats.runtime  = self.runtime

        return rel_msg

