class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        hashmap = {}
        for i in nums:
            hashmap[i] = hashmap.get(i,0) + 1
        
        ans = []
        
        while len(hashmap) != 0:
            vals = []
            for k in list(hashmap.keys()):
                if(hashmap[k] == 0):
                    hashmap.pop(k)
                else:
                    vals.append(k)
                    hashmap[k] -= 1
            if(len(vals) > 0):
                ans.append(vals)
            
        return ans