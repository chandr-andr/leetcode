from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return f"{self.val} {self.next if self.next else ''}"


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            head

        prev_node = dummy = ListNode(val=float("-inf"), next=head)
        current_node = head

        while current_node:
            if prev_node.val == current_node.val:
                prev_node.next = current_node.next
                current_node = current_node.next
            else:
                prev_node = prev_node.next
                current_node = current_node.next

        return dummy.next


s = Solution()
head = ListNode(
    val=1,
    next=ListNode(
        val=1,
        next=ListNode(
            val=2,
            next=ListNode(
                val=3,
                next=ListNode(
                    val=3,
                    next=ListNode(val=3, next=None),
                ),
            ),
        ),
    ),
)
print(s.deleteDuplicates(head))
