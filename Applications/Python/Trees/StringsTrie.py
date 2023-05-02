class Trie:
    class TrieNode:        
        def __init__(self):
            self.nodes = {}
            self.terminal = False
            
    def __init__(self):
        self.root = self.TrieNode()

    def insert(self, word: str) -> None:
        current = self.root
        
        for c in word:
            if(c not in current.nodes):
                current.nodes[c] = self.TrieNode()                
                
            current = current.nodes[c]
            
        current.terminal = True
                
    def search(self, word: str) -> bool:
        current = self.root
        
        for c in word:            
            if (c in current.nodes):
                current = current.nodes[c]
            else:
                return False
                       
        return True and current.terminal

    def startsWith(self, prefix: str) -> bool:
        current = self.root
        
        for c in prefix:            
            if (c in current.nodes):
                current = current.nodes[c]
            else:
                return False
        
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

obj = Trie()
obj.insert("apple")
print("Correct result is True, compared to: ", str(obj.search("apple")))
print("Correct result is False, compared to: ", str(obj.search("app")))
print("Correct result is True, compared to: ", str(obj.startsWith("app")))