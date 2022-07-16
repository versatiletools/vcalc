from datastructure import NODE_TYPE
from preprocessor import Preprocessor


class Calculator:
    def __init__(self):
        self.equations = []
        self.results = []
        self.preproc = Preprocessor()

    def all_clear(self):
        """
        Clear all
        """
        self.equations.clear()
        self.results.clear()

    def clear_entry(self):
        pass

    def add_equation(self, equation):
        self.equations.append(equation)

    def calculate(self, equation):
        self.add_equation(self.preproc.process(equation))
        for eq in self.equations:
            self.results.append(self._calc(eq))

        return self.results

    # def calculate(self):
    #     for eq in self.equations:
    #         self.results.append(self._calc(eq))
    #
    #     return self.results

    def _calc(self, p_tree):
        left_value = 0
        right_value = 0

        # if node is a digit, just return it.
        if p_tree.type == NODE_TYPE.DIGIT:
            return p_tree.data

        if p_tree is None:
            return None

        # Get left value. If the left node is a operator, recursive call.
        if p_tree.left.type == NODE_TYPE.OPERATION:
            left_value = self._calc(p_tree.left)
        else:
            left_value = p_tree.left.data

        # Get right value. If the right node is a operator, recursive call.
        if p_tree.right.type == NODE_TYPE.OPERATION:
            right_value = self._calc(p_tree.right)
        else:
            right_value = p_tree.right.data

        # Calculate and return the result.
        return self.operation(left_value, right_value, p_tree.data)

    def operation(self, param1: float, param2: float, op: str) -> float:
        """

        :param param1:
        :param param2:
        :param op:
        :return:
        """
        if op == "+":
            return param1 + param2
        elif op == "-":
            return param1 - param2
        elif op == "*":
            return param1 * param2
        elif op == "/":
            return param1 / param2
        else:
            raise ValueError("Unidentified operation.")




