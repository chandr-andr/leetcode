class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        import itertools

        closest_value = None
        all_sums = {sum(comb) for comb in itertools.combinations(nums, 3)}

        if target in all_sums:
            return target

        for sums in all_sums:
            if closest_value is None:
                closest_value = sums
            if abs(target - sums) < abs(target - closest_value):
                closest_value = sums
        return closest_value


# s = Solution()
# print(s.threeSumClosest([-1, 2, 1, -4], 1))
# print(s.threeSumClosest([0, 0, 0], 1))
# print(s.threeSumClosest([1, 1, 1, 0], 100))


class NewSolution:
    def threeSumClosest(self, nums, target):
        import sys
        nums.sort()
        num_len = len(nums)
        min_diff = sys.maxsize

        right = num_len - 1
        for num1 in range(num_len):
            num2, num3 = num1 + 1, right
            while num2 < num3:
                diff = nums[num1] + nums[num2] + nums[num3] - target
                if abs(diff) < abs(min_diff):
                    min_diff = diff

                if diff > 0:
                    num3 -= 1
                elif diff < 0:
                    num2 += 1
                else:
                    return target

        return target + min_diff


ns = NewSolution()
print(ns.threeSumClosest([-1, 2, 1, -4], 1))
print(ns.threeSumClosest([0, 0, 0], 1))
print(ns.threeSumClosest([1, 1, 1, 0], 100))
