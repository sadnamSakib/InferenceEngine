import itertools


class TruthTable:
    def __init__(self, kb):
        self.kb = kb
        self.truth_table = []
        self.construct_truth_table()

    def conjunction(
        self, row, clause
    ):  ## row er proti ta variable er value true hole clause true basically and operation
        val = True
        for c in clause:
            if row[c] == False:
                val = False
                break
        return val

    def implication(self, a, b):  ## a implies b => a is false or b is true
        return not a or b

    def construct_truth_table(self):  # Generate the truth table

        variables = set()  # Set to store all variables in the knowledge base
        for clause in self.kb:
            variables.add(clause[1])  # Add the conclusion to the set
            variables.update(clause[0])  # Add all premises to the set

        # Sort variables for consistent order
        variables = sorted(variables)  # sort korlam

        combinations = list(itertools.product([False, True], repeat=len(variables)))
        ## itertools.product([False, True], repeat=len(variables)) er mane holo proti ta variable er jonno False and True er combination generate kora

        # proti ta combination er jonno ekta row banalam and oita truth table e dilam
        for combination in combinations:
            row = dict(zip(variables, combination))
            self.truth_table.append(row)

        print(self.truth_table[:5])

    def solve(
        self, query
    ):  # ei function e ekta query diye dibo and eta true or false hobe and true hoile koybar tru hoise sheta dekhabo
        entailment = 0
        for row in self.truth_table:  # proti row check korbo
            valid = True
            for clause in self.kb:  # ebar proti ta clause check korbo
                if clause[0]:  # jodi shekhane premise thake
                    valid = self.conjunction(row, clause[0])
                else:
                    valid = True
                valid = self.implication(valid, row[clause[1]])
                if not valid:
                    break
            if valid and row[query]:
                entailment += 1

        if entailment:
            print("YES: ", end="")
        else:
            print("NO: ", end="")
        print(entailment)
