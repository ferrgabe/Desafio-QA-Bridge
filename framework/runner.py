import time
from concurrent.futures import ThreadPoolExecutor, TimeoutError
from framework.decorators import TEST_REGISTRY
from framework.result import TestResult

def run_single_test(test):

    name = test["name"]
    func = test["func"]
    timeout = test["timeout"]

    start = time.time()

    with ThreadPoolExecutor(max_workers=1) as executor:

        future = executor.submit(func)

        try:

            future.result(timeout=timeout)

            duration = round(time.time() - start, 2)

            return TestResult(name, True, duration)

        except TimeoutError:

            return TestResult(name, False, timeout, "Timeout")

        except Exception as e:

            duration = round(time.time() - start, 2)

            return TestResult(name, False, duration, str(e))


def run_all():

    results = []

    for test in TEST_REGISTRY:

        result = run_single_test(test)

        results.append(result)

    return results