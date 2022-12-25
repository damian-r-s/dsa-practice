#1, 3 cents
# n = 2 -> (1, 1) -> 1 way
# n = 3 -> (1, 1, 1), (3) -> 2 ways
# n = 4 -> (1, 1, 1, 1), (1, 3), (3, 1) -> 3 ways
# n = 5 -> (1, 1, 1, 1), (1, 1, 3), (1, 3, 1), (3, 1, 1) -> 4 ways
# Transition function f(n) = f(n - 1) + f(n - 3) + ... + f(n - k)

import unittest

def CoinsExchangeTopDown(coins, n):
    memo = {}    
    memo[0] = 1
    return CoinsExchangeTopDownNested(coins, n, memo)

def CoinsExchangeTopDownNested(coins, n, memo):    
    if n < 0:
        return 0
    
    if n in memo:
        return memo[n]
        
    result = 0
    for coin in coins:
        result += CoinsExchangeTopDown(coins, n - coin)
    
    memo[n] = result    
    return result

class TestCase(unittest.TestCase):
    def testCase1(self):
        result = CoinsExchangeTopDown([1, 3], 1)
        self.assertEqual(result, 1, "Should be 1")
        
    def testCase2(self):
        result = CoinsExchangeTopDown([1, 3], 3)
        self.assertEqual(result, 2, "Should be 2")
        
    def testCase3(self):
        result = CoinsExchangeTopDown([1, 3], 5)
        self.assertEqual(result, 4, "Should be 4")
        
    def testCase4(self):
        result = CoinsExchangeTopDown([1, 3, 5], 5)
        self.assertEqual(result, 5, "Should be 5")
        
    def testCase5(self):
        result = CoinsExchangeTopDown([1, 3, 5, 10], 10)
        self.assertEqual(result, 48, "Should be 48")