class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        import itertools, re
        possible_subs = [
            "".join(comb)
            for comb
            in itertools.permutations(words, len(words))
        ]
        result_indexes = set()
        for sub in possible_subs:
            start_indexes = [match.start() for match in re.finditer(sub[0], s)]
            for start_idx in start_indexes:
                sub_length = len(sub)
                if s[start_idx:start_idx + sub_length] == sub:
                    result_indexes.add(start_idx)

        return result_indexes
        

s = Solution()
string_ = "barfoothefoobarman"
words = ["foo","bar"]
print(s.findSubstring(string_, words))
string_ = "aaa"
words = ["a","a"]
print(s.findSubstring(string_, words))
