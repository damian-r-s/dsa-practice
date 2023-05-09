import unittest
import RedBlackBinarySearchTree as BST

class RedBlackBinarySearchTreeUnitTests(unittest.TestCase):
    def setUp(self) -> None:
        self.bst = BST.RedBlackTree()
        
    def test_new_RedBlackTreeNode_has_red_color(self):
        node = BST.RedBlackTreeNode('a', 1)
        
        self.assertTrue(node.isRed())
        self.assertFalse(node.isBlack())
        
    def test_new_RedBlackTreeNode_has_markblack_color(self):
        node = BST.RedBlackTreeNode('a', 1)
        
        node.markBlack()
        
        self.assertTrue(node.isBlack())
        self.assertFalse(node.isRed())
        
if __name__ == '__main__':
    unittest.main()   
