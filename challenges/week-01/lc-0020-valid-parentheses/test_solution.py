"""
PyTest Test Cases

LC-0020: Valid Parentheses
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
    assert solver.is_valid("()") is True


def test_example_2(solver):
    assert solver.is_valid("()[]{}") is True


def test_example_3(solver):
    assert solver.is_valid("(]") is False


def test_example_4(solver):
    assert solver.is_valid("([)]") is False


def test_example_5(solver):
    assert solver.is_valid("{[]}") is True


def test_single_open_bracket(solver):
    assert solver.is_valid("(") is False


def test_single_close_bracket(solver):
    assert solver.is_valid(")") is False


def test_nested_brackets(solver):
    assert solver.is_valid("((({{{[[[]]]}}})))") is True


def test_empty_stack_condition(solver):
    assert solver.is_valid("]") is False


def test_return_type(solver):
    result = solver.is_valid("()")

    assert isinstance(result, bool)
