"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Example 1:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:
Input: head = [1], n = 1
Output: []
"""


# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # when the node to be removed is the head of the linked list.
        # Dummy node as the new head
        dummy = ListNode(-1)
        dummy.next = head

        left, right = dummy, dummy
        while n > 0:
            right = right.next  # type: ignore
            n -= 1

        while right.next:  # type: ignore
            right = right.next  # type: ignore
            left = left.next  # type: ignore

        left.next = left.next.next  # type: ignore

        return dummy.next
