class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        string_length = len(s)
        if string_length in {1, 2} or numRows == 1 or string_length < numRows:
            return s

        step = (numRows - 1) * 2

        step_back = 2
        res = ""

        for num in range(numRows):
            res += s[num]

            sub_num = num
            while sub_num < len(s):
                sub_num += step
                if num not in {0, numRows - 1}:
                    step_back *= num
                    sub_num -= step_back
                    if sub_num < len(s):
                        res += s[sub_num]
                    sub_num += step_back
                    step_back = 2

                if sub_num < len(s):
                    res += s[sub_num]

        return res


s = Solution()
print(s.convert("PAYPALISHIRING", 3))  # PINASGYHPI
print(s.convert("PAYPALISHIRING", 4))  # PINALSIGYAHRPI
print(s.convert("A", 1))  # A
print(s.convert("AB", 1))  # AB
print(s.convert("ABC", 1))  # ABC


# Input: s = "PAYPALISHIRING", numRows = 4
# Output: "PINALSIGYAHRPI"
# Explanation:
# P     I    N
# A   L S  I G
# Y A   H R
# P     I