class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.cnt = 1
        self.left = left
        self.right = right

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        if len(nums) == 0:
            self.root = None
            return
            
        self.root = TreeNode(nums[0])        
        for num in nums[1:]:
            self.construct(self.root, num)
    
    def construct(self, root: TreeNode, val: int):
        if root is None:
            return TreeNode(val)
        
        root.cnt += 1        
        if root.val >= val:
            root.left = self.construct(root.left, val)
        else:
            root.right = self.construct(root.right, val)
            
        return root
    
    def find(self, root: TreeNode, k: int):
        left = 0
        if  root.left is not None:
            left = root.left.cnt
                    
        if  0 == root.cnt - left - k:
            return root.val
        
        if root.right is not None and root.right.cnt >= k:            
            return self.find(root.right, k)        
        
        right = 0
        if root.right is not None:
            right = root.right.cnt        
        
        return self.find(root.left, k - right - 1)
    
    def add(self, val: int) -> int:
        if self.root == None:
            self.root = TreeNode(val)
        else:
            self.construct(self.root, val)        
                
        kth = self.find(self.root, self.k)        
        return kth        