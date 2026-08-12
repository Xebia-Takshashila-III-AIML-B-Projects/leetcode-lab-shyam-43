"""
PyTest Test Cases

LC-0121: Best Time to Buy and Sell Stock
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
    assert solver.max_profit([7, 1, 5, 3, 6, 4]) == 5


def test_example_2(solver):
    assert solver.max_profit([7, 6, 4, 3, 1]) == 0


def test_single_day(solver):
    assert solver.max_profit([5]) == 0


def test_increasing_prices(solver):
    assert solver.max_profit([1, 2, 3, 4, 5]) == 4


def test_decreasing_prices(solver):
    assert solver.max_profit([5, 4, 3, 2, 1]) == 0


def test_same_prices(solver):
    assert solver.max_profit([3, 3, 3, 3]) == 0


def test_profit_at_end(solver):
    assert solver.max_profit([8, 2, 1, 10]) == 9


def test_large_values(solver):
    assert solver.max_profit([10000, 1, 9999]) == 9998


def test_return_type(solver):
    result = solver.max_profit([7, 1, 5])

    assert isinstance(result, int)


def test_empty_profit(solver):
    assert solver.max_profit([9, 8]) == 0
