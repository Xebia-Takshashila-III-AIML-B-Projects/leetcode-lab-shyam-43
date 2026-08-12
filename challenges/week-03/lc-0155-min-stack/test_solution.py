from pathlib import Path
import importlib.util

solution_path = Path(__file__).parent / "solution.py"

spec = importlib.util.spec_from_file_location(
    "student_solution",
    solution_path,
)

module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

MinStack = module.MinStack


def test_example_case():
    stack = MinStack()

    stack.push(-2)
    stack.push(0)
    stack.push(-3)

    assert stack.getMin() == -3

    stack.pop()

    assert stack.top() == 0
    assert stack.getMin() == -2


def test_single_element():
    stack = MinStack()

    stack.push(5)

    assert stack.top() == 5
    assert stack.getMin() == 5


def test_multiple_push_pop():
    stack = MinStack()

    stack.push(4)
    stack.push(2)
    stack.push(6)
    stack.push(1)

    assert stack.getMin() == 1

    stack.pop()

    assert stack.getMin() == 2

    stack.pop()

    assert stack.top() == 2
    assert stack.getMin() == 2


def test_duplicate_minimum():
    stack = MinStack()

    stack.push(2)
    stack.push(2)
    stack.push(3)

    assert stack.getMin() == 2

    stack.pop()

    assert stack.getMin() == 2

    stack.pop()

    assert stack.getMin() == 2


def test_negative_numbers():
    stack = MinStack()

    stack.push(-1)
    stack.push(-5)
    stack.push(-3)

    assert stack.getMin() == -5

    stack.pop()

    assert stack.getMin() == -5

    stack.pop()

    assert stack.getMin() == -1
