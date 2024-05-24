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
                self.agenda.append(
                    clause[1]
                )  # agenda list e shob conclusion gula append korsi karon amra jani je conclusion gula shotti jekhane kono premise nai , ekhane basically jeshob jinish true shegula thakbe
                # for example jodi shudhu a,b emne deya thake etar mane a,b egula shotti

    def add_fact(self, fact):
        self.facts[fact] = (
            True  # eta dictionary e fact gula store korar jonno,so eta track rakhbe je kon kon fact gula tru kora hoise
        )

    def forward_chaining(self):
        while self.agenda:  # agenda khali na howa prjnto loop cholbe
            fact = self.agenda.pop(
                0
            )  # ekekta agenda ke fact e nibo and agenda theke oita shoray dibo
            if (
                fact not in self.facts
            ):  # jodi ei fact ta already check na hoye thake , which means self.facts dictionary te na thake
                self.add_fact(fact)  # tokhon fact add korbo
                self.entailed_symbols.append(
                    fact
                )  # fact jehetu true amra jani so entailed symbol e oita add korbo karon eta amader pore lagbe onno clause gula ke true banaite
                for (
                    clause
                ) in (
                    self.kb
                ):  # ekhon abar prottekta clause check korbo knowledge base theke
                    if (
                        fact in clause[0]
                    ):  # jodi fact ta clause[0] er moddhe thake then oitare remove korbo
                        clause[0].remove(fact)
                        if len(clause[0]) == 0:
                            self.agenda.append(
                                clause[1]
                            )  # jehetu protibar fact gulake remove kortesi ekta porjaye jokhon kono clause er shob remove hoye jabe tar mane oi conclusion ta shotti so oita agenda te push korbo

    def solve(self, query):
        self.forward_chaining()
        if (
            query in self.facts
        ):  # jodi query thake self.facts e then print yes karon query ta shotti proman hoise
            print("YES: ", end=" ")
            for symbol in self.entailed_symbols:
                print(symbol + ",", end=" ")

        else:
            print("NO")
