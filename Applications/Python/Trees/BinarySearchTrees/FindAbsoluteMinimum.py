# Find absolute minimum
# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.absmin = float('inf')
        self.prev = None

    def inOrder(self, root):
        if root is None:
            return

        self.inOrder(root.left)

        if self.prev is not None:
            localmin = abs(root.val - self.prev.val)
            self.absmin = min(localmin, self.absmin)

        self.prev = root

        self.inOrder(root.right)

    def getMinimumDifference(self, root: TreeNode) -> int:
        self.inOrder(root)
        return self.absmin
