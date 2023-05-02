# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        stack = []
        current = float('-inf')
        
        while root is not None or len(stack) != 0:            
            while root is not None:
                stack.append(root)
                root = root.left
                
            root = stack.pop()
            if root.val <= current:
                return False
            
            current = root.val
            root = root.right
        
        return True