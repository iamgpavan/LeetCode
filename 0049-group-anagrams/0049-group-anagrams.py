class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        
        for word in strs:
            frequencies = [0]*26
            
            for letter in word:
                frequencies[ord(letter) - ord('a')] += 1
            
            res[tuple(frequencies)].append(word)
        
        return res.values()