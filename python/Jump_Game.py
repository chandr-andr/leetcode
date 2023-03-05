class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        current_idx = 0
        for idx, value in enumerate(nums):
            if idx > current_idx:
                return False
            current_idx = max(current_idx, idx + value)

        return True
