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
        self.heap.add(12)
        self.heap.add(1)
        self.heap.add(15)
        
        min = self.heap.pop()      
        self.assertEqual(min, 1, 'Min element should have value 1!')
        
        min = self.heap.pop()      
        self.assertEqual(min, 4, 'Min element should have value 4!')
        
        min = self.heap.pop()      
        self.assertEqual(min, 6, 'Min element should have value 6!')
        
        min = self.heap.pop()      
        self.assertEqual(min, 8, 'Min element should have value 8!')
        
        min = self.heap.pop()      
        self.assertEqual(min, 10, 'Min element should have value 10!')
        
        min = self.heap.pop()      
        self.assertEqual(min, 12, 'Min element should have value 12!')
        
if __name__ == '__main__':
    unittest.main()   
