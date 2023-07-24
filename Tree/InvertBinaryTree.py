"""
Given the root of a binary tree, invert the tree, and return its root.
Example 1:
Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]
"""

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        root.left, root.right = root.right, root.left

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root


tree1 = TreeNode(4)
tree1.left = TreeNode(2)
tree1.left.left = TreeNode(1)
tree1.left.right = TreeNode(3)
tree1.right = TreeNode(7)
tree1.right.left = TreeNode(6)
tree1.right.right = TreeNode(9)

res = Solution().invertTree(tree1)


def inorder_traversal(node: Optional[TreeNode]):
    if node is None:
        return

    inorder_traversal(node.left)
    print(node.val)
    inorder_traversal(node.right)


inorder_traversal(res)
