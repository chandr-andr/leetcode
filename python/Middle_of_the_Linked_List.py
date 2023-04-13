# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return f"{self.val} {self.next if self.next else ''}"


class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        import math

        count = 0
        temp = head
        while temp:
            count += 1
            temp = temp.next

        target_count = (
            round(count / 2) + 1 if count % 2 == 0 else math.ceil(count / 2)
        )

        iter_num = 0
        while True:
            iter_num += 1
            if iter_num == target_count:
                return head

            head = head.next


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
print(s.middleNode(head))


head = ListNode(
    val=1,
    next=ListNode(
        val=2,
        next=ListNode(
            val=3,
            next=ListNode(
                val=4,
                next=ListNode(val=5, next=None),
            ),
        ),
    ),
)
print(s.middleNode(head))
