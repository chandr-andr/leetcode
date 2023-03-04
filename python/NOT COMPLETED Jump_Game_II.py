class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = []
        target_idx = len(nums) - 1

        def sol(current_idx, nums_of_steps):

            if target_idx < current_idx:
                result.append(nums_of_steps)
                return
            if target_idx == current_idx:
                result.append(nums_of_steps)
                return

            for jump_number in range(1, nums[current_idx] + 1):
                sol(
                    current_idx + jump_number,
                    nums_of_steps + 1,
                )

        sol(0, 0)
        return min(result)


class Solution2(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 0

        reachableIndex = 0
        previousReachableIndex = 0
        jump = 0

        for curr in range(len(nums)):
            if curr + nums[curr] >= reachableIndex:
                reachableIndex = curr + nums[curr]

            if curr == previousReachableIndex:
                jump += 1
                previousReachableIndex = reachableIndex
                if previousReachableIndex >= len(nums) - 1:
                    return jump


s = Solution2()
# print(s.jump([2, 2, 0, 1]))
# print(s.jump([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 0]))
# print(s.jump([0]))
# print(s.jump([1, 2, 1, 1, 1]))
# print(s.jump([1, 3, 2]))
print(s.jump([2, 3, 1, 1, 4]))
# print(s.jump([2, 3, 0, 1, 4]))
# print(s.jump([4, 1, 1, 3, 1, 1, 1]))
# print(
#     s.jump(
#         [
#             5,
#             6,
#             4,
#             4,
#             6,
#             9,
#             4,
#             4,
#             7,
#             4,
#             4,
#             8,
#             2,
#             6,
#             8,
#             1,
#             5,
#             9,
#             6,
#             5,
#             2,
#             7,
#             9,
#             7,
#             9,
#             6,
#             9,
#             4,
#             1,
#             6,
#             8,
#             8,
#             4,
#             4,
#             2,
#             0,
#             3,
#             8,
#             5,
#         ]
#     )
# )
