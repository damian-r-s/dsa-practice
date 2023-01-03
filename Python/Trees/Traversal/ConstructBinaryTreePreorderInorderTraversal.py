import unittest

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def buildTree(self, preorder, inorder):        
        length = len(inorder)
        
        if length == 0:
            return None
                
        (rootIdx, middleIdx) = self.findMiddle(preorder, inorder)      
        
        rootValue = preorder[rootIdx]       
        del preorder[rootIdx] # remove root from preorder list
        
        leftPart = inorder[0:middleIdx]        
        rightPart = inorder[middleIdx + 1: length]
        
        root = TreeNode()
        root.val = rootValue        
        root.left = self.buildTree(preorder, leftPart)
        root.right = self.buildTree(preorder, rightPart)
        
        return root
                
    def findMiddle(self, preorder, inorder):
        result = 0
        
        for idx in range(len(preorder)):
            try:
                root = preorder[idx]
                return (idx, inorder.index(root))
            except ValueError:
                result = -1
        
        return result
        
class TestCase(unittest.TestCase):    
    def testCase1(self):
        preorder = [3,9,20,15,7]
        inorder = [9,3,15,20,7]
        solutoin = Solution()
        
        treeRoot = solutoin.buildTree(preorder, inorder)
        
        self.assertEqual(treeRoot.val, 3, "Should be 3")
        self.assertEqual(treeRoot.left.val, 9, "Should be 9")
        self.assertEqual(treeRoot.right.val, 20, "Should be 20")
        self.assertEqual(treeRoot.right.left.val, 15, "Should be 15")
        self.assertEqual(treeRoot.right.right.val, 7, "Should be 7")       