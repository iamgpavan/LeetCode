class Solution:
    def validPath(self, n: int, E: List[List[int]], src: int, dst: int) -> bool:
        if src == dst : return True
        
        G = defaultdict(set)
        for u,v in E : G[u].add(v), G[v].add(u)

        seen = set()
        
        def dfs(u):
            return u == dst or any(dfs(v) for v in G[u] 
                                   if v not in seen and 
                                   seen.add(v) is None)
                
        return dfs(src)