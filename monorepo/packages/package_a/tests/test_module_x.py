import unittest
from package_a.module_x import fib


class TestCompute(unittest.TestCase):
    def test_fib(self) -> None:
        self.assertEqual(5, fib(5))


if __name__ == "__main__":
    unittest.main()
