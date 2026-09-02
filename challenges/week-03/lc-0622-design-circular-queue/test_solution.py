import pytest

from solution import MyCircularQueue


def test_example_case():
    queue = MyCircularQueue(3)

    assert queue.enQueue(1) is True
    assert queue.enQueue(2) is True
    assert queue.enQueue(3) is True
    assert queue.enQueue(4) is False
    assert queue.Rear() == 3
    assert queue.isFull() is True
    assert queue.deQueue() is True
    assert queue.enQueue(4) is True
    assert queue.Rear() == 4


def test_empty_queue():
    queue = MyCircularQueue(3)

    assert queue.isEmpty() is True
    assert queue.isFull() is False
    assert queue.Front() == -1
    assert queue.Rear() == -1


def test_single_capacity():
    queue = MyCircularQueue(1)

    assert queue.isEmpty() is True
    assert queue.enQueue(10) is True
    assert queue.isFull() is True
    assert queue.Front() == 10
    assert queue.Rear() == 10
    assert queue.enQueue(20) is False
    assert queue.deQueue() is True
    assert queue.isEmpty() is True
    assert queue.deQueue() is False


def test_multiple_elements():
    queue = MyCircularQueue(5)

    for value in range(1, 6):
        assert queue.enQueue(value) is True

    assert queue.Front() == 1
    assert queue.Rear() == 5
    assert queue.isFull() is True


def test_fifo_behavior():
    queue = MyCircularQueue(3)

    queue.enQueue(10)
    queue.enQueue(20)
    queue.enQueue(30)

    assert queue.Front() == 10

    queue.deQueue()
    assert queue.Front() == 20

    queue.deQueue()
    assert queue.Front() == 30


def test_cannot_dequeue_empty_queue():
    queue = MyCircularQueue(3)

    assert queue.deQueue() is False
    assert queue.isEmpty() is True


def test_cannot_enqueue_full_queue():
    queue = MyCircularQueue(2)

    assert queue.enQueue(1) is True
    assert queue.enQueue(2) is True
    assert queue.enQueue(3) is False

    assert queue.Front() == 1
    assert queue.Rear() == 2


def test_wrap_around():
    queue = MyCircularQueue(3)

    queue.enQueue(1)
    queue.enQueue(2)
    queue.enQueue(3)

    queue.deQueue()
    queue.deQueue()

    assert queue.enQueue(4) is True
    assert queue.enQueue(5) is True

    assert queue.Front() == 3
    assert queue.Rear() == 5


def test_interleaved_operations():
    queue = MyCircularQueue(3)

    assert queue.enQueue(1) is True
    assert queue.enQueue(2) is True
    assert queue.deQueue() is True
    assert queue.enQueue(3) is True
    assert queue.enQueue(4) is True

    assert queue.Front() == 2
    assert queue.Rear() == 4
    assert queue.isFull() is True


def test_reuse_after_emptying():
    queue = MyCircularQueue(3)

    queue.enQueue(1)
    queue.enQueue(2)
    queue.enQueue(3)

    queue.deQueue()
    queue.deQueue()
    queue.deQueue()

    assert queue.isEmpty() is True

    assert queue.enQueue(10) is True
    assert queue.enQueue(20) is True

    assert queue.Front() == 10
    assert queue.Rear() == 20


def test_front_does_not_remove_element():
    queue = MyCircularQueue(3)

    queue.enQueue(10)
    queue.enQueue(20)

    assert queue.Front() == 10
    assert queue.Front() == 10
    assert queue.isEmpty() is False


def test_many_elements():
    queue = MyCircularQueue(1000)

    for value in range(1000):
        assert queue.enQueue(value) is True

    assert queue.isFull() is True
    assert queue.Front() == 0
    assert queue.Rear() == 999


def test_multiple_wraparounds():
    queue = MyCircularQueue(3)

    for _ in range(10):
        assert queue.enQueue(1) is True
        assert queue.deQueue() is True

    assert queue.isEmpty() is True


def test_return_types():
    queue = MyCircularQueue(2)

    assert isinstance(queue.enQueue(1), bool)
    assert isinstance(queue.enQueue(2), bool)
    assert isinstance(queue.isEmpty(), bool)
    assert isinstance(queue.isFull(), bool)
    assert isinstance(queue.deQueue(), bool)
    assert isinstance(queue.Front(), int)
    assert isinstance(queue.Rear(), int)