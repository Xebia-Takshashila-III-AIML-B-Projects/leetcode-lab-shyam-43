"""
PyTest Test Cases

LC-0070: Climbing Stairs
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
    assert solver.climb_stairs(2) == 2


def test_example_2(solver):
    assert solver.climb_stairs(3) == 3


def test_single_step(solver):
    assert solver.climb_stairs(1) == 1


def test_four_steps(solver):
    assert solver.climb_stairs(4) == 5


def test_five_steps(solver):
    assert solver.climb_stairs(5) == 8


def test_ten_steps(solver):
    assert solver.climb_stairs(10) == 89


def test_twenty_steps(solver):
    assert solver.climb_stairs(20) == 10946


def test_max_constraint(solver):
    assert solver.climb_stairs(45) == 1836311903


def test_return_type(solver):
    result = solver.climb_stairs(5)

    assert isinstance(result, int)


def test_positive_answer(solver):
    assert solver.climb_stairs(15) > 0
