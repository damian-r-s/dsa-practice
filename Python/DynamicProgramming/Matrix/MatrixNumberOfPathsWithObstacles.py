def MatrixNumberOfPaths(m, n, obstacles):
    if m == 1 and n == 1:
        return 1
    
    paths = [[0 for x in range(n)] for y in range(m)]
    paths[0][0] = 1
    
    for x in range(m):
        for y in range(n):                        
            if (x > 0 and y > 0):
                paths[x][y] = Cell(x - 1, y, paths, obstacles) + Cell(x, y - 1, paths, obstacles)
            elif (x > 0):
                paths[x][y] = Cell(x - 1, y, paths, obstacles)
            elif (y > 0):
                paths[x][y] = Cell(x, y - 1, paths, obstacles)
                
    return paths[m - 1][n - 1]

def Cell(x, y, paths, obstacles):
    if (obstacles[x][y] == 0):
        return paths[x][y]    
    return 0

obstacles = [[0 for x in range(10)] for y in range(10)]
obstacles[1][2] = 1
obstacles[1][3] = 1
obstacles[2][1] = 1
obstacles[3][3] = 1
obstacles[3][3] = 1

print(MatrixNumberOfPaths(1, 1, obstacles)) # 1           
print(MatrixNumberOfPaths(2, 2, obstacles)) # 2
print(MatrixNumberOfPaths(3, 3, obstacles)) # 0
print(MatrixNumberOfPaths(4, 4, obstacles)) # 1
print(MatrixNumberOfPaths(4, 5, obstacles)) # 1
print(MatrixNumberOfPaths(5, 4, obstacles)) # 3
print(MatrixNumberOfPaths(5, 5, obstacles)) # 4