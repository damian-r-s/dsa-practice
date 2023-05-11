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
        
    def test_root_node_has_size_equal_to_one(self):
        self.bst.put('A', 1)
        
        self.assertEqual(self.bst.size(), 1, 'One node in the tree must have size equal to 1!')
        
    def test_root_node_has_size_equal_to_two_if_two_nodes_added(self):
        self.bst.put('A', 1)
        self.bst.put('B', 2)
        self.bst.put('C', 3)
        
        self.assertEqual(self.bst.size(), 3, 'Two nodes in the tree make the size of the tree equal to two!')
        
    def test_delete_minimum(self):        
        self.bst.put('C', 3)
        self.bst.put('B', 2)        
        self.bst.put('A', 1)
        self.bst.put('D', 4)
        self.bst.put('E', 5)
        
        self.bst.deleteMin()
        
        self.assertEqual(self.bst.size(), 4, 'Size should be 4!')                
        self.assertEqual(self.bst.get('A'), None, 'Node "A" should not be present!')
        
    def test_delete_minimum_if_only_one_node_exist(self):                
        self.bst.put('B', 1)
        
        self.bst.deleteMin()
        
        self.assertEqual(self.bst.size(), 0, 'Size should be 1!')
        self.assertEqual(self.bst.get('B'), None, 'Node "A" should not be present!')
        
    def test_contains_key_check(self):
        self.bst.put('A', 1)
        self.bst.put('B', 2)
        self.bst.put('C', 3)
        self.bst.put('Z', 4)
        self.bst.put('M', 5)
        
        self.assertTrue(self.bst.contains('Z'), 'Z key must be present in this tree!')
        self.assertTrue(self.bst.contains('M'), 'M key must be present in this tree!')
        self.assertTrue(self.bst.contains('C'), 'C key must be present in this tree!')
        
        self.assertFalse(self.bst.contains('L'), 'L key must not be present in this tree!')
        self.assertFalse(self.bst.contains('G'), 'G key must not be present in this tree!')
        self.assertFalse(self.bst.contains('S'), 'S key must not be present in this tree!')
    
    # def test_delete_key(self):
    #     self.bst.put('A', 1)
    #     self.bst.put('B', 2)
    #     self.bst.put('C', 3)
    #     self.bst.put('D', 4)
    #     self.bst.put('E', 5)
    #     self.bst.put('Z', 6)
    #     self.bst.put('M', 7)
        
    #     self.bst.delete('D')
    #     self.assertFalse(self.bst.contains('D'), 'D key cannot be present!')
    #     self.assertEqual(self.bst.size(), 6, 'Size must be eqal 5!')
        
    #     self.bst.delete('E')
    #     self.assertFalse(self.bst.contains('E'), 'E key cannot be present!')
    #     self.assertEqual(self.bst.size(), 5, 'Size must be eqal 4!')
        
    #     self.bst.delete('B')
    #     self.assertFalse(self.bst.contains('B'), 'E key cannot be present!')
    #     self.assertEqual(self.bst.size(), 4, 'Size must be eqal 3!')
        
        
if __name__ == '__main__':
    unittest.main()   
