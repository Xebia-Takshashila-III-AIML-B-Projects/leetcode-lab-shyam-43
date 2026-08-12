"""
LC-0146: LRU Cache

Solution Template
-----------------

Complete the implementation below.
"""


class LRUCache:
    def __init__(self, capacity: int):
        """
        Initialize the cache.

        Args:
            capacity: Maximum number of items the cache can store.
        """

        # TODO:
        # Initialize your data structures.

        pass

    def get(self, key: int) -> int:
        """
        Return the value associated with the key.

        If the key does not exist, return -1.
        """

        # TODO

        pass

    def put(self, key: int, value: int) -> None:
        """
        Insert or update a key-value pair.

        If the cache exceeds capacity,
        remove the least recently used item.
        """

        # TODO

        pass


if __name__ == "__main__":
    cache = LRUCache(2)

    # Example
    cache.put(1, 1)
    cache.put(2, 2)

    print(cache.get(1))
