import unittest

# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:    
    def buildTree(self, inorder, postorder):
        l = len(inorder)
        
        if l == 0:
            return None
        
        if l == 1:
            root = TreeNode()
            root.val = inorder[0]
            return root
        
        rootIdx, delIdx = self.findRoot(inorder, postorder)
        del postorder[delIdx]  
        
        if rootIdx == -1:
            return None
        
        root = TreeNode()
        root.val = inorder[rootIdx]  
        root.left = self.buildTree(inorder[0:rootIdx], postorder)
        root.right = self.buildTree(inorder[rootIdx + 1:l], postorder)
        
        return root
    
    def findRoot(self, inorder, postorder):
        result = -1
        
        for i in range(len(postorder) - 1, 0, -1):
            try:
                searchedValue = postorder[i]
                result = inorder.index(searchedValue)
                return (result, i)
            except ValueError:
                result = -1
                
        return result


class TestCase(unittest.TestCase):    
    def testCase1(self):
        inorder = [9,3,15,20,7]
        postorder = [9,15,7,20,3]
        solutoin = Solution()
        
        treeRoot = solutoin.buildTree(inorder, postorder)
        
        self.assertEqual(treeRoot.val, 3, "Should be 3")
        self.assertEqual(treeRoot.left.val, 9, "Should be 9")
        self.assertEqual(treeRoot.right.val, 20, "Should be 20")
        self.assertEqual(treeRoot.right.left.val, 15, "Should be 15")
        self.assertEqual(treeRoot.right.right.val, 7, "Should be 7")