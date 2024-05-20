class BackwardChaining:
    def __init__(self, kb):
        self.kb = kb
        self.entailed_symbols = []
        self.failed_symbols = []
        self.goal_stack = []

    def is_known(self, symbol):
        return (
            symbol in self.entailed_symbols
        )  # symbol jodi entailed_symbols e thake tahole true return korbe karon tar mane symbol ta true

    def has_failed(self, symbol):
        return (
            symbol in self.failed_symbols
        )  # symbol jodi failed_symbols e thake tahole true return korbe karon tar mane symbol ta false

    def backward_chaining(self, query):
        if self.is_known(
            query
        ):  # jodi query ta entailed_symbols e thake tahole true return korbe
            return True
        if self.has_failed(
            query
        ):  # jodi query ta failed_symbols e thake tahole false return korbe
            return False
        if (
            query in self.goal_stack
        ):  # jodi query ta goal_stack e thake tahole false return korbe karon loop create hoise and symbol tar ar true howa possible na hoile etokhone hoye jaito
            return False  # Loop detected

        self.goal_stack.append(query)  # goal_stack e query ta append korlam

        for clause in self.kb:  # proti ta clause er upor loop chalabo
            premises, conclusion = clause  # premise ar conclusion alada korlam
            if conclusion == query:
                all_premises_proven = True
                for premise in premises:  # proti ta premise er upor loop chalabo
                    if not self.backward_chaining(
                        premise
                    ):  # recursively backward chaining chalabo prota premise er upor , jodi konon ekta false return kore tar mane kono ekta premise hoileo mittha hoise
                        all_premises_proven = False
                        break
                if (
                    all_premises_proven
                ):  # jodi shob shotti pai tahole ei conclusion ta shotti
                    self.entailed_symbols.append(
                        query
                    )  # entailed_symbols e query ta append korlam
                    self.goal_stack.pop()  # goal_stack er last element ta pop korlam
                    return True  # true return korlam

        self.failed_symbols.append(
            query
        )  # jodi kono ekta clause e shob premise shotti na pai tahole ei query ta failed_symbols e append korlam
        self.goal_stack.pop()  # goal_stack er last element ta pop korlam
        return False

    def solve(self, query):
        result = self.backward_chaining(
            query
        )  # backward chaining chalailam query er upor
        if result:
            print("YES: ", end=" ")
            for symbol in self.entailed_symbols:
                print(symbol + ",", end=" ")
        else:
            print("NO")
