# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:        
        if(root is None):
            True
        
        return self.isMirror(root.left, root.right)
                
    def isMirror(self, root1, root2):
        if(root1 is None and root2 is None):
            return True
        
        if(root1 is not None and root2 is not None and root1.val == root2.val):
            left = self.isMirror(root1.left, root2.right)
            right = self.isMirror(root2.left, root1.right)            
            return left and right        
        else:
            return False