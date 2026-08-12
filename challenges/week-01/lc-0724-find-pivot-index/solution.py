"""
LC-0724: Find Pivot Index

Solution Template
-----------------

Complete the function below.

Time Complexity:
    TODO

Space Complexity:
    TODO
"""

from typing import List


class Solution:
    def pivot_index(self, nums: List[int]) -> int:
        """
        Find the pivot index of an array.

        A pivot index is an index where the sum of all
        elements strictly to the left is equal to the
        sum of all elements strictly to the right.

        If no pivot index exists, return -1.

        Args:
            nums: List of integers.

        Returns:
            The leftmost pivot index if it exists.
            Otherwise, return -1.
        """

        # ======================================================
        # TODO:
        #
        # Write your solution here.
        #
        # ======================================================

        pass


if __name__ == "__main__":
    solution = Solution()

    # Example
    print(solution.pivot_index([1, 7, 3, 6, 5, 6]))