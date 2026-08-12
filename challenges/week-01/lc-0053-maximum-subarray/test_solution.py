"""
PyTest Test Cases

LC-0053: Maximum Subarray
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
    assert solver.max_sub_array([-2,1,-3,4,-1,2,1,-5,4]) == 6


def test_example_2(solver):
    assert solver.max_sub_array([1]) == 1


def test_example_3(solver):
    assert solver.max_sub_array([5,4,-1,7,8]) == 23


def test_all_negative(solver):
    assert solver.max_sub_array([-5,-2,-7,-1]) == -1


def test_all_positive(solver):
    assert solver.max_sub_array([1,2,3,4]) == 10


def test_single_negative(solver):
    assert solver.max_sub_array([-10]) == -10


def test_single_positive(solver):
    assert solver.max_sub_array([10]) == 10


def test_mixed_numbers(solver):
    assert solver.max_sub_array([2,-1,2,3,4,-5]) == 10


def test_return_type(solver):
    result = solver.max_sub_array([1,2,3])

    assert isinstance(result, int)


def test_large_input(solver):
    nums = [1] * 1000

    assert solver.max_sub_array(nums) == 1000
