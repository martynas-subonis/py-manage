import unittest
from src.package_b.math import add_one


class TestMath(unittest.TestCase):
    def test_add_one(self) -> None:
        self.assertEqual(2, add_one(1))


if __name__ == "__main__":
    unittest.main()
