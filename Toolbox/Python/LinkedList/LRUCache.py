class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.last = Node(0, 0)
        self.first = Node(0, 0)
        self.last.next, self.first.prev = self.first, self.last

    def remove(self, node):
        prev = node.prev
        next = node.next

        prev.next = next
        next.prev = prev
    
    def append(self, node):
        prev = self.first.prev
        prev.next = node
        self.first.prev = node

        node.prev = prev        
        node.next = self.first

    def get(self, key: int) -> int:
        if  key not in self.cache:
            return -1

        node = self.cache[key]               
        self.remove(node)
        self.append(node)

        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)       
        
        node = Node(key, value)
        self.cache[key] = node
        self.append(node)
        
        if len(self.cache) > self.cap:
            node = self.last.next
            del self.cache[node.key]
            self.remove(node)           

class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None