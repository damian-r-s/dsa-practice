import unittest

# 1 - even
# 0 - odd
def ExchangeEvenNumberOfCoins(coins, n, even):
    
    result = [[0 for y in range(2)] for x in range(n + 1)]    
    result[0][1] = 1
    
    for i in range(1, n + 1):
        for c in coins:
            if i - c >= 0:
                result[i][0] += result[i - c][1]
                result[i][1] += result[i - c][0]
    
    return result[n][even]    

print(ExchangeEvenNumberOfCoins([1, 3, 5, 10], 10, 1))    

class TestCase(unittest.TestCase):
    def testCase1(self):
        result = ExchangeEvenNumberOfCoins([1, 3, 5, 10], 1, 1)
        self.assertEqual(result, 0, "Should be 0")
        
    def testCase2(self):
        result = ExchangeEvenNumberOfCoins([1, 3, 5, 10], 10, 1)
        self.assertEqual(result, 47, "Should be 47")
        
    def testCase3(self):
        result = ExchangeEvenNumberOfCoins([1, 3, 5, 10], 4, 1)
        self.assertEqual(result, 3, "Should be 3")
        
    def testCase4(self):
        result = ExchangeEvenNumberOfCoins([1, 3, 5, 10], 6, 1)
        self.assertEqual(result, 8, "Should be 8")
        
    def testCase5(self):
        result = ExchangeEvenNumberOfCoins([1, 3, 5, 10], 5, 0)
        self.assertEqual(result, 5, "Should be 5")
        
    def testCase6(self):
        result = ExchangeEvenNumberOfCoins([1, 3, 5, 10], 3, 0)
        self.assertEqual(result, 2, "Should be 2")