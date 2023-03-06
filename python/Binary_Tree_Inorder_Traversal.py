# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []

        def in_order(root):
            if not root:
                return

            in_order(root.left)
            stack.append(root.val)
            in_order(root.right)

        in_order(root)

        return stack


class Solution2:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack: List[TreeNode] = []
        result = []

        while root or stack:

            while root:
                stack.append(root)
                root = root.left

            rt = stack.pop()
            result.append(rt.val)

            root = rt.right

        return result


tree = TreeNode(
    val=10,
    left=TreeNode(
        val=2,
        left=TreeNode(
            val=1,
        ),
        right=TreeNode(
            val=5,
            left=TreeNode(
                val=4,
            ),
        ),
    ),
    right=TreeNode(
        val=15,
        left=TreeNode(
            val=13,
            left=TreeNode(
                val=12,
            ),
            right=TreeNode(
                val=14,
            ),
        ),
    ),
)
print(Solution().inorderTraversal(tree))
print(Solution2().inorderTraversal(tree))
