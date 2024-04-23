class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if(n == 1):
            return [0]
        
        degree = [0 for _ in range(n)]
        adj = [[] for _ in range(n)]
        
        for u,v in edges:
            degree[u] += 1
            degree[v] += 1
            
            adj[u].append(v)
            adj[v].append(u)
        
        q = []
        
        for node in range(n):
            if(degree[node] == 1):
                q.append(node)
        
        while(n > 2):
            size = len(q)
            n -= size
            
            while(size):
                node = q.pop(0)
                
                for adj_node in adj[node]:
                    degree[adj_node] -= 1
                    if(degree[adj_node] == 1):
                        q.append(adj_node)
                 
                size -= 1
        
        return q
        
        