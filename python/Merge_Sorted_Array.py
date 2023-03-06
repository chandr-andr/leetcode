from typing import List


class Solution:
    def merge(
        self, nums1: List[int], m: int, nums2: List[int], n: int
    ) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1.extend(nums2)
        nums1.sort()

        while len(nums1) - 1 >= n + m:
            nums1.remove(0)


nums1, nums2, m, n = [1, 2, 3, 0, 0, 0], [2, 5, 6], 3, 3
s = Solution()
s.merge(nums1, m, nums2, n)
print(nums1)
