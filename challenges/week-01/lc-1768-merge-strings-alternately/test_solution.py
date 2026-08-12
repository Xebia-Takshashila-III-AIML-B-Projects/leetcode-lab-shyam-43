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
    assert solver.merge_alternately("abc", "pqr") == "apbqcr"


def test_example_2(solver):
    assert solver.merge_alternately("ab", "pqrs") == "apbqrs"


def test_example_3(solver):
    assert solver.merge_alternately("abcd", "pq") == "apbqcd"


def test_single_character(solver):
    assert solver.merge_alternately("a", "b") == "ab"


def test_empty_second_remaining(solver):
    assert solver.merge_alternately("hello", "x") == "hxello"


def test_same_length(solver):
    assert solver.merge_alternately("xyz", "123") == "x1y2z3"


def test_return_type(solver):
    result = solver.merge_alternately("abc", "pqr")
    assert isinstance(result, str)
