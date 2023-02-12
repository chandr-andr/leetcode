class Solution:
    def longestCommonPrefix(self, strs) -> str:
        max_pref = ""
        for chars in zip(*strs):
            if len(set(chars)) == 1:
                max_pref += chars[0]
            else:
                break
        return max_pref


s = Solution()
print(s.longestCommonPrefix(["flower", "flow", "flight"]))
print(s.longestCommonPrefix(["cir", "car"]))
