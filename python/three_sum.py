# Given an integer array nums, return all the triplets
# [nums[i], nums[j], nums[k]] such that i != j, i != k,
# and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = set()

        positive, negative, zeros = [], [], []

        for num in nums:
            if num > 0:
                positive.append(num)
            if num < 0:
                negative.append(num)
            if num == 0:
                zeros.append(num)

        positive_set = set(positive)
        negative_set = set(negative)

        if len(zeros) >= 3:
            result.add((0, 0, 0))

        if zeros:
            for p_num in positive:
                if -p_num in negative_set:
                    result.add((p_num, 0, -p_num))

        for neg_num_idx1 in range(len(negative)):
            for neg_num_idx2 in range(neg_num_idx1 + 1, len(negative)):
                num_in_pos = -(
                    negative[neg_num_idx1] + negative[neg_num_idx2]
                )
                if num_in_pos in positive_set:
                    result.add(
                        tuple(
                            sorted(
                                [
                                    negative[neg_num_idx1],
                                    negative[neg_num_idx2],
                                    num_in_pos,
                                ]
                            )
                        )
                    )

        for pos_num_idx1 in range(len(positive)):
            for pos_num_idx2 in range(pos_num_idx1 + 1, len(positive)):
                num_in_neg = -(
                    positive[pos_num_idx1] + positive[pos_num_idx2]
                )
                if num_in_neg in negative_set:
                    result.add(
                        tuple(
                            sorted(
                                [
                                    positive[pos_num_idx1],
                                    positive[pos_num_idx2],
                                    num_in_neg,
                                ]
                            )
                        )
                    )

        return result


s = Solution()
print(s.threeSum([-1, 0, 1, 2, -1, -4]))
print(s.threeSum([0, 1, 1]))
print(s.threeSum([0, 0, 0]))
