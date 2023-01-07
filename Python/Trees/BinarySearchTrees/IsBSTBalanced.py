# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:    
    def height(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        lh = self.height(root.left)
        if lh == -1:
            return -1
        
        rh = self.height(root.right)
        if rh == -1:
            return -1
        
        if abs(lh - rh) > 1:
            return -1
        
        return max(lh, rh) + 1
    
    def isBalanced(self, root: Optional[TreeNode]) -> bool:                
        if root is None:
            return True
        
        result = self.height(root)
        
        if result == -1:
            return False
        
        return True