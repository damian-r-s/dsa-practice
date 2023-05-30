# 543. Diameter of Binary Tree
# Given the root of a binary tree, return the length of the diameter of the tree.
# The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.
# The length of a path between two nodes is represented by the number of edges between them

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def diameterOfBinaryTree(self, root):
        result = self.rec(root)
        return result[0]

    def rec(self, root):        
        if root is None:
            return [0, 0]
        
        left = self.rec(root.left)
        right = self.rec(root.right)

        heightMax = max(left[1], right[1])
        
        leftD = left[0]
        rightD = right[0]        
        maxD = max(leftD, rightD, left[1] + right[1])

        return [maxD, heightMax + 1]