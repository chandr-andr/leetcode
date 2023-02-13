class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        import itertools

        mapping = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        strings = [
            "".join(combination)
            for combination
            in itertools.product(*[mapping[digit] for digit in digits])
            if combination
        ]

        return strings


s = Solution()
print(s.letterCombinations("2345"))
