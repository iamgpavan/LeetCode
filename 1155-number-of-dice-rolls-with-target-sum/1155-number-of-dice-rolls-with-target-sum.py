class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        dp = {}
        def helper(n, k, target):
            if(n == 0):
                if(target == 0):
                    return 1
                return 0
            
            if (n, target) in dp:
                return dp[(n, target)]

            ans = 0

            for i in range(1, k+1):
                ans += helper(n-1, k, target-i)
                ans %= 10**9 + 7
                
            dp[(n,target)] = ans

            return ans
        
        
        
        return helper(n, k, target)