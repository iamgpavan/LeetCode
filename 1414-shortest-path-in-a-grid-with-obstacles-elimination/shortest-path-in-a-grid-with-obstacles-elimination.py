from collections import deque

class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m = len(grid)
        n = len(grid[0])

        if k >= m + n - 2:
            return m + n - 2

        dx = [-1, 0, 1, 0]
        dy = [0, 1, 0, -1]
        vis = {}

        q = deque([(0, 0, 0, k)])

        while(q):
            x, y, steps, k_left = q.popleft()
            if(x == m-1 and y == n-1):
                return steps
            
            if((x, y) in vis) and vis[(x, y)] >= k_left:
                continue

            vis[(x, y)] =  k_left

            for _ in range(4):
                i = x + dx[_]
                j = y + dy[_]

                if(0<=i<m) and (0<=j<n):
                    new_k = k_left - grid[i][j]

                    if(k_left >=0 and (i, j, k_left) not in vis):
                        q.append([i, j, steps+1, new_k])
                    
        return -1
