class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 1:
            return 1

        longest_substring = ""
        new_substring = ""
        hashset = set()
        chars_hashmap = {}
        idx = 0
        while idx != len(s):
            char = s[idx]
            if char in hashset:
                if len(new_substring) > len(longest_substring):
                    longest_substring = new_substring

                new_substring = ""
                idx = chars_hashmap[char] + 1
                chars_hashmap.clear()
                hashset.clear()
                continue

            new_substring += char
            chars_hashmap[char] = idx
            hashset.add(char)

            if len(new_substring) > len(longest_substring):
                longest_substring = new_substring

            idx += 1
        return len(longest_substring)


s = Solution()
print(s.lengthOfLongestSubstring("abcabcbb"))