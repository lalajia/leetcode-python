"""
You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.
Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
"""

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        temp = ListNode()
        res = temp
        while list1 and list2:
            if list1.val > list2.val:
                res.next = list2
                list2 = list2.next
            else:
                res.next = list1
                list1 = list1.next
            res = res.next
        # Append the remaining elements from the non-empty list (if any)
        if list1:
            res.next = list1
        elif list2:
            res.next = list2
        return temp.next


next5 = ListNode(9, None)
next4 = ListNode(5, next5)
next3 = ListNode(3, next4)
listTwo = ListNode(1, next3)

nextTwo = ListNode(7, None)
nextOne = ListNode(4, nextTwo)
listOne = ListNode(1, nextOne)
res = Solution().mergeTwoLists(list1=listOne, list2=listTwo)
current = res
while current:
    print(current.val)
    current = current.next
