# 230. Kth Smallest Element in a BST
# Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack = []        
        current = root
        while stack or current:
            while current:
                stack.append(current)
                current = current.left               
            
            current = stack.pop()
            k -= 1
            if k == 0:
                return current.val
            
            current = current.right