class InputParser:
    def __init__(self, fileName):
        self.testFile = fileName  # test file er naam nilam
        self.read_input()  # read_input method call korlam INPUT GULA READ KORTE
        self.extract_tell_values()  # TELL VALUE GULA EXTRACT KORLAM
        self.extract_ask_value()  # ASK VALUE / QUERY EXTRACT KORLAM
        self.extract_clauses()  # TELL VALUE THEKE PROTI TA CLAUSE KE ALADA KORLAM
        self.sort_clauses()  # CLAUSE GULA SORT KORLAM

    def read_input(
        self,
    ):  # BASICALLY PROTI TA LINE BY LINE READ KORE INPUT VARIABLE E RAKHLAM
        with open(self.testFile, "r") as file:
            self.input = file.read()
            file.close()

    def extract_tell_values(
        self,
    ):  # SECOND LINE E TELL VALUES ASE SO SECOND LINE NILAM AND MAJHER SHOB SPACING SHORAY DILAM
        lines = self.input.split("\n")
        self.tell_values = lines[1].strip().replace(" ", "")

    def extract_ask_value(
        self,
    ):  # FOURTH LINE E ASK VALUE ASE SO FOURTH LINE NILAM AND MAJHER SHOB SPACING SHORAY DILAM
        lines = self.input.split("\n")
        self.ask_value = lines[3].strip().replace(" ", "")

    def extract_clauses(
        self,
    ):  # TELL VALUE ER LINE E PROTI TA CLAUSE KE ALADA KORLAM BASED ON SEMI COLON KARON PROTI CLAUSE ER POR SEMI COLON ASE
        clauses = []
        self.clauses = self.tell_values.split(";")

    def sort_clauses(
        self,
    ):  # CLAUSE GULA SORT KORLAM BASED ON PREMISE SIZE(PREMISE MAANE => ER BAAMER VALUE)
        sorted_clauses = []
        sorted_clauses = sorted(
            self.clauses, key=lambda x: ("=>" in x, len(x.split("=>")[0]))
        )
        sorted_clauses = [clause for clause in sorted_clauses if clause]
        self.clauses = sorted_clauses  # EVABE SORT KORAR KARON HOCCHE AMRA AGE CHOTO SIZE ER PREMISE GULA SOLVE KORTE CHAI
        # ETA MAINLY LAGBE FORWARD CHAINING ER JONNO TRUTH TABLE E LAGBE NA

    # def construct_kb(self):
    #     kb = []
    #     for clause in self.clauses:  ## proti ta clause e iterate kortesi
    #         if (
    #             "=>" in clause
    #         ):  ## jodi => thake taile => er baamer gula premise and => er daaner gula conclusion
    #             split_clause = clause.split(
    #                 "=>"
    #             )  ## split korlam baamer and daaner part
    #             premise = split_clause[0].split(
    #                 "&"
    #             )  ## premise er majhe and thakle protita premise variable keo alada korlam
    #             conclusion = split_clause[1]  # conclusion ke alada korlam
    #             for (
    #                 p
    #             ) in (
    #                 premise
    #             ):  # premise er proti ta variable ke knowledge base a append korlam with conclusion
    #                 kb.append((p, conclusion))
    #         else:
    #             kb.append((clause, clause))  # => na thakle premise and conclusion same
    #     return kb

    # def construct_kb_fc(self):
    #     kb = []
    #     for clause in self.clauses:
    #         if "=>" in clause:
    #             split_clause = clause.split("=>")
    #             premise = split_clause[0].split("&")
    #             conclusion = split_clause[1]
    #             kb.append((premise, conclusion))
    #         else:
    #             kb.append(([], clause))
    #     return kb

    # def construct_kb_bc(self):
    #     kb = {}
    #     for clause in self.clauses:
    #         if "=>" in clause:
    #             split_clause = clause.split("=>")
    #             premise = split_clause[0].split("&")
    #             conclusion = split_clause[1]
    #             if conclusion in kb:
    #                 kb[conclusion].append(premise)
    #             else:
    #                 kb[conclusion] = [premise]
    #         else:
    #             if clause in kb:
    #                 kb[clause].append([])
    #             else:
    #                 kb[clause] = [[]]
    #     return kb

    def construct_kb_tt(
        self,
    ):  ## EI METHOD KNOWLEDGE BASE CREATE KORE , KNOWLEDGE BASE E PREMISE AND CONCLUSIONS KEMNE THAKBE SHETA DEFINE KORE
        kb = []
        for clause in self.clauses:  ## proti ta clause e iterate kortesi
            if "=>" in clause:  # jodi => sign thake
                split_clause = clause.split(
                    "=>"
                )  # tokhon => er daaner ta conclusion and baamer ta premise
                premise = split_clause[0].split(
                    "&"
                )  # premise er proti ta variable abar alda kortesi
                conclusion = split_clause[1]  # conclusion ke alada korlam
                kb.append((premise, conclusion))  # knowledge base e append korlam
            else:
                kb.append(
                    ([], clause)
                )  # => sign na thakle only conclusion rakhsi premise nai
        return kb
