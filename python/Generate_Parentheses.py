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
            item_from_f_queue = f_queue.pop()

            parentheses = item_from_f_queue[0]
            left = item_from_f_queue[1]
            right = item_from_f_queue[2]

            if right == left == 0:
                result.append(parentheses)
            else:
                if left != 0:
                    f_queue.append(
                        [
                            parentheses + "(",
                            left-1,
                            right,
                        ],
                    )
                if right > left:
                    f_queue.append(
                        [
                            parentheses + ")",
                            left,
                            right - 1,
                        ],
                    )
        return result


s = Solution()
print(s.generateParenthesis(3))
