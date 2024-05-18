class InputParser:
    def __init__(self, fileName):
        self.testFile = fileName  # test file er naam nilam
        self.read_input()  # read_input method call korlam INPUT GULA READ KORTE
        self.extract_tell_values()  # TELL VALUE GULA EXTRACT KORLAM
        self.extract_ask_value()  # ASK VALUE / QUERY EXTRACT KORLAM
        self.extract_clauses()  # TELL VALUE THEKE PROTI TA CLAUSE KE ALADA KORLAM

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

    def construct_kb(
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
                if clause != "":
                    kb.append(([], clause))
        print(kb)
        return kb
