import importlib
import os
from colorama import Fore, Style, init

from framework.runner import run_all
from framework.reporter import save_report

init(autoreset=True)
def load_tests():

    for file in os.listdir("tests"):

        if file.startswith("test_"):

            importlib.import_module(f"tests.{file[:-3]}")

def print_result(result):
    if result.success:
        status = Fore.GREEN + "PASS"
    else:
        status = Fore.RED + "FAIL"

    print(f"{status} | {result.name} | {result.duration}s | {result.message}")


def main():

    load_tests()

    results = run_all()

    passed = 0

    for r in results:
      print_result(r)

      if r.success:
            passed += 1

    print("\nResumo:")
    print(f"{passed}/{len(results)} passaram")

    report_file = save_report(results)

    print(f"\nRelatório salvo em: {report_file}")


if __name__ == "__main__":
    main()