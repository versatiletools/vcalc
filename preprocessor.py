
class Preprocessor:
    EQ_SEPRATORS = "( ) + - * /"
    EQ_OPERATORS = "+-*/"

    def __init__(self):
        self.equation = ""
        self.result_eq = []

    def get_equation(self):
        return self.__equation

    def set_equation(self, equation):
        pass

    def process(self, equation):
        result_eq = []
        self.equation = equation

        if not self.is_valid(equation):
            return None

        tokens = self._split(equation)
        cnt_tokens = len(tokens)

        result_eq = self._make_postorder(tokens, 0, cnt_tokens - 1)

        return result_eq

    def _split(self, eq):
        result = []
        size = len(eq)
        in_parenthesis = False
        i = 0

        while i < size:
            chunk = ""
            c = eq[i]

            if c == " ":
                continue
            elif c == "(":
                in_parenthesis = True
                chunk = c
            elif c == ")":
                if in_parenthesis is False:
                    raise ValueError("Closing parenthesis without starting at {p}".format(i))
                else:
                    chunk = c
                    in_parenthesis = False
            elif c.isdigit():
                chunk = eq[i]
                j = i + 1
                if j < size - 1:
                    while eq[j].isdigit():
                        chunk += eq[j]
                        j += 1
                        if j > size - 1:
                            break
            else:
                chunk = c

            result.append(chunk)
            i += len(chunk)

        return result

    def _make_postorder(self, tokens, start, end):
        internal_eq = ["("]

        i = start
        while i < end:
            c = tokens[i]
            if c == "(":
                end_parenthesis = i
                # find end of the parenthesis
                while tokens[end_parenthesis] != ")":
                    end_parenthesis += 1
                # if fail to find it.
                if end_parenthesis > end:
                    return -1

                internal_eq += self._make_postorder(tokens, i + 1, end_parenthesis - 1)

                # jump to next to the end parenthesis
                i += end_parenthesis + 1
            elif c in self.EQ_OPERATORS:
                internal_eq.append(tokens[i+1])
                internal_eq.append(c)
                i += 2
            elif c.isdigit():
                internal_eq.append(tokens[i])      # the first operand
                internal_eq.append(tokens[i+2])    # the second operand
                internal_eq.append(tokens[i+1])    # operator
                i += 3

        internal_eq.append(")")

        return internal_eq

    def is_valid(self, equation):
        return True
