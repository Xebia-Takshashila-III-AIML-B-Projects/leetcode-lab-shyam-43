"""
PyTest Test Cases

LC-0198: House Robber
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
    assert solver.rob([1, 2, 3, 1]) == 4


def test_example_2(solver):
    assert solver.rob([2, 7, 9, 3, 1]) == 12


def test_single_house(solver):
    assert solver.rob([5]) == 5


def test_two_houses(solver):
    assert solver.rob([2, 10]) == 10


def test_all_equal(solver):
    assert solver.rob([5, 5, 5, 5]) == 10


def test_alternate_large_values(solver):
    assert solver.rob([100, 1, 100, 1, 100]) == 300


def test_zero_values(solver):
    assert solver.rob([0, 0, 0, 0]) == 0


def test_increasing_values(solver):
    assert solver.rob([1, 2, 3, 4, 5]) == 9


def test_return_type(solver):
    result = solver.rob([2, 7, 9])

    assert isinstance(result, int)


def test_large_input(solver):
    nums = [1] * 100
    assert solver.rob(nums) == 50
