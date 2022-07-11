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

    def _calc(self, equation):
        stack = []

        for i in equation:
            if i in Preprocessor.EQ_OPERATORS:
                op1 = float(stack.pop())
                op2 = float(stack.pop())
                value = self.operation(op1, op2, i)
                stack.append(value)
            elif i == ")":
                value = stack.pop()     # pop the last value
                stack.pop()             # remove '('
                stack.append(value)     # push the last value.
                                        # This means that '(' and ')' are removed.
            else:
                stack.append(i)

        return stack.pop()

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




