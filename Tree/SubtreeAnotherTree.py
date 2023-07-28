"""
Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.
A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.

Example 1:
Input: root = [3,4,5,1,2], subRoot = [4,1,2]
Output: true
2:
Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
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
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def sameTree(a, b):
            if not a and not b:
                return True
            if not a or not b or a.val != b.val:
                return False
            left = sameTree(a.left, b.left)
            right = sameTree(a.right, b.right)

            if left and right:
                return True
            return False

        if not subRoot:
            return True
        if not root:
            return False

        if sameTree(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)


tree1 = TreeNode(20)
tree1.left = TreeNode(5)
tree1.right = TreeNode(6)

tree2 = TreeNode(3)
tree2.left = TreeNode(9)
tree2.right = TreeNode(20)
tree2.right.left = TreeNode(5)
tree2.right.right = TreeNode(6)


print(Solution().isSubtree(tree2, tree1))
