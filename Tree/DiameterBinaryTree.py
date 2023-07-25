"""
Given the root of a binary tree, return the length of the diameter of the tree.
The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.
The length of a path between two nodes is represented by the number of edges between them.

Example 1:
Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].
"""

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    res = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(root) -> int:
            node = root

            if node is None:
                return 0

            else:
                # lDepth = dfs(node.left) + 1
                # rDepth = dfs(node.right) + 1
                lDepth = dfs(node.left)
                rDepth = dfs(node.right)
                # self.res
                self.res = max(self.res, (lDepth + rDepth))
                # 在return这里加一
            return max(lDepth, rDepth) + 1

        dfs(root=root)
        # self.res
        return self.res


tree1 = TreeNode(1)
tree1.left = TreeNode(2)
tree1.right = TreeNode(3)
tree1.right.left = TreeNode(4)
tree1.right.right = TreeNode(5)

print(Solution().diameterOfBinaryTree(tree1))
