class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[-1 for j in range(len(text2))] for i in range(len(text1))]
        # print(dp)
        
        def fun(s1, s2, n, m):
            if(n<0 or m<0):
                return 0
            # print(n,m)
            if(dp[n][m] != -1):
                return dp[n][m]
            
            if(s1[n] == s2[m]):
                dp[n][m] = 1 + fun(s1, s2, n-1, m-1)
            else:
                dp[n][m] =  max(fun(s1, s2, n-1, m), fun(s1, s2, n, m-1))
            
            return dp[n][m]
        
        return fun(text1, text2, len(text1)-1, len(text2)-1)