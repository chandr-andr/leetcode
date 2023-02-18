class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        open_remaining = n - 1
        close_remaining = n
        f_queue = [("(", open_remaining, close_remaining)]
        result = []

        while f_queue:
            item_from_stack = f_queue.pop()

            parentheses = item_from_stack[0]
            right = item_from_stack[1]
            left = item_from_stack[2]

            if right == left == 0:
                result.append(parentheses)
            else:
                if right != 0:
                    f_queue.append(
                        [
                            parentheses + "(",
                            right-1,
                            left,
                        ],
                    )
                if left > right:
                    f_queue.append(
                        [
                            parentheses + ")",
                            right,
                            left - 1,
                        ],
                    )
        return result


s = Solution()
print(s.generateParenthesis(3))
