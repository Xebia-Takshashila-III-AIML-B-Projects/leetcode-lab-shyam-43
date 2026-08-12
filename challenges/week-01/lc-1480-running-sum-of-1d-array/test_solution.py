"""
PyTest Test Cases

LC-1480: Running Sum of 1D Array
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
    assert solver.running_sum([1, 2, 3, 4]) == [1, 3, 6, 10]


def test_example_2(solver):
    assert solver.running_sum([1, 1, 1, 1, 1]) == [1, 2, 3, 4, 5]


def test_example_3(solver):
    assert solver.running_sum([3, 1, 2, 10, 1]) == [3, 4, 6, 16, 17]


def test_single_element(solver):
    assert solver.running_sum([5]) == [5]


def test_all_zeros(solver):
    assert solver.running_sum([0, 0, 0, 0]) == [0, 0, 0, 0]


def test_negative_numbers(solver):
    assert solver.running_sum([-1, -2, -3]) == [-1, -3, -6]


def test_mixed_numbers(solver):
    assert solver.running_sum([5, -2, 3, -1]) == [5, 3, 6, 5]


def test_large_values(solver):
    assert solver.running_sum([1000000, 1000000]) == [1000000, 2000000]


def test_return_type(solver):
    result = solver.running_sum([1, 2, 3])

    assert isinstance(result, list)


def test_result_length(solver):
    nums = [4, 2, 8, 1]

    result = solver.running_sum(nums)

    assert len(result) == len(nums)
