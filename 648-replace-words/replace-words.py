class TrieNode:
    def __init__(self):
        self.isEnd = False
        self.child = [None]*26

class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word):
        dummy = self.root
        
        for character in word:
            ind = abs(ord('a')-ord(character))
            
            if(dummy.child[ind] == None):
                newTrie = TrieNode()
                dummy.child[ind] = newTrie
            
            dummy = dummy.child[ind]
        
        dummy.isEnd = True
    
    def search(self, word):
        dummy = self.root
        
        for i in range(len(word)):
            character = word[i]
            ind = abs(ord('a')-ord(character))
            
            if(dummy.child[ind] == None):
                return word
            
            if(dummy.child[ind].isEnd):
                return word[:i+1]
            
            dummy = dummy.child[ind]
        
        return word
    
class Solution:        
    
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = Trie()
        
        for word in dictionary:
            trie.insert(word)
        
        ans = []
        
        for word in sentence.split():
            ans.append(trie.search(word))
        
        return " ".join(ans)
            