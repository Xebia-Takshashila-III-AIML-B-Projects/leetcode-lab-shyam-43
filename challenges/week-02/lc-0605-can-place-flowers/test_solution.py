"""
PyTest Test Cases

LC-0605: Can Place Flowers
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
    assert solver.can_place_flowers([1, 0, 0, 0, 1], 1) is True


def test_example_2(solver):
    assert solver.can_place_flowers([1, 0, 0, 0, 1], 2) is False


def test_empty_flowerbed(solver):
    assert solver.can_place_flowers([0], 1) is True


def test_single_flower(solver):
    assert solver.can_place_flowers([1], 0) is True


def test_all_empty(solver):
    assert solver.can_place_flowers([0, 0, 0, 0, 0], 3) is True


def test_no_space(solver):
    assert solver.can_place_flowers([1, 1, 1, 1], 1) is False


def test_edge_positions(solver):
    assert solver.can_place_flowers([0, 0, 1, 0, 0], 2) is True


def test_large_flowerbed(solver):
    flowerbed = [0] * 100

    assert solver.can_place_flowers(flowerbed, 50) is True


def test_return_type(solver):
    result = solver.can_place_flowers([0, 0, 1], 1)

    assert isinstance(result, bool)


def test_zero_flowers_to_plant(solver):
    assert solver.can_place_flowers([1, 0, 1], 0) is True
