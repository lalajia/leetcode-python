"""
Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

Example 1:
Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]
Example 2:
Input: root = [1,null,3]
Output: [1,3]
Example 3:
Input: root = []
Output: []
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from collections import deque
from typing import List, Optional


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = deque()
        if not root:
            return []
        queue.append(root)
        res = []
        while queue:
            lastNodeOfLevel = None
            size = len(queue)
            for i in range(size):
                curr = queue.popleft()
                if curr:
                    lastNodeOfLevel = curr
                    queue.append(curr.left)
                    queue.append(curr.right)
            if lastNodeOfLevel:
                res.append(lastNodeOfLevel.val)
        return res
