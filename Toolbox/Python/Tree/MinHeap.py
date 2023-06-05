class MinHeap:
    def __init__(self, size = 100) -> None:
        self._size = size
        self._nodes = [0]*self._size
        self._ptr = 0
        
    def peek(self):
        return self._nodes[1]

    def add(self, value):
        self._ptr += 1
        
        if self._ptr > self._size:
            raise("Heap has too many elements!")
        
        self._nodes[self._ptr] = value
        
        index = self._ptr
        parent = index // 2        
        while(parent > 0 and self._nodes[parent] > self._nodes[index]):
            self._nodes[parent], self._nodes[index] = self._nodes[index], self._nodes[parent]
            index = parent
            parent = index // 2        
    
    def pop(self):
        if self._ptr == 0:
            raise Exception("The heap is empty!")
        
        result = self._nodes[1]
        self._nodes[1] = self._nodes[self._ptr]
        self._nodes[self._ptr] = 0
        self._ptr -= 1
        
        index = 1
        if self._ptr == 2 and self._nodes[index] > self._nodes[index + 1]:
            self._nodes[index], self._nodes[index + 1] = self._nodes[index + 1], self._nodes[index]
            return result
        
        while index < self._ptr // 2:
            leftChild = index * 2
            rightChild = index * 2 + 1
            current = self._nodes[index]
            
            if self._nodes[leftChild] < current or self._nodes[rightChild] < current:
                if self._nodes[leftChild] < self._nodes[rightChild]:
                    self._nodes[leftChild], self._nodes[index] = self._nodes[index], self._nodes[leftChild]                    
                    index = leftChild
                else:
                    self._nodes[rightChild], self._nodes[index] = self._nodes[index], self._nodes[rightChild]                    
                    index = rightChild
            else:
                break
                    
        return result
        