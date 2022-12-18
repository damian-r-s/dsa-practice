def MatrixNumberOfPaths(m, n):
    if m == 1 and n == 1:
        return 1
    
    paths = [[0 for x in range(n)] for y in range(m)]
    paths[0][0] = 1
    
    for x in range(m):
        for y in range(n):            
            if (x > 0 and y > 0):
                paths[x][y] = paths[x - 1][y] + paths[x][y - 1]
            elif (x > 0):
                paths[x][y] = paths[x - 1][y]
            elif (y > 0):
                paths[x][y] = paths[x][y - 1]
                
                
    return paths[m - 1][n - 1]

print(MatrixNumberOfPaths(1, 1)) # 1           
print(MatrixNumberOfPaths(2, 2)) # 2
print(MatrixNumberOfPaths(3, 3)) # 6
print(MatrixNumberOfPaths(4, 4)) # 20
print(MatrixNumberOfPaths(4, 5)) # 35
print(MatrixNumberOfPaths(5, 4)) # 35
print(MatrixNumberOfPaths(5, 5)) # 70