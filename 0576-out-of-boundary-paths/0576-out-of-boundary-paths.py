class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        dp = {}
        def helper(m, n, moves, i, j):
            
            if(i<0 or i==m or j<0 or j==n):
                return 1
            if(moves == 0):
                return 0
            
            if((i,j,moves) in dp):
                return dp[(i,j,moves)]
            
            dp[(i,j,moves)] = helper(m, n, moves-1, i, j-1) + helper(m, n, moves-1, i, j+1) + helper(m, n, moves-1, i-1, j) + helper(m, n, moves-1, i+1, j)
            
            return dp[(i, j, moves)]%(10**9 + 7)
        
        return helper(m, n, maxMove, startRow, startColumn)