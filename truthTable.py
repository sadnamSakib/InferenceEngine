import itertools


class TruthTable:
    def __init__(self, kb):
        self.kb = kb
        self.truth_table = []
        self.construct_truth_table()

    def conjunction(self, row, clause):
        val = True
        for c in clause:
            if not row[c]:
                val = False
                break
        return val

    def implication(self, a, b):
        return not a or b

    def biconditional(self, a, b):
        return a == b

    def entail(self, row, clause):
        # Tokenize the clause
        tokens = self.parse_expression(clause)

        # Evaluate the tokenized expression
        return self.evaluate_expression(row, tokens)

    def parse_expression(self, expression):
        tokens = []
        i = 0

        while i < len(expression):

            if expression[i] in ["&", "~", "(", ")"]:
                tokens.append(expression[i])
                i += 1

            elif expression[i] == "||":
                tokens.append("||")
                i += 1
            elif expression[i] == "=>":
                tokens.append("=>")
                i += 1
            elif i + 2 < len(expression) and expression[i] == "<=>":
                tokens.append("<=>")
                i += 1
            else:
                var = []
                while i < len(expression) and expression[i].isalnum():
                    var.append(expression[i])
                    i += 1

                tokens.append("".join(var))

        return tokens

    def evaluate_expression(self, row, tokens):
        def get_value(token):
            if token in row:
                return row[token]
            elif token == "True":
                return True
            elif token == "False":
                return False
            else:
                raise ValueError(f"Unknown token: {token}")

        def precedence(op):
            if op == "~":
                return 3
            if op in ("&", "||"):
                return 2
            if op in ("=>", "<=>"):
                return 1
            return 0

        def apply_op(ops, values):

            op = ops.pop()
            if op == "~":
                values.append(not values.pop())
            else:
                right = values.pop()
                left = values.pop()
                if op == "&":
                    values.append(left and right)
                elif op == "||":
                    values.append(left or right)
                elif op == "=>":
                    values.append(self.implication(left, right))
                elif op == "<=>":
                    values.append(self.biconditional(left, right))

        ops = []
        values = []
        i = 0
        while i < len(tokens):
            if tokens[i] == "(":
                ops.append(tokens[i])
            elif tokens[i] == ")":
                while ops and ops[-1] != "(":
                    apply_op(ops, values)
                ops.pop()
            elif tokens[i] in ["&", "||", "~", "=>", "<=>"]:
                while (
                    ops
                    and ops[-1] != "("
                    and precedence(ops[-1]) >= precedence(tokens[i])
                ):
                    apply_op(ops, values)
                ops.append(tokens[i])
            else:
                values.append(get_value(tokens[i]))
            i += 1

        while ops:
            apply_op(ops, values)

        return values[0]

    def construct_truth_table(self):
        variables = set()
        for clause in self.kb:
            variables.update(clause)

        variables = [var for var in variables if var.isalnum()]

        combinations = list(itertools.product([False, True], repeat=len(variables)))

        for combination in combinations:
            row = dict(zip(variables, combination))

            self.truth_table.append(row)

    def solve(self, query):
        entailment = 0

        for row in self.truth_table:

            valid = True
            for clause in self.kb:

                valid = self.entail(row, clause)
                if not valid:
                    break
            if valid and self.entail(row, query):
                entailment += 1

        if entailment:
            print("YES: ", end="")
        else:
            print("NO: ", end="")
        print(entailment)


# Example usage
