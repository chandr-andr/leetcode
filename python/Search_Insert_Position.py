class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        while left <= right:
            middle = (left + right) // 2
            now_num = nums[middle]
            if now_num == target:
                return middle
            elif now_num > target:
                right = middle - 1
            else:
                left = middle + 1
        return right + 1


s = Solution()
print(s.searchInsert([1, 3, 4, 7], 5))
print(s.searchInsert([1, 3, 5, 7, 9, 15, 20, 21], 8))
print(s.searchInsert([1, 3, 5, 7, 9, 15, 20, 21, 23], 100))
