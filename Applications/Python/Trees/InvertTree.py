# 226. Invert Binary Tree
# Given the root of a binary tree, invert the tree, and return its root.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root):
        if root is None:
            return None

        right = self.invertTree(root.left)
        left = self.invertTree(root.right)

        root.left = left
        root.right = right

        return root