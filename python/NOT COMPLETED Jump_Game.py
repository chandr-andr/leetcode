from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        result = []
        target_idx = len(nums) - 1

        def sol(current_idx):
            if target_idx < current_idx or nums[current_idx] == 0:
                return
            if target_idx == current_idx:
                result.append(True)
                return

            for jump_number in range(1, nums[current_idx] + 1):
                sol(current_idx + jump_number)

        sol(0)

        return True in result


s = Solution()
print(s.canJump([2, 3, 1, 1, 4]))
