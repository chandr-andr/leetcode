class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums1.extend(nums2)
        nums1.sort()
        if len(nums1) % 2 == 0:
            return sum((nums1[len(nums1) // 2 - 1:len(nums1) // 2 + 1])) / 2.0
        else:
            return nums1[len(nums1) // 2]


s = Solution()
print(s.findMedianSortedArrays([1, 2], [3, 4]))
