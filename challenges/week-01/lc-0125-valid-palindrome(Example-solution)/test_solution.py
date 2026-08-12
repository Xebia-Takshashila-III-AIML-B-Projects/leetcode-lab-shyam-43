import unittest

from pathlib import Path
import importlib.util

solution_path = Path(__file__).parent / "solution.py"

spec = importlib.util.spec_from_file_location(
    "student_solution",
    solution_path,
)

module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

Solution = module.Solution


class TestValidPalindrome(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertTrue(
            self.solution.isPalindrome(
                "A man, a plan, a canal: Panama"
            )
        )

    def test_example_2(self):
        self.assertFalse(
            self.solution.isPalindrome(
                "race a car"
            )
        )

    def test_example_3(self):
        self.assertTrue(
            self.solution.isPalindrome(
                " "
            )
        )

    def test_single_character(self):
        self.assertTrue(
            self.solution.isPalindrome(
                "a"
            )
        )

    def test_numbers(self):
        self.assertTrue(
            self.solution.isPalindrome(
                "1221"
            )
        )

    def test_mixed_case(self):
        self.assertTrue(
            self.solution.isPalindrome(
                "Madam"
            )
        )


if __name__ == "__main__":
    unittest.main()
