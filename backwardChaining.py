class BackwardChaining:
    def __init__(self, kb):
        self.kb = kb
        self.entailed_symbols = []
        self.failed_symbols = []
        self.goal_stack = []

    def is_known(self, symbol):
        return symbol in self.entailed_symbols

    def has_failed(self, symbol):
        return symbol in self.failed_symbols

    def backward_chaining(self, query):
        if self.is_known(query):
            return True
        if self.has_failed(query):
            return False
        if query in self.goal_stack:
            return False  # Loop detected

        self.goal_stack.append(query)

        for clause in self.kb:
            premises, conclusion = clause
            if conclusion == query:
                all_premises_proven = True
                for premise in premises:
                    if not self.backward_chaining(premise):
                        all_premises_proven = False
                        break
                if all_premises_proven:
                    self.entailed_symbols.append(query)
                    self.goal_stack.pop()
                    return True

        self.failed_symbols.append(query)
        self.goal_stack.pop()
        return False

    def solve(self, query):
        result = self.backward_chaining(query)
        if result:
            print("YES: ", end=" ")
            for symbol in self.entailed_symbols:
                print(symbol + ",", end=" ")
        else:
            print("NO")
