class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        def validate(hashmap, word):
            hm = hashmap.copy()
            for char in word:
                if char not in hm or hm[char] == 0:
                    return False
                hm[char] -= 1
            return True
        
        hashmap = {}
        ans = 0
        
        for i in chars:
            hashmap[i] = hashmap.get(i, 0) + 1
        
        for word in words:
            # print(hashmap)
            if validate(hashmap, word):
                ans += len(word)
            
            
        return ans