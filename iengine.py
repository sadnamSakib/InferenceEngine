import sys
from inputParser import InputParser
from truthTable import TruthTable
from forwardChaining import ForwardChaining
from backwardChaining import BackwardChaining


def main():
    testFile = sys.argv[1]  # test file er naam nilam
    method = sys.argv[2]  # method er naam nilam
    inputParser = InputParser(
        testFile
    )  # inputParser class er object banailam and constructor e testFile path pass kore dilam
    kb = inputParser.construct_kb()
    if method == "TT":  # method TT hole truth table class er object banailam
        tt = TruthTable(
            kb
        )  # kb method call korlam , ei method call korle basically knowledge base create hoy
        tt.solve(inputParser.ask_value)  # ask value pass kore solve method call korlam
    elif method == "FC":  # method TT hole truth table class er
        fc = ForwardChaining(kb)
        fc.solve(inputParser.ask_value)
    elif method == "BC":
        bc = BackwardChaining(kb)
        bc.solve(inputParser.ask_value)

    # else:
    #     print("Invalid method")
    #     exit(1)


if __name__ == "__main__":
    main()
