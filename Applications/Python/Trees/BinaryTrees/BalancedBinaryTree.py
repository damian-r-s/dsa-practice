# 110. Balanced Binary Tree
# Given a binary tree, determine if it is height-balanced
# A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root):
        if root is None:
            return True

        result = self.rec(root)

        if result == -1:
            return False
        
        return True

    def rec(self, root):
        if root is None:
            return 0

        left = self.rec(root.left)
        if left == -1:
            return -1

        right = self.rec(root.right)
        if right == -1:
            return -1

        if abs(left - right) > 1:
            return -1

        return max(left, right) + 1