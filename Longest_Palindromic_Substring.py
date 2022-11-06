import time


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def palind(string, left, right):
            while left >= 0 and right < len(string) and string[left] == string[right]:
                left -= 1
                right += 1
            return string[left+1:right]

        result = ""

        for idx in range(len(s)):
            print("STARTED", idx)
            result = max(palind(s, idx, idx), palind(s, idx, idx + 1), result, key=len)

        return result



s = Solution()
print(s.longestPalindrome("abb"))
print(s.longestPalindrome("bacabab"))
print(s.longestPalindrome("babad"))
print(s.longestPalindrome("cbbd"))
print(s.longestPalindrome("ac"))
print(s.longestPalindrome("ccc"))
print(s.longestPalindrome("c"))
print(s.longestPalindrome("bananas"))
print(s.longestPalindrome("xaabacxcabaaxcabaax"))
print(s.longestPalindrome("aacabdkacaa"))
print(s.longestPalindrome("babaddtattarrattatddetartrateedredividerb"))
print(s.longestPalindrome("abababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababa"))
print(s.longestPalindrome("321012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210123210012321001232100123210123"))
