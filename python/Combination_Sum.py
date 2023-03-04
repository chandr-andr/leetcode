class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        st = []

        def dfs(candidates, target):
            if target < 0:
                return
            if target == 0:
                result.append(st.copy())
                return
            for candi_idx in range(len(candidates)):
                st.append(candidates[candi_idx])
                dfs(candidates[candi_idx:], target-candidates[candi_idx])
                st.pop()

        dfs(candidates, target)
        return result


s = Solution()
print(s.combinationSum([2, 3, 6, 7], 7))
print(s.combinationSum([2, 3, 5], 8))
