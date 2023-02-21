class Solution:
    def removeDuplicates(self, nums):
        left = 1
        for idx in range(1, len(nums)):
            if nums[idx] != nums[idx - 1]:
                nums[left] = nums[idx]
                left += 1
        return left


s = Solution()
l = [1, 1, 2]
print(s.removeDuplicates(l))
print(l)
