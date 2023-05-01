class MinHeap:
    def __init__(self, heapSize) -> None:
        self.heapSize = heapSize
        self.heap = [0] * (heapSize + 1)
        self.realSize = 0
        
    def add(self, element):
        self.realSize += 1
        
        if self.realSize > self.heapSize:        
            print("Size of the collection exceeded!")
            self.realSize -= 1
            return
        
        self.heap[self.realSize] = element
        index = self.realSize
        parent = index // 2
        
        while (self.heap[index] < self.heap[parent] and index > 1):
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            index = parent
            parent = index // 2
    
    def peek(self):
        return self.heap[1]
    
    def size(self):
        return self.realSize
    
    def delete(self, element):               
        index = 1
        
        while index <= self.realSize:
            if self.heap[index] == element:
                self.heap[index] = self.heap[self.realSize]
                self.realSize -= 1
                break
            
            left = 2 * index
            right = 2 * index + 1
            
            if left > self.realSize:
                break
            
            if right > self.realSize:
                index = left
                break
            
            if self.heap[left] < self.heap[right]:
                index = left
            else:
                index = right

    
    def pop(self):
        if self.realSize < 1:
            print("Heap is empty")
            return    
        
        result = self.heap[1]        
        self.heap[1] = self.heap[self.realSize]
        self.realSize -= 1
        index = 1
        
        while index <= self.realSize // 2:
            left = index * 2
            right = index * 2 + 1
            
            if self.heap[index] > self.heap[left] or self.heap[index] > self.heap[right]:
                if self.heap[left] < self.heap[right]:
                    self.heap[left], self.heap[index] = self.heap[index], self.heap[left]
                    index = left
                else:
                    self.heap[right], self.heap[index] = self.heap[index], self.heap[right]
                    index = right                        
            else:
                break

        return result
                

def dijkstraNaive(graph, s):
    n = len(graph)
    vistied = [False] * n
    distances = [1e7] * n    
    distances[s] = 0
    
    for i in range(n):
        idx = findClosestVertex(distances, vistied)        
        vistied[idx] = True
                
        for adjV in graph[idx]:
            vertex = adjV[0]
            length = adjV[1]
            
            if vistied[vertex] == False and distances[vertex] > (distances[idx] + length):
                distances[vertex] = distances[idx] + length
        
    return distances
    
graph = [[(1, 2), (2, 3)], [(3, 1)], [(3, 4)], []]

print(dijkstraNaive(graph, 0))