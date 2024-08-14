class Solution:
    def nNatural(self, n):
        return (n*(n+1))//2
    def minimalKSum(self, nums: List[int], k: int) -> int:
        nums.sort()
        
        ans = 0
        
        if(nums[0] > 0):
            high = min(k, nums[0]-1)

            ans += (self.nNatural(high))
            k -= high
        
        for i in range(len(nums)):
            if(nums[i] > nums[i-1]+1):
                low = nums[i-1]
                high = min(nums[i]-1, nums[i-1]+k)
                
                ans += (self.nNatural(high) - self.nNatural(low))
                k -= (high - low)
                if(k <= 0):
                    break
        
        if(k > 0):
            
            low = nums[-1]
            high = low + k

            ans += (self.nNatural(high) - self.nNatural(low))
        
        return ans