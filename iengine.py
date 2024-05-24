import sys
from inputParser import InputParser
from truthTable import TruthTable
from forwardChaining import ForwardChaining
from backwardChaining import BackwardChaining
import psutil
import time


def get_memory_usage():
    process = psutil.Process()
    return process.memory_info().rss / (1024)  # Convert bytes to MB


def main():

    testFile = sys.argv[1]  # test file er naam nilam
    method = sys.argv[2]  # method er naam nilam
    inputParser = InputParser(
        testFile
    )  # inputParser class er object banailam and constructor e testFile path pass kore dilam
    kb = inputParser.construct_kb()
    ktb = inputParser.construct_kb_truth_table()
    start_time = time.perf_counter()
    start_mem = get_memory_usage()
    if method == "TT":  # method TT hole truth table class er object banailam
        tt = TruthTable(
            ktb
        )  # kb method call korlam , ei method call korle basically knowledge base create hoy
        tt.solve(inputParser.ask_value)  # ask value pass kore solve method call korlam
        end_time = time.perf_counter()
    elif method == "FC":  # method TT hole truth table class er
        fc = ForwardChaining(kb)
        fc.solve(inputParser.ask_value)
        end_time = time.perf_counter()
    elif method == "BC":
        bc = BackwardChaining(kb)
        bc.solve(inputParser.ask_value)
        end_time = time.perf_counter()
    else:
        print("Invalid method")
        exit(1)

    end_mem = get_memory_usage()
    print()
    print(f"Time taken for {method}: {end_time*1000 - start_time*1000} milliseconds")
    print(f"Memory usage: {end_mem - start_mem:.2f} KB")


if __name__ == "__main__":
    main()
