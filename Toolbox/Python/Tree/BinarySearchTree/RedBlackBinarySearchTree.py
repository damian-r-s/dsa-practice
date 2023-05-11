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
    
    def isEmpty(self):
        return self.root is None
    
    def contains(self, key):
        return self.get(key) is not None
    
    def __isRed(self, node: RedBlackTreeNode):
        if node is None:
            return False
        return node.isRed()
    
    def __isBlack(self, node: RedBlackTreeNode):
        if node is None:
            return False
        return node.isBlack()
    
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
        
        if self.__isRed(root.right) and self.__isRed(root.left) != True:
            root = self.__rotateLeft(root)
        
        if self.__isRed(root.left) and self.__isRed(root.left.left):
            root = self.__rotateRight(root)
        
        if self.__isRed(root.left) and self.__isRed(root.right):
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
    
    def __moveRedLeft(self, root: RedBlackTreeNode) -> RedBlackTreeNode:
        current = root        
        self.__flipColors(current)
        
        if self.__isRed(current.right.left):
            current.right = self.__rotateRight(current.right)
            current = self.__rotateLeft(current)
            self.__flipColors(current)
            
        return current
    
    def __moveRedRight(self, root: RedBlackTreeNode) -> RedBlackTreeNode:
        current = root        
        self.__flipColors(current)        
        if self.__isRed(current.left.left):            
            current = self.__rotateRight(current)
            self.__flipColors(current)
            
        return current
  
    def deleteMin(self):
        if self.isEmpty():
            return
        
        if self.__isBlack(self.root.left) and self.__isBlack(self.root.right):            
            self.root.markRed()
        
        self.root = self.__deleteMin(self.root)        
        
        if self.isEmpty() != True:
            self.root.markBlack()
                
    def __deleteMin(self, root: RedBlackTreeNode):
        current = root        
        if current.left is None:
            return None
        
        if self.__isBlack(current.left) and self.__isBlack(current.left.left):
            current = self.__moveRedLeft(current)
            
        current.left = self.__deleteMin(current.left)
        return self.balance(current)            
        
    def balance(self, root: RedBlackTreeNode) -> RedBlackTreeNode:        
        currentRoot = root        
        if self.__isBlack(currentRoot.left) and self.__isRed(currentRoot.right):
            currentRoot = self.__rotateLeft(currentRoot)
        if self.__isRed(currentRoot.left) and self.__isRed(currentRoot.left.left):
            currentRoot = self.__rotateRight(currentRoot)
        if self.__isRed(currentRoot.left) and self.__isRed(currentRoot.right):
            self.__flipColors(currentRoot)
            
        currentRoot.size = 1 + self.__size(currentRoot.left) + self.__size(currentRoot.right)
        return currentRoot
    
    def min(self):
        if self.isEmpty():
            return None        
        return self.__min(self.root)
    
    def __min(self, root: RedBlackTreeNode):
        if root.left is None:
            return root
        return self.__min(root.left)
        
    # def delete(self, key: any):
    #     if self.contains(key) != True:
    #         return
        
    #     if self.__isRed(self.root.left) != True and self.__isRed(self.root.right) != True:
    #         self.root.markRed()
            
    #     self.root = self.__delete(self.root, key)
        
    #     if self.isEmpty() != True:
    #         self.root.markBlack()
    
    # def __delete(self, root: RedBlackTreeNode, key: any) -> RedBlackTreeNode:
    #     current = root        
    #     if key < current.key:
    #         if self.__isRed(current.left) != True and self.__isRed(current.left.left) != True:
    #             current = self.__moveRedLeft(current)
    #         current.left = self.__delete(current.left, key)
    #     else:
    #         if self.__isRed(current.left):
    #             current = self.__rotateRight(current)
    #         if key == current.key and current.right is None:
    #             return None
    #         if self.__isRed(current.right) != True and self.__isRed(current.right.left) != True:
    #             current = self.__moveRedRight(current)
    #         if key == current.key:
    #             node = self.__min(current.right)
    #             current.key = node.key
    #             current.val = node.val
    #             current.right = self.__deleteMin(current.right)
    #         else:
    #             current.right = self.__delete(current.right, key)
                
    #     return self.balance(current)
            