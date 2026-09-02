"""
LC-0622: Design Circular Queue

Solution Template
-----------------

Complete the implementation below.
"""


class MyCircularQueue:
    def __init__(self, k: int):
        """
        Initialize your circular queue.

        Parameters:
            k: Maximum capacity of the queue.
        """

        # TODO:
        # Initialize the data structures required
        # for your circular queue.

        pass

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue.

        Return True if successful.
        Return False if the queue is full.
        """

        # TODO:
        # 1. Check whether the queue is full.
        # 2. Insert the value at the correct position.
        # 3. Move the rear position circularly.
        # 4. Update the current size.

        pass

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue.

        Return True if successful.
        Return False if the queue is empty.
        """

        # TODO:
        # 1. Check whether the queue is empty.
        # 2. Move the front position circularly.
        # 3. Update the current size.

        pass

    def Front(self) -> int:
        """
        Return the front item of the queue.

        Return -1 if the queue is empty.
        """

        # TODO:
        # Return the element at the front position.

        pass

    def Rear(self) -> int:
        """
        Return the last item of the queue.

        Return -1 if the queue is empty.
        """

        # TODO:
        # Return the last inserted element.
        # Remember that rear may represent
        # the next insertion position.

        pass

    def isEmpty(self) -> bool:
        """
        Return True if the queue is empty.
        Otherwise, return False.
        """

        # TODO:
        # Check whether the current size is zero.

        pass

    def isFull(self) -> bool:
        """
        Return True if the queue is full.
        Otherwise, return False.
        """

        # TODO:
        # Check whether the current size
        # is equal to the queue capacity.

        pass


if __name__ == "__main__":
    queue = MyCircularQueue(3)

    queue.enQueue(1)
    queue.enQueue(2)
    queue.enQueue(3)

    print(queue.Rear())
    print(queue.isFull())

    queue.deQueue()
    queue.enQueue(4)

    print(queue.Rear())