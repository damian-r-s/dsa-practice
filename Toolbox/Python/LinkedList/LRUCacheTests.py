import unittest
import LRUCache as cache

class LRUCacheUnitTests(unittest.TestCase):
    def setUp(self) -> None:
        self.lru = cache.LRUCache(5)
        self.lru.put(1, 1)
        self.lru.put(2, 2)
        self.lru.put(3, 3)
        self.lru.put(4, 4)
        self.lru.put(5, 5)
        
    def test_if_not_present_return_minus_one(self):        
        val = self.lru.get(9)
        self.assertEqual(val, -1, 'Frist element should not be present any more!')
        
    def test_if_size_exceeded_then_new_added_element_remove_last_item(self):        
        self.lru.put(6, 6)
        
        val = self.lru.get(6)
        self.assertEqual(val, 6, '6 must be present in the chache!')
        
        val = self.lru.get(1)
        self.assertEqual(val, -1, '1 does not exist any more in the chache!')
        
if __name__ == '__main__':
    unittest.main()   
