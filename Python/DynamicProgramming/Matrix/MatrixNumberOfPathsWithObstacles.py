def MatrixNumberOfPaths(m, n, profits):
    if m == 1 and n == 1:
        return profits[0][0]
    
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
                
    return maxProfit[m - 1][n - 1]

profits = [[0 for x in range(10)] for y in range(10)]
profits[0][0] = 3
profits[0][1] = 2
profits[1][0] = 4
profits[1][1] = 1
profits[1][2] = 5
profits[2][1] = 5
profits[2][2] = 2
profits[3][3] = 3
profits[4][4] = 4
profits[1][3] = 1
profits[3][1] = 4
profits[3][2] = 4
profits[2][3] = 4
profits[3][4] = 6
profits[4][3] = 6

print(MatrixNumberOfPaths(1, 1, profits)) # 3           
print(MatrixNumberOfPaths(2, 2, profits)) # 2
print(MatrixNumberOfPaths(3, 3, profits)) # 0
print(MatrixNumberOfPaths(4, 4, profits)) # 1
print(MatrixNumberOfPaths(4, 5, profits)) # 1
print(MatrixNumberOfPaths(5, 4, profits)) # 3
print(MatrixNumberOfPaths(5, 5, profits)) # 4