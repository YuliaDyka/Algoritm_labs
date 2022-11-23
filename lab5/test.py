from KnuthMorrisPratt import kmp
import time
# import unittest

# class AdditionTest(unittest.TestCase):
def fastest_test():
    print("------The fastest test------")
    string = "a" * 10000
    print(f"Len - {len(string)}")
    pattern = "aaaaaaaa"

    timer = time.time()

    assert kmp(pattern, string) == 0

    print(f"Time - {time.time() - timer}")

def average_test():
    print("------The average test------")
    string = "a" * 5000
    string += "c"
    string += "a" * 5000
    print(f"Len - {len(string)}")
    pattern = "aaac"

    timer = time.time()

    assert kmp(pattern, string) != -1

    print(f"Time - {time.time() - timer}")

def second_average_test():
    print("------The second average test------")
    string = "Lorem ipsum dolor sit amet, consectetur adipiscing elit" * 90
    string += "PythonTest"
    string += "Lorem ipsum dolor sit amet, consectetur adipiscing elit" * 90
    print(f"Len - {len(string)}")
    pattern = "PythonTest"

    timer = time.time()

    assert kmp(pattern, string) != -1

    print(f"Time - {time.time() - timer}")


def slowest_test():
    print("------The slowest test------")
    string = "a" * 10000
    print(f"Len - {len(string)}")
    string += "jab"
    pattern = "ajab"

    timer = time.time()

    assert kmp(pattern, string) != -1

    print(f"Time - {time.time() - timer}")


if __name__ == "__main__":
    fastest_test()
    print("Fastest test success\n")

    average_test()
    print("Average test success\n")

    second_average_test()
    print("Second average test success\n")

    slowest_test()
    print("Slowest test success\n")
