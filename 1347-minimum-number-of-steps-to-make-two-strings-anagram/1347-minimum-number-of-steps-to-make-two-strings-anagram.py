class Solution:
    def minSteps(self, s: str, t: str) -> int:
        if(len(s) != len(t)):
            return 0
        
        hashmap = {}
        
        for i in s:
            hashmap[i] = hashmap.get(i, 0) + 1
        
        ans = 0
        for i in t:
            if i in hashmap and hashmap[i] != 0:
                hashmap[i] -= 1
            else:
                ans += 1
        
        return ans