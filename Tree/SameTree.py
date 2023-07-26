"""
Given the roots of two binary trees p and q, write a function to check if they are the same or not.
Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

Example 1:
Input: p = [1,2], q = [1,null,2]
Output: false
"""

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(p, q):
            # Base case: Both nodes are None, which means they match
            if not p and not q:
                return True

            # Base case: One of the nodes is None, which means they don't match
            if not p or not q:
                return False

            if p.val != q.val:
                return False

            left = dfs(p.left, q.left)
            right = dfs(p.right, q.right)

            if left and right:
                return True
            return False

        return dfs(p, q)


tree1 = TreeNode(3)
tree1.right = TreeNode(20)

tree2 = TreeNode(3)
tree2.left = TreeNode(9)
tree2.right = TreeNode(20)


print(Solution().isSameTree(tree1, tree2))
