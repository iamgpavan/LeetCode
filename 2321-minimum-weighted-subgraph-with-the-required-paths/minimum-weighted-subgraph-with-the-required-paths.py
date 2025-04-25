import heapq
from collections import defaultdict
class Solution:
    def minimumWeight(self, n: int, edges: List[List[int]], src1: int, src2: int, dest: int) -> int:
        def dijiktra(n, graph, src):
            dist = [float('inf')]*n
            q = [(0, src)]

            while(q):
                curr_dist, curr_node = heapq.heappop(q)
                if(curr_dist > dist[curr_node]):
                    continue

                dist[curr_node] = curr_dist

                for adj_node, adj_dist in graph[curr_node]:
                    if(curr_dist + adj_dist < dist[adj_node]):
                        heapq.heappush(q, [curr_dist+adj_dist, adj_node])

            return dist

        g1 = defaultdict(list)
        g2 = defaultdict(list)

        for u, v, w in edges:
            g1[u].append([v, w])
            g2[v].append([u, w])
        
        dist_src_1 = dijiktra(n, g1, src1)
        dist_src_2 = dijiktra(n, g1, src2)
        dist_src_dest = dijiktra(n, g2, dest)

        ans = float('inf')

        for i in range(n):
            ans = min(ans, dist_src_1[i]+dist_src_2[i]+dist_src_dest[i])
        
        if(ans == float('inf')):
            return -1

        return ans