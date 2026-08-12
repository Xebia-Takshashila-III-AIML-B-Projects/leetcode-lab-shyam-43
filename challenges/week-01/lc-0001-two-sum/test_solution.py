"""
PyTest Test Cases

LC-0001: Two Sum
"""

import pytest

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


@pytest.fixture
def solver():
    return Solution()


def test_example_1(solver):
    nums = [2, 7, 11, 15]
    target = 9

    assert solver.two_sum(nums, target) == [0, 1]


def test_example_2(solver):
    nums = [3, 2, 4]
    target = 6

    assert solver.two_sum(nums, target) == [1, 2]


def test_example_3(solver):
    nums = [3, 3]
    target = 6

    assert solver.two_sum(nums, target) == [0, 1]


def test_negative_numbers(solver):
    nums = [-3, 4, 3, 90]
    target = 0

    assert solver.two_sum(nums, target) == [0, 2]


def test_zero_values(solver):
    nums = [0, 4, 3, 0]
    target = 0

    assert solver.two_sum(nums, target) == [0, 3]


def test_large_numbers(solver):
    nums = [1000000, 2000000, 3000000, 9000000]
    target = 11000000

    assert solver.two_sum(nums, target) == [1, 3]


def test_two_elements(solver):
    nums = [1, 2]
    target = 3

    assert solver.two_sum(nums, target) == [0, 1]


def test_duplicate_values(solver):
    nums = [1, 5, 1, 7]
    target = 2

    assert solver.two_sum(nums, target) == [0, 2]


def test_returns_list(solver):
    result = solver.two_sum([2, 7, 11, 15], 9)

    assert isinstance(result, list)


def test_result_has_two_indices(solver):
    result = solver.two_sum([2, 7, 11, 15], 9)

    assert len(result) == 2
