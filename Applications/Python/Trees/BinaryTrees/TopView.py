class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""
def topView(root):
    #Write your code here
    
    d = {}    
    def trav(root, key, level):
        if root != None:            
            if key not in d:
                d[key] = [root, level]                                
            elif d[key][1] > level:                
                d[key] = [root, level]
                
            trav(root.left, key - 1, level + 1)
            trav(root.right, key + 1, level + 1)
                
    
    trav(root, 0, 0)   
    
    for key in sorted(d):
        print(d[key][0], end = " ")
        
       

