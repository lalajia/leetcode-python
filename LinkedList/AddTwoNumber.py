"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
"""

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy = ListNode(-1)
        res = dummy
        temp = 0
        while l1 or l2 or temp:
            # check if l1 and l2 exist
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            val = val1 + val2 + temp
            temp = val // 10
            val = val % 10

            res.next = ListNode(val)
            res = res.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next


list1 = ListNode(4)
list1.next = ListNode(0)
list1.next.next = ListNode(9)

list2 = ListNode(9)
list2.next = ListNode(0)
list2.next.next = ListNode(1)

solution = Solution()
res = solution.addTwoNumbers(list1, list2)

print("List 1:", list1.val, list1.next.val, list1.next.next.val)
print("List 2:", list2.val, list2.next.val, list2.next.next.val)

print("List 1:", res.val, res.next.val, res.next.next.val, res.next.next.next.val)  # type: ignore
