class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        ways = 0

        prev = 0
        current = 1
        for _ in range(1, n + 1):
            ways = current + prev
            prev, current = current, ways

        return ways


class Solution2:
    def climbStairs(self, n: int) -> int:
        ways = [0]

        def solution(reached_step: int, step_num: int):
            if reached_step + step_num == n:
                ways[0] += 1
                return
            if reached_step + +step_num > n:
                return

            for step in [1, 2]:
                solution(reached_step + step_num, step)

        solution(0, 1)
        solution(0, 2)

        return ways[0]


s = Solution()
print(s.climbStairs(10))

s2 = Solution2()
print(s2.climbStairs(10))
