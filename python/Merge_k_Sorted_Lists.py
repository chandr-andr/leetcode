# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return f"{self.val} {self.next if self.next else ''}"


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        all_values = []
        while lists:
            linked_list = lists.pop()

            while linked_list:
                all_values.append(linked_list.val)
                linked_list = linked_list.next

        all_values.sort()

        result = ListNode(-1)
        temp = result
        for val_ in range(len(all_values)):
            result.next = ListNode(all_values[val_])
            result = result.next

        return temp.next


list1 = ListNode(1)
list1.next = ListNode(2)
list1.next.next = ListNode(4)
list1.next.next.next = ListNode(5)

list2 = ListNode(2)
list2.next = ListNode(3)
list2.next.next = ListNode(6)

list3 = ListNode(1)
list2.next = ListNode(2)
list2.next.next = ListNode(5)
list2.next.next.next = ListNode(7)
list2.next.next.next.next = ListNode(7)

s = Solution()
print(s.mergeKLists([list1, list2, list3]))
