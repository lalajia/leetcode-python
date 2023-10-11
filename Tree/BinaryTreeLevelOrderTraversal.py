"""
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
Example 2:

Input: root = [1]
Output: [[1]]
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
from typing import Deque, List, Optional


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # 必须确定有root
        if not root:
            return []

        queue = deque()
        queue.append(root)
        res = []

        # 每一层都有的时候while loop
        while queue:
            # 当前一层有多少个node
            size = len(queue)
            level = []
            for i in range(size):
                # 当前一层的所有node
                curr = queue.popleft()
                level.append(curr.val)

                # 每一个node的左边and右边
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            res.append(level)

        return res


tree1 = TreeNode(1)
tree1.left = TreeNode(2)
tree1.right = TreeNode(3)
tree1.right.left = TreeNode(4)
# tree1.right.right = TreeNode(5)
tree1.right.left.left = TreeNode(4)

print(Solution().levelOrder(tree1))
