"""
PyTest Test Cases

LC-0724: Find Pivot Index
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
    assert solver.pivot_index([1, 7, 3, 6, 5, 6]) == 3


def test_example_2(solver):
    assert solver.pivot_index([1, 2, 3]) == -1


def test_example_3(solver):
    assert solver.pivot_index([2, 1, -1]) == 0


def test_single_element(solver):
    assert solver.pivot_index([5]) == 0


def test_all_zeros(solver):
    assert solver.pivot_index([0, 0, 0, 0]) == 0


def test_negative_numbers(solver):
    assert solver.pivot_index([-1, -1, -1, 0, 1, 1]) == 0


def test_no_pivot(solver):
    assert solver.pivot_index([5, 4, 3, 2, 1]) == -1


def test_large_values(solver):
    assert solver.pivot_index([1000, -1000, 0]) == 2


def test_return_type(solver):
    result = solver.pivot_index([1, 7, 3, 6, 5, 6])

    assert isinstance(result, int)


def test_multiple_possible_pivots_returns_leftmost(solver):
    assert solver.pivot_index([0, 0, 0]) == 0
