# Given a collection of candidate numbers (candidates) and
# a target number (target), find all unique combinations
# in candidates where the candidate numbers sum to target.

# Each number in candidates may only be used once in the combination.

# Note: The solution set must not contain duplicate combinations.


class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()

        result = []
        st = []

        def dfs(candidates, target, idx):
            if target == 0:
                result.append(st.copy())
                return
            for candi_idx in range(idx, len(candidates)):
                if candidates[candi_idx] > target:
                    break

                if (
                    candidates[candi_idx] == candidates[candi_idx - 1]
                    and candi_idx > idx
                ):
                    continue

                st.append(candidates[candi_idx])
                dfs(
                    candidates,
                    target - candidates[candi_idx],
                    candi_idx + 1,
                )
                st.pop()

        dfs(candidates, target, 0)
        return result


s = Solution()
print(s.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8))
print(s.combinationSum2([2, 5, 2, 1, 2], 5))
