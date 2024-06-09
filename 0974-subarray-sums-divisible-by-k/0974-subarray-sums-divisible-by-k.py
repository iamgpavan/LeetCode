class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        remainders = {0:1}
        currSum = 0
        ans = 0
        
        for num in nums:
            currSum += num
            
            if(currSum % k) in remainders:
                ans += remainders[(currSum % k)]
                remainders[(currSum % k)] += 1
            else:
                remainders[(currSum % k)] = 1
        
        return ans