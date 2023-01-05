# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return root
        
        if root.val == key:
            if root.left is None and root.right is None:
                return None            
            if root.left is not None and root.right is not None:
                if root.right.left is None and root.right.right is None:
                    root.val = root.right.val
                    root.right = None
                elif root.right.left is None and root.right.right is not None:
                    root.val = root.right.val
                    root.right = root.right.right                
                else:                                          
                    current = root.right
                    prev = current

                    while current.left is not None:
                        prev = current
                        current = current.left

                    root.val = current.val
                    if current.right is not None:                        
                        prev.left = current.right                        
                    else:
                        prev.left = None             
                    
                return root
            
            if root.left is None:                
                return root.right
            
            if root.right is None:                
                return root.left
                
        if root.val > key:
            root.left = self.deleteNode(root.left, key)            
        else:
            root.right = self.deleteNode(root.right, key)            
    
        return root 
                