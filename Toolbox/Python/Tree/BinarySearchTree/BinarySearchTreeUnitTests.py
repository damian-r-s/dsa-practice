import unittest
import BinarySearchTree as BST

class BinarySearchTreeUnitTests(unittest.TestCase):
    def setUp(self) -> None:
        self.bst = BST.Tree()
        
    def test_empty_tree_has_size_zero(self):
        self.assertEqual(self.bst.size(), 0, 'Empty BTS must have size equal to zero!')
        
    def test_root_node_has_size_equal_to_one(self):
        self.bst.put('A', 1)
        self.assertEqual(self.bst.size(), 1, 'One node in the tree must have size equal to 1!')
        
    def test_root_node_has_size_equal_to_two_if_two_nodes_added(self):
        self.bst.put('A', 1)
        self.bst.put('B', 2)
        self.assertEqual(self.bst.size(), 2, 'Two nodes in the tree make the size of the tree equal to two!')
        
    def test_min_returns_none_if_tree_is_empty(self):        
        self.assertEqual(self.bst.min(), None, 'Minimum does not exist in empty tree!')
        
    def test_if_only_one_node_then_it_is_the_minimum(self):        
        self.bst.put('Z', 100)
        self.assertEqual(self.bst.min().key, 'Z', 'If only root present then minimum equals this node!')
        self.assertEqual(self.bst.min().val, 100, 'If only root present then minimum equals this node!')
        
    def test_minimum_is_found_correctly(self):        
        self.bst.put('r', 5)
        self.bst.put('m', 10)
        self.bst.put('o', 15)
        self.bst.put('p', 20)
        self.bst.put('z', 25)
        self.bst.put('a', 30)
        self.bst.put('b', 35)
        
        self.assertEqual(self.bst.min().key, 'a', 'Minimum key should be a')
        
    def test_max_returns_none_if_tree_is_empty(self):        
        self.assertEqual(self.bst.max(), None, 'Maximum does not exist if tree is empty!')
        
    def test_if_only_one_node_then_it_is_the_maximum(self):        
        self.bst.put('A', 100)
        self.assertEqual(self.bst.max().key, 'A', 'If only root present then maximum equals this node!')
        self.assertEqual(self.bst.max().val, 100, 'If only root present then maximum equals this node!')
        
    def test_maximum_is_found_correctly(self):        
        self.bst.put('r', 5)
        self.bst.put('m', 10)
        self.bst.put('o', 15)
        self.bst.put('p', 20)
        self.bst.put('z', 25)
        self.bst.put('a', 30)
        self.bst.put('b', 35)
        
        self.assertEqual(self.bst.max().key, 'z', 'Maximum key should be z')
        
    def test_floor_return_none_if_tree_is_empty(self):
        self.assertEqual(self.bst.floor('a'), None, 'If tree is empty then floor equals None!')
        
    def test_floor_is_on_the_left_found_correctly(self):
        self.bst.put('d', 5)
        self.bst.put('r', 10)
        self.bst.put('b', 15)
        self.bst.put('a', 20)
        
        self.assertEqual(self.bst.floor('c').key, 'b', 'The floor should be b!')
    
    def test_floor_is_on_the_right_found_correctly(self):
        self.bst.put('c', 5)
        self.bst.put('p', 15)
        self.bst.put('r', 20)
        self.bst.put('a', 25)
        self.bst.put('b', 30)        
        self.bst.put('o', 15)
        
        self.assertEqual(self.bst.floor('s').key, 'r', 'The floor should be r!')
        self.assertEqual(self.bst.floor('q').key, 'p', 'The floor should be o!')

    def test_ceil_returns_none_if_tree_is_empty(self):
        self.assertEqual(self.bst.ceil('a'), None, 'If tree is empty then ceil equals None!')
    
    def test_ceil_is_on_the_right_found_correctly(self):
        self.bst.put('e', 5)
        self.bst.put('b', 15)
        self.bst.put('a', 20)
        self.bst.put('c', 25)
        self.bst.put('h', 30)        
        self.bst.put('g', 35)
        self.bst.put('j', 35)
        
        self.assertEqual(self.bst.ceil('f').key, 'g', 'The ceil should be g!')
        self.assertEqual(self.bst.ceil('p'), None, 'The ceil should be None!')
        
    def test_select_k_nodes_lower_than(self):
        self.bst.put('e', 5)
        self.bst.put('b', 15)
        self.bst.put('a', 20)
        self.bst.put('c', 25)
        self.bst.put('h', 30)        
        self.bst.put('g', 35)
        self.bst.put('j', 35)
        
        node = self.bst.select(1)
        self.assertEqual(node.key, 'b', 'The only one key higher than 1 is b!')
        
        node = self.bst.select(15)
        self.assertEqual(node, None, 'There is no such key!')        
        
        node = self.bst.select(5)
        self.assertEqual(node.key, 'h', 'There is h key!')  
        
    def test_rank_empty_tree_equals_zero(self):        
        self.assertEqual(self.bst.rank('A'), 0, 'Must be zero for empty tree!')  
        
    def test_left_tree_rank_equals_subtree_size(self):        
        self.bst.put('e', 1)
        self.bst.put('b', 2)
        self.bst.put('a', 3)
        self.bst.put('c', 4)
        self.bst.put('h', 5)        
        self.bst.put('g', 6)
        self.bst.put('j', 7)
                
        self.assertEqual(self.bst.rank('e'), 3, 'Must be equal to 3!')  
        self.assertEqual(self.bst.rank('g'), 4, 'Must be equal to 5!')  
        
    def test_rank_the_maximum_node(self):        
        self.bst.put('e', 1)
        self.bst.put('b', 2)
        self.bst.put('a', 3)
        self.bst.put('c', 4)
        self.bst.put('h', 5)        
        self.bst.put('g', 6)
        self.bst.put('j', 7)
        
        self.assertEqual(self.bst.rank('k'), 7, 'Must be equal to 7!')
    
if __name__ == '__main__':
    unittest.main()   
