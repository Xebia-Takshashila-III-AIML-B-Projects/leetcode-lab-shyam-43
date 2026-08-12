"""
LC-0232: Implement Queue using Stacks

Solution Template
-----------------

Complete the implementation below.
"""


class MyQueue:
    def __init__(self):
        """
        Initialize your queue.

        Use only stack operations internally.
        """

        # ======================================================
        # TODO:
        #
        # Initialize your data structures.
        #
        # ======================================================

        pass

    def push(self, x: int) -> None:
        """
        Push element x to the back of the queue.
        """

        # TODO

        pass

    def pop(self) -> int:
        """
        Remove and return the element
        from the front of the queue.
        """

        # TODO

        pass

    def peek(self) -> int:
        """
        Return the front element.
        """

        # TODO

        pass

    def empty(self) -> bool:
        """
        Return True if the queue is empty,
        otherwise False.
        """

        # TODO

        pass


if __name__ == "__main__":
    queue = MyQueue()

    queue.push(1)
    queue.push(2)

    print(queue.peek())
