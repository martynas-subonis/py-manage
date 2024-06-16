import unittest
from src.package_a.compute import fib


class TestCompute(unittest.TestCase):
    def test_fib(self) -> None:
        self.assertEqual(5, fib(5))


if __name__ == "__main__":
    unittest.main()
