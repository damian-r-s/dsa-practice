

class TreeNode:
    def __init__(self, key=None, val=any, size=0, left=None, right=None) -> None:
        self.key = key
        self.val = val
        self.left = left
        self.right = right
        self.size = size
        
class Tree:
    def __init__(self) -> None:
        self.root = None
    
    def put(self, key, value) -> None:
        self.root = self.__put(self.root, key, value)
    
    def __put(self, root: TreeNode, key, value) -> TreeNode:
        if root is None:
            return TreeNode(key, value, 1)
        
        if root.key == key:
            root.val = value
        elif key < root.key:
            root.left = self.__put(root.left, key, value)
        else:
            root.right = self.__put(root.right, key, value)            
        
        root.size = self.__size(root.left) + self.__size(root.right) + 1
                
        return root   
        
    def get(self, key) -> TreeNode:
        return self.__get(self.root, key) 
    
    def __get(self, root: TreeNode, key) -> any:
        if root is None:
            return None
        
        if key == root.key:
            return root.val
        
        if key < root.key:
            return self.__get(root.left, key)
        else:
            return self.__get(root.right, key)
        
    def size(self):
        return self.__size(self.root)
        
    def __size(self, root: TreeNode):
        if root is None:
            return 0
        
        return root.size
        
        
tree = Tree()

tree.put('s', 0)
tree.put('e', 1)
tree.put('a', 2)
tree.put('r', 3)
tree.put('c', 4)
tree.put('h', 5)

print(tree.size())
