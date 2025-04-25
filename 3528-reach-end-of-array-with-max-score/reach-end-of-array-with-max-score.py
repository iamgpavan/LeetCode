class Solution:
    def findMaximumScore(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        maxi = 0

        for i in range(n):
            ans += maxi
            maxi = max(maxi, nums[i])
        
        return ans