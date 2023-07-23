"""
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
Merge all the linked-lists into one sorted linked-list and return it.

Example 1:
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
"""

# Definition for singly-linked list.
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        while len(lists) > 1:
            merged = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if i + 1 < len(lists) else None
                merged.append(self.mergeTwoList(l1, l2))
            lists = merged
        return lists[0]

    def mergeTwoList(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy = ListNode(-1)
        cur = dummy
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next

        # cur.next = l1 if l1 else None
        # cur.next = l2 if l2 else None
        cur.next = l1 if l1 else l2
        return dummy.next


next6 = ListNode(10, None)
listThree = ListNode(2, next6)

next5 = ListNode(9, None)
next4 = ListNode(5, next5)
next3 = ListNode(3, next4)
listTwo = ListNode(1, next3)

nextTwo = ListNode(7, None)
nextOne = ListNode(4, nextTwo)
listOne = ListNode(1, nextOne)

lists = [listOne, listTwo, listThree, None]
res = Solution().mergeKLists(lists=lists)
current = res
while current:
    print(current.val)
    current = current.next
