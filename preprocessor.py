from tokenize import generate_tokens
from io import StringIO
from datastructure import BTree, NODE_TYPE, OP_PRIORITIES


def token_split(data:str):
    result = []
    tokens = generate_tokens(StringIO(data).readline)

    for _, value, _, _, _ in tokens:
        if value != "":
            result.append(value)

    return result


class Token:
    def __init__(self):
        self.__tokens = []
        self.__current = 0
        self.__len = 0

    def __init__(self, string):
        self.tokenizer(string)

    def tokenizer(self, string):
        self.__tokens = token_split(string)
        self.__current = 0
        self.__len = len(self.__tokens)

    def __len__(self):
        return self.__len

    def pop(self):
        if self.__current >= self.__len:
            return None

        t = self.__tokens[self.__current]
        self.__current += 1

        return t

    def unpop(self):
        self.__current -= 1

    def popEq(self):
        """
        return sub equation from the current position starting from 0 to the end of parenthesis.
        Assume that the given equation list is "123 + 456 ( 789 * 10 ^ 2 + 11 ) + 12" and position is 2 which means "456".
        popEq() is "( 789 * 10 ^ 2 + 11 )" in list type and the position moves to "12".
        If the current position is 4(means 789), the value is 10.
        The matter is "(".

        :return:
        """
        if self.__tokens[self.__current] == "(":
            sp = self.__current
            while self.pop() != ")":

                # if fail to find ")", the equestion is wrong.
                if self.__current >= len(self.__tokens):
                    return None
                pass
            return self.__tokens[sp:self.__current]
        else:
            return self.pop()


class Preprocessor:
    EQ_SEPRATORS = "( ) + - * /"
    EQ_OPERATORS = "+-*/"

    def __init__(self):
        self.__equation = ""
        self.result_eq = []
        self.root = None

    def get_equation(self):
        return self.__equation

    def set_equation(self, equation):
        self.__equation = equation

    def process(self, equation:str):
        # Initialize
        self.root = None

        self.__equation = equation.strip()
        if not self.is_valid(self.__equation):
            return None

        # tokens = self._split(equation)
        tokens = Token(self.__equation)
        cnt_tokens = len(tokens)
        self._make_parsertree(tokens, 0, cnt_tokens - 1)

        return self.root

    def _make_parsertree(self, tokens, start, end):
        current_node = self.root

        while True:
            c = tokens.pop()

            if c is None or c == "":
                break
            elif c == "(":
                pass
            elif c in self.EQ_OPERATORS:
                priority = OP_PRIORITIES.get_priority(c)
                node = BTree(c, NODE_TYPE.OPERATION, priority)

                # If this node is the first operator
                if self.root == current_node:
                    self.root = node
                    node.left = current_node
                elif current_node.parent.priority < priority:
                    current_node.parent.right = node
                    node.left = current_node
                else:
                    p = current_node.parent

                    # Find the lower or equal priority operators in ancestor tree.
                    while p.parent is not None and p.priority >= node.priority:
                        p = p.parent
                    # node transfer. new node becomes ancestor node.
                    node.parent = p.parent
                    node.left = p

                    # set new root
                    if p == self.root:
                        self.root = node

            elif c.isdigit():
                node = BTree(float(c), NODE_TYPE.DIGIT)
                if self.root is None:
                    self.root = node
                elif current_node.type == NODE_TYPE.OPERATION:  #   OP
                    current_node.right = node                   #  / \
                                                                # D   D(node)
                else:
                    raise RuntimeError("Invalid data : ", self.data)

            current_node = node

    def is_valid(self, equation):
        return True
