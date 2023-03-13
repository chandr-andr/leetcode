class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # FIRST VERSION (BAD)
        # for idx, num in enumerate(nums):
        #     for s_idx, s_num in enumerate(nums[idx + 1:], idx+1):
        #         if num + s_num == target:
        #             return [idx, s_idx]

        # OH MY GOD, GOOOOD
        hashmap = dict()
        for idx, num in enumerate(nums):
            if target - num in hashmap:
                return [hashmap[target - num], idx]
            hashmap[num] = idx
