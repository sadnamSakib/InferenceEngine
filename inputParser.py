class InputParser:
    def __init__(self, fileName):
        self.testFile = fileName
        self.read_input()
        self.extract_tell_values()
        self.extract_ask_value()
        self.extract_clauses()

    def read_input(self):
        with open(self.testFile, "r") as file:
            self.input = file.read()

    def extract_tell_values(self):
        lines = self.input.split("\n")
        self.tell_values = lines[1].strip().replace(" ", "")

    def extract_ask_value(self):
        lines = self.input.split("\n")
        self.ask_value = lines[3].strip().replace(" ", "")

    def extract_clauses(self):
        self.clauses = self.tell_values.split(";")

    def construct_kb(self):
        kb = []
        for clause in self.clauses:

            if "=>" in clause:
                split_clause = clause.split("=>")
                premise = split_clause[0].split("&")
                conclusion = split_clause[1]
                kb.append((premise, conclusion))
            else:
                if clause != "":
                    kb.append(([], clause))

        return kb

    def construct_kb_truth_table(self):
        kb = []
        for clause in self.clauses:

            if len(clause) == 0:
                continue
            parsed_clause = self.parse_expression(clause)
            kb.append(parsed_clause)

        return kb

    def parse_expression(self, expression):
        tokens = []
        i = 0
        while i < len(expression):
            if expression[i] in ["&", "~", "(", ")"]:
                tokens.append(expression[i])
                i += 1
            elif expression[i] == "|":
                tokens.append("||")
                i += 2
            elif (
                expression[i] == "="
                and i + 1 < len(expression)
                and expression[i + 1] == ">"
            ):
                tokens.append("=>")
                i += 2
            elif (
                expression[i] == "<"
                and i + 2 < len(expression)
                and expression[i + 1] == "="
                and expression[i + 2] == ">"
            ):
                tokens.append("<=>")
                i += 3
            else:
                var = []
                while i < len(expression) and expression[i].isalnum():
                    var.append(expression[i])
                    i += 1
                tokens.append("".join(var))
        return tokens
