# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return f"{self.val} {self.next if self.next else ''}"


class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not list1:
            return list2
        if not list2:
            return list1

        values = []
        while (list1 is not None):
            values.append(list1.val)
            list1 = list1.next

        while (list2 is not None):
            values.append(list2.val)
            list2 = list2.next

        values.sort()
        result = ListNode(-1)
        temp = result
        for val_ in range(len(values)):
            result.next = ListNode(values[val_])
            result = result.next

        return temp.next


s = Solution()
list1 = ListNode(1)
list1.next = ListNode(2)
list1.next.next = ListNode(4)
list1.next.next.next = ListNode(5)

list2 = ListNode(2)
list2.next = ListNode(3)
list2.next.next = ListNode(6)

print(s.mergeTwoLists(list1, list2))
