class RedBlackTreeNode:
    def __init__(self, key=any, val=any) -> None:
        self.key = key
        self.val = val
        self.left: RedBlackTreeNode = None
        self.right: RedBlackTreeNode = None
        self.size = 1
        self.color = True # True means red, False means black
    
    def markBlack(self):
        self.color = False
        
    def markRed(self):
        self.color = True  
        
    def isRed(self):
        return self.color
    
    def isBlack(self):
        return not self.color      
        
class RedBlackTree:
    def __init__(self) -> None:
        self.root: RedBlackTreeNode = None
    
    def __isRed(self, node: RedBlackTreeNode):
        if node is None:
            return False
        return node.isRed()
    
    def __flipColors(self, root: RedBlackTreeNode):
        root.markRed()        
        if root.left is not None:
            root.left.markBlack()        
        if root.right is not None:
            root.right.markBlack()
    
    def size(self) -> int:
        return self.__size(self.root)
    
    def __size(self, root: RedBlackTreeNode) -> int:
        if root is None:
            return 0
        return root.size
    
    def __rotateRight(self, root: RedBlackTreeNode):
        left = root.left
        root.left = left.right
        left.right = root
        left.color = root.color
        root.markRed()
        left.size = root.size
        root.size = 1 + self.__size(root.left) + self.__size(root.right)
        return left
    
    def __rotateLeft(self, root: RedBlackTreeNode):
        right = root.right
        root.right = right.left
        right.left = root
        right.color = root.color
        root.markRed()
        right.size = root.size
        root.size = 1 + self.__size(root.left) + self.__size(root.right)        
        return right
    
    def put(self, key, value) -> None:
        self.root = self.__put(self.root, key, value)
        self.root.markBlack()
    
    def __put(self, root: RedBlackTreeNode, key, value) -> RedBlackTreeNode:
        if root is None:
            return RedBlackTreeNode(key, value) # by default Red
        
        if root.key < key:
            root.right = self.__put(root.right, key, value)            
        elif root.key > key:
            root.left = self.__put(root.left, key, value) 
        else:
            root.val = value
        
        if self.__isRed(root.right) and not self.__isRed(root.left):
            root = self.__rotateLeft(root)
        
        if self.__isRed(root.left) and self.__isRed(root.left.left):
            root = self.__rotateRight(root)
        
        if root.left.isRed() and root.right.isRed():
            self.__flipColors(root)
        
        root.size = 1 + self.__size(root.left) + self.__size(root.right)        
        return root        
        
    def get(self, key) -> any:
        return self.__get(self.root, key) 
    
    def __get(self, root: RedBlackTreeNode, key) -> any:
        if root is None:
            return None        
        if key == root.key:
            return root.val        
        if key < root.key:
            return self.__get(root.left, key)
        else:
            return self.__get(root.right, key)
  
    