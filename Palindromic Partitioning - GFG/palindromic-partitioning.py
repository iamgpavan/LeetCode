#User function Template for python3

class Solution:
    def palindromicPartition(self, s):
        n = len(s)
        is_palindrome = [[False] * n for _ in range(n)]

        for i in range(n):
            is_palindrome[i][i] = True

        for length in range(2, n + 1):
            for start in range(n - length + 1):
                end = start + length - 1
                if length == 2:
                    is_palindrome[start][end] = s[start] == s[end]
                else:
                    is_palindrome[start][end] = s[start] == s[end] and is_palindrome[start + 1][end - 1]

        dp = [0] * n

        for end in range(n):
            min_cuts = float('inf')
            for start in range(end + 1):
                if is_palindrome[start][end]:
                    if start == 0:
                        min_cuts = 0
                    else:
                        min_cuts = min(min_cuts, dp[start - 1] + 1)
            dp[end] = min_cuts

        return dp[n - 1]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range (t):
        string = input()
        
        ob = Solution()
        print(ob.palindromicPartition(string))
# } Driver Code Ends