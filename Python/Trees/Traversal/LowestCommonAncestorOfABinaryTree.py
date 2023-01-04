# Definition for a binary tree node.
# Example root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:    
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':        
        if root is None:
            return None
        
        if root.val == p.val:
            return root
        
        if root.val == q.val:
            return root
                
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        if left != None and right != None:
            return root
        
        if left == None and right != None:
            return right
        
        if left != None and right == None:
            return left
        
        return None