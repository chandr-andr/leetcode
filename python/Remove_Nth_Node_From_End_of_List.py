# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return f"{self.val} {self.next if self.next else ''}"


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        count = 1
        temp = head.next

        while temp:
            count += 1
            temp = temp.next

        to_del_elem_end_count = count - n + 1

        count = 0
        prev_node = None
        node = head
        next_node = head.next
        while True:
            count += 1
            if to_del_elem_end_count == count:
                if prev_node:
                    if next_node:
                        prev_node.next = next_node
                        return head
                else:
                    return next_node
                prev_node.next = next_node
                return head
            prev_node = node
            node = next_node
            next_node = next_node.next


head = ListNode(
    val=1,
    next=ListNode(
        val=2,
        next=ListNode(
            val=3,
            next=ListNode(
                val=4,
                next=ListNode(
                    val=5,
                    next=None,
                )
            )
        )
    )
)
s = Solution()
print(s.removeNthFromEnd(head, 2))

head = ListNode(
    val=1,
    next=ListNode(
        val=2,
        next=ListNode(
            val=3,
            next=ListNode(
                val=4,
                next=ListNode(
                    val=5,
                    next=None,
                )
            )
        )
    )
)
s = Solution()
print(s.removeNthFromEnd(head, 5))

head = ListNode(
    val=1,
    next=ListNode(
        val=2,
        next=ListNode(
            val=3,
            next=ListNode(
                val=4,
                next=ListNode(
                    val=5,
                    next=None,
                )
            )
        )
    )
)
s = Solution()
print(s.removeNthFromEnd(head, 1))

head = ListNode(
    val=1,
    next=ListNode(
        val=2,
        next=None,
    )
)
s = Solution()
print(s.removeNthFromEnd(head, 1))

head = ListNode(
    val=1,
    next=None,
)
s = Solution()
print(s.removeNthFromEnd(head, 1))
