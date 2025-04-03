import unittest


def fibcalc(first: int, second: int, length: int):
    if not all(isinstance(x, int) for x in [first, second, length]):
        raise TypeError("Error: All inputs must be integers.")
    if length == 0:
        return [first]

    sequence = [first]  # Start with the first value
    sequence += fibcalc(second, first + second, length - 1)  # Recursively app
    return sequence


class TestFibonacci(unittest.TestCase):

    def test_valid_fibonacci(self):
        self.assertEqual(fibcalc(0, 1, 6), [0, 1, 1, 2, 3, 5, 8])  # 7 terms
        self.assertEqual(fibcalc(2, 3, 4), [2, 3, 5, 8, 13])  # 5 terms
        self.assertEqual(fibcalc(5, 8, 5), [5, 8, 13, 21, 34, 55])  # 6 terms


if __name__ == "__main__":
    unittest.main()
