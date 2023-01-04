import queue

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: TreeNode):
        if(root is None):
            return []
        
        fifo = queue.Queue()                
        fifo.put(root)                
        
        result = []        
        while(fifo.empty() == False):                                  
            size = fifo.qsize()
            sub = []
            for _ in range(size):
                current = fifo.get()
                sub.append(current.val)
                if(current.left is not None):
                    fifo.put(current.left)                    
                if(current.right is not None):
                    fifo.put(current.right)                   
            
            result.append(sub)       
        
        return result