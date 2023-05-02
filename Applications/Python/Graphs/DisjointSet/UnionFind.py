class UnionFind:
    def __init__(self, size) -> None:
        self.root = [i for i in range(size)]
        self.rank = [0 for i in range(size)]
        
    def find(self, x):
        while x != self.root[x]:
            x = self.root[x]            
        return x
    
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.rank[rootY] > self.rank[rootX]:
                self.root[rootX] = rootY
            else:
                self.root[rootY] = rootX
                self.rank[rootX] += 1
                
    def connected(self, x, y):
        return self.find(x) == self.find(y)


algo = UnionFind(10)
algo.union(3, 2)
algo.union(3, 5)

print(algo.connected(3, 2))
print(algo.connected(3, 5))
print(algo.connected(1, 5))
print(algo.connected(1, 8))
