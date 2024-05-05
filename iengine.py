import sys
from inputParser import InputParser
from truthTable import TruthTable


def main():
    testFile = sys.argv[1]  # test file er naam nilam
    method = sys.argv[2]  # method er naam nilam
    inputParser = InputParser(
        testFile
    )  # inputParser class er object banailam and constructor e testFile path pass kore dilam
    if method == "TT":  # method TT hole truth table class er object banailam
        tt = TruthTable(
            inputParser.construct_kb_tt()
        )  # inputParser.construct_kb_tt() method call korlam , ei method call korle basically knowledge base create hoy
        tt.solve(inputParser.ask_value)  # ask value pass kore solve method call korlam
    # else:
    #     print("Invalid method")
    #     exit(1)


if __name__ == "__main__":
    main()
