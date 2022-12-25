import unittest

def MatrixPathMaximumProfit(m, n, profits):
    if m == 1 and n == 1:
        return (profits[0][0], [(0, 0)])
    
    maxProfit = [[0 for x in range(n)] for y in range(m)]
    maxProfit[0][0] = 1
    
    for x in range(m):
        for y in range(n):          
            maxProfit[x][y] = profits[x][y]
              
            if (x > 0 and y > 0):
                maxProfit[x][y] += max(maxProfit[x - 1][y], maxProfit[x][y - 1])
            elif (x > 0):
                maxProfit[x][y] += maxProfit[x - 1][y]
            elif (y > 0):
                maxProfit[x][y] += maxProfit[x][y - 1]                
                
    maxProfitablePath = calculatePath(maxProfit, m - 1, n - 1)
    return (maxProfit[m - 1][n - 1], maxProfitablePath)

def calculatePath(maxProfit, x, y):
    if x == 0 and y == 0:
        return [(0, 0)]
    elif x == 0:
        return calculatePath(maxProfit, x, y - 1) + [(x, y)]
    elif y == 0:
        return calculatePath(maxProfit, x - 1, y) + [(x, y)]
    else:
        if maxProfit[x - 1][y] > maxProfit[x][y - 1]:
            return calculatePath(maxProfit, x - 1, y) + [(x, y)]
        else:
            return calculatePath(maxProfit, x, y - 1) + [(x, y)]
    

class TestCases(unittest.TestCase):        
    def testCase1(self): 
        result = MatrixPathMaximumProfit(1, 1, self.profits)               
        self.assertEqual(result[0], 3, "Should be 3")
        
    def testCase2(self): 
        result = MatrixPathMaximumProfit(2, 2, self.profits)       
        self.assertEqual(result[0], 8, "Should be 8")
        
    def testCase3(self):
        result = MatrixPathMaximumProfit(3, 3, self.profits)
        self.assertEqual(result[0], 15, "Should be 15")        