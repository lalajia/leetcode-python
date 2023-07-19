"""
Given the head of a singly linked list, reverse the list, and return the reversed list.
Example 1:
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
"""

"""https://giphy.com/gifs/yyHjGlxcCJfpTUudHk"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        pre = None

        while current is not None:
            nextNode = current.next
            current.next = pre
            pre = current
            current = nextNode

        return pre


nextTwo = ListNode(3, None)
nextOne = ListNode(2, nextTwo)
head = ListNode(1, nextOne)
print(Solution().reverseList(head=head))
