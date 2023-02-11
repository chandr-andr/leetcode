# Working but bad.

class BadSolution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) <= 2:
            return min(height)
        max_value = 0
        for idx1, hgt1 in enumerate(height):
            for idx2, hgt2 in enumerate(height[idx1+1:], start=idx1+1):
                new_value = (idx2 - idx1) * min([hgt1, hgt2])
                if new_value > max_value:
                    max_value = new_value
        return max_value


# s = Solution()
# print(s.maxArea(height=[1, 8, 6, 2, 5, 4, 8, 3, 7]))
# print("-"*50, "/n")
# print(s.maxArea(height=[1, 2]))


# New Solution

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left_idx = 0
        right_idx = len(height) - 1
        max_value = 0

        while left_idx < right_idx:
            left_hgt = height[left_idx]
            right_hgt = height[right_idx]

            if left_hgt > right_hgt:
                new_value = right_hgt * (right_idx - left_idx)
                right_idx -= 1
            else:
                new_value = left_hgt * (right_idx - left_idx)
                left_idx += 1

            if new_value > max_value:
                max_value = new_value

        return max_value


s = Solution()
print(s.maxArea(height=[1, 8, 6, 2, 5, 4, 8, 3, 7]))
print("-"*50, "/n")
print(s.maxArea(height=[1, 2]))
