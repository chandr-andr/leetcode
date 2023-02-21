# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return f"{self.val} {self.next if self.next else ''}"


class BadSolution(object):
    def swapPairs(self, head):
        """
        :type head: ListNodes
        :rtype: ListNode
        """
        values = []
        while head:
            values.append(head.val)
            head = head.next

        if not values:
            return None

        new_values = []
        for value_idx in range(0, len(values), 2):
            if value_idx + 1 < len(values):
                new_values.append(values[value_idx + 1])
            new_values.append(values[value_idx])

        node = ListNode(-1)
        temp = node
        for value_idx in range(len(new_values)):
            node.next = ListNode(new_values[value_idx])
            node = node.next

        return temp.next


list1 = ListNode(1)
list1.next = ListNode(2)
list1.next.next = ListNode(4)
list1.next.next.next = ListNode(5)

list2 = ListNode(2)
list2.next = ListNode(3)
list2.next.next = ListNode(6)

list3 = ListNode(1)
list3.next = ListNode(2)
list3.next.next = ListNode(5)
list3.next.next.next = ListNode(7)
list3.next.next.next.next = ListNode(7)

# s = BadSolution()
# print(s.swapPairs(list1))
# print(s.swapPairs(list2))
# print(s.swapPairs(list3))


class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNodes
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        prev, prev.next = dummy, head
        while prev.next and prev.next.next:
            current = prev.next
            next_from_current = current.next
            prev.next, next_from_current.next, current.next = next_from_current, current, next_from_current.next
            prev = current
        return dummy.next



list3 = ListNode(1)
list3.next = ListNode(2)
list3.next.next = ListNode(5)
list3.next.next.next = ListNode(7)
list3.next.next.next.next = ListNode(7)

ss = Solution()
print(ss.swapPairs(list3))