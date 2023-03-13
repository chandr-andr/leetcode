class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        s_dict = {}
        t_dict = {}

        for idx, ls in enumerate(s):
            s_dict.setdefault(ls, []).append(idx)

        for idx, lt in enumerate(t):
            t_dict.setdefault(lt, []).append(idx)

        return sorted(list(s_dict.values())) == sorted(list(t_dict.values()))


s = Solution()
print(
    s.isIsomorphic(
        "bbbaaaba",
        "aaabbbba",
    )
)

print(
    s.isIsomorphic(
        "add",
        "egg",
    )
)
