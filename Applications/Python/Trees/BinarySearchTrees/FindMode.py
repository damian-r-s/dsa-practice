# 501. Find Mode in Binary Search Tree
from ast import List
from pyparsing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.count = {}

    def inOrder(self, root: TreeNode):
        if root is None:
            return
        
        self.inOrder(root.left)
        self.count[root.val] = self.count.get(root.val, 0) + 1
        self.inOrder(root.right)
        
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        self.inOrder(root)

        maximum = max(self.count.values())
        return [key for key, value in self.count.items() if value == maximum]
        