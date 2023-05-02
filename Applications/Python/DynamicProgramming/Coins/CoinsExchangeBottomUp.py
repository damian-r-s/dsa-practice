#1, 3 cents
# n = 2 -> (1, 1) -> 1 way
# n = 3 -> (1, 1, 1), (3) -> 2 ways
# n = 4 -> (1, 1, 1, 1), (1, 3), (3, 1) -> 3 ways
# n = 5 -> (1, 1, 1, 1), (1, 1, 3), (1, 3, 1), (3, 1, 1) -> 4 ways
# Transition function f(n) = f(n - 1) + f(n - 3) + ... + f(n - k)

import unittest

def CoinsExchangeBottomUp(coins, n):    
    columns = n + 1
    result = [0 for x in range(columns)]
    result[0] = 1        
            
    for space in range(1, columns):
        for coin in coins:
            if space >= coin:
                result[space] += result[space - coin]
                    
    return result[columns - 1]
        
class TestCase(unittest.TestCase):
    def testCase1(self):
        result = CoinsExchangeBottomUp([1, 3], 1)
        self.assertEqual(result, 1, "Should be 1")
        
    def testCase2(self):
        result = CoinsExchangeBottomUp([1, 3], 3)
        self.assertEqual(result, 2, "Should be 2")
        
    def testCase3(self):
        result = CoinsExchangeBottomUp([1, 3], 5)
        self.assertEqual(result, 4, "Should be 4")
        
    def testCase4(self):
        result = CoinsExchangeBottomUp([1, 3, 5], 5)
        self.assertEqual(result, 5, "Should be 5")
        
    def testCase5(self):
        result = CoinsExchangeBottomUp([1, 3, 5, 10], 10)
        self.assertEqual(result, 48, "Should be 48")