class ForwardChaining:
    def __init__(self, kb):
        self.kb = kb
        self.facts = {}
        self.agenda = []
        self.entailed_symbols = []  # List to store entailed symbols
        self.initialize()

    def initialize(self):
        for clause in self.kb:
            if len(clause[0]) == 0:

                self.agenda.append(clause[1])

    def add_fact(self, fact):
        self.facts[fact] = True

    def forward_chaining(self):
        while self.agenda:
            fact = self.agenda.pop(0)
            if fact not in self.facts:
                self.add_fact(fact)
                self.entailed_symbols.append(fact)
                for clause in self.kb:
                    if fact in clause[0]:
                        clause[0].remove(fact)
                        if len(clause[0]) == 0:
                            self.agenda.append(clause[1])

    def solve(self, query):
        self.forward_chaining()
        if query in self.facts:
            print("YES: ", end=" ")
            for symbol in self.entailed_symbols:
                print(symbol + ",", end=" ")
            print()
        else:
            print("NO")
