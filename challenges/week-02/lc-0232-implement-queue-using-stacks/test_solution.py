"""
PyTest Test Cases

LC-0232: Implement Queue using Stacks
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

MyQueue = module.MyQueue


@pytest.fixture
def queue():
    return MyQueue()


def test_example_case(queue):
    queue.push(1)
    queue.push(2)

    assert queue.peek() == 1
    assert queue.pop() == 1
    assert queue.empty() is False


def test_single_element(queue):
    queue.push(10)

    assert queue.peek() == 10
    assert queue.pop() == 10
    assert queue.empty() is True


def test_multiple_push_pop(queue):
    queue.push(1)
    queue.push(2)
    queue.push(3)

    assert queue.pop() == 1
    assert queue.pop() == 2
    assert queue.pop() == 3


def test_peek_does_not_remove(queue):
    queue.push(5)

    assert queue.peek() == 5
    assert queue.peek() == 5
    assert queue.pop() == 5


def test_empty_queue(queue):
    assert queue.empty() is True


def test_interleaved_operations(queue):
    queue.push(1)
    queue.push(2)

    assert queue.pop() == 1

    queue.push(3)

    assert queue.peek() == 2
    assert queue.pop() == 2
    assert queue.pop() == 3


def test_fifo_behavior(queue):
    for i in range(1, 6):
        queue.push(i)

    for i in range(1, 6):
        assert queue.pop() == i


def test_return_types(queue):
    queue.push(100)

    assert isinstance(queue.peek(), int)
    assert isinstance(queue.pop(), int)
    assert isinstance(queue.empty(), bool)


def test_queue_after_emptying(queue):
    queue.push(1)
    queue.pop()

    queue.push(2)

    assert queue.peek() == 2
    assert queue.pop() == 2


def test_many_elements(queue):
    for i in range(100):
        queue.push(i)

    for i in range(100):
        assert queue.pop() == i

    assert queue.empty() is True
