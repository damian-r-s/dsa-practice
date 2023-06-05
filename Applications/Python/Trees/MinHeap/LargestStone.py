# 1046. Last Stone Weight
# You are given an array of integers stones where stones[i] is the weight of the ith stone.
# We are playing a game with the stones. On each turn, we choose the heaviest two stones and smash them together. Suppose the heaviest two stones have weights x and y with x <= y. The result of this smash is:

# If x == y, both stones are destroyed, and
# If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
# At the end of the game, there is at most one stone left.
# Return the weight of the last remaining stone. If there are no stones left, return 0.

class MaxHeap:
    def __init__(self, size = 100) -> None:
        self._size = size
        self._nodes = [0]*self._size
        self._ptr = 0
        
    def count(self):
        return self._ptr

    def peek(self):
        return self._nodes[1]

    def add(self, value):
        self._ptr += 1
        
        if self._ptr > self._size:
            raise("Heap has too many elements!")
        
        self._nodes[self._ptr] = value
        
        index = self._ptr
        parent = index // 2        
        while(parent > 0 and self._nodes[parent] < self._nodes[index]):
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
        if self._ptr == 2 and self._nodes[index] < self._nodes[index + 1]:
            self._nodes[index], self._nodes[index + 1] = self._nodes[index + 1], self._nodes[index]
            return result
        
        while index <= self._ptr // 2:
            leftChild = index * 2
            rightChild = index * 2 + 1
            current = self._nodes[index]
            
            if rightChild > self._ptr:
                break
            
            if self._nodes[leftChild] > current or self._nodes[rightChild] > current:
                if self._nodes[leftChild] > self._nodes[rightChild]:
                    self._nodes[leftChild], self._nodes[index] = self._nodes[index], self._nodes[leftChild]                    
                    index = leftChild
                else:
                    self._nodes[rightChild], self._nodes[index] = self._nodes[index], self._nodes[rightChild]                    
                    index = rightChild
            else:
                break
                    
        return result

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = MaxHeap(10000)

        for i in range(len(stones)):
            s = stones[i]
            heap.add(s)

        while heap.count() >= 2:
            f = heap.pop()
            s = heap.pop()

            if f != s:
                if f < s:
                    heap.add(s - f)
                else:
                    heap.add(f - s)


        if heap.count() != 0: 
            return heap.pop() 
        else: 
            return 0




