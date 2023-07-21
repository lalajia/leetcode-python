"""
You are given the head of a singly linked-list. The list can be represented as:
L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:
L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.

Example 1:
Input: head = [1,2,3,4]
Output: [1,4,2,3]
"""


from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        slow = head
        if not head or not head.next:
            return

        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        def reversedList(self, head: Optional[ListNode]) -> Optional[ListNode]:
            current = head
            pre = None
            while current:
                nextNode = current.next
                current.next = pre
                pre = current
                current = nextNode
            return pre

        def mergeList(
            self, list1: Optional[ListNode], list2: Optional[ListNode]
        ) -> Optional[ListNode]:
            while list1 and list2:
                temp1, temp2 = list1.next, list2.next
                list1.next = list2
                # !!不是list1是temp1
                list2.next = temp1
                list1, list2 = temp1, temp2

            return None

        list2 = reversedList(self, head=slow.next)
        slow.next = None

        mergeList(self, list1=head, list2=list2)


nextThree = ListNode(4, None)
nextTwo = ListNode(3, nextThree)
nextOne = ListNode(2, nextTwo)
head = ListNode(1, nextOne)
print(Solution().reorderList(head=head))
