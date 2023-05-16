import unittest
import MinHeap as heap

class BinarySearchTreeUnitTests(unittest.TestCase):
    def setUp(self) -> None:
        self.heap = heap.MinHeap(100)
        
    def test_min_element_is_on_the_toop(self):
        self.heap.add(10)
        self.heap.add(4)
        self.heap.add(8)
        self.heap.add(6)
        
        min = self.heap.pop()      
        self.assertEqual(min, 4, 'Min element should have value 4!')
        
        min = self.heap.pop()      
        self.assertEqual(min, 6, 'Min element should have value 6!')
        
if __name__ == '__main__':
    unittest.main()   
