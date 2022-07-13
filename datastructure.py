from enum import Enum, auto


class NODE_TYPE(Enum):
    DIGIT = auto()
    EQUATION = auto()
    OPERATION = auto()


class OP_PRIORITIES:
    PARENTHESIS = 1000
    MULTIPLY = 990
    DIVIDE = 990
    PLUS = 980
    MINUS = 980
    NONE = 0

    @staticmethod
    def get_priority(op):
        """
        Get the priority number of the specified operator.
        :param op: Operator string. eg) +, -, *, /
        :return: The priority number
        """
        if op == "(":
            pri = OP_PRIORITIES.PARENTHESIS
        elif op == "*":
            pri = OP_PRIORITIES.MULTIPLY
        elif op == "/":
            pri = OP_PRIORITIES.DIVIDE
        elif op == "+":
            pri = OP_PRIORITIES.PLUS
        elif op == "-":
            pri = OP_PRIORITIES.MINUS
        else:
            pri = OP_PRIORITIES.NONE

        return pri


class BTree:
    """
    Binary Tree class for a parser tree
    """
    def __init__(self, data, type, priority=OP_PRIORITIES.NONE, left=None, right=None, parent=None):
        self.data = data
        self._left = left
        self._right = right
        self._parent = parent
        self.type = type
        self._priority = priority

    @property
    def left(self):
        return self._left

    @left.setter
    def left(self, node):
        self._left = node
        node._parent = self

    @property
    def right(self):
        return self._right

    @right.setter
    def right(self, node):
        self._right = node
        node._parent = self

    @property
    def priority(self):
        return self._priority

    @priority.setter
    def priority(self, data):
        self._parent = data

    @property
    def parent(self):
        """
        Get the parent node
        :return:
        """
        return self._parent

    @parent.setter
    def parent(self, data):
        """
        Set the parent node with
        :param data:
        :return:
        """
        self._parent = data

