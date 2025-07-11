from collections import defaultdict
class Solution:
    def dfs(self, node, adj, visit, inStack):
        # If the node is already in the stack, we have a cycle.
        if inStack[node]:
            return True
        if visit[node]:
            return False
        # Mark the current node as visited and part of current recursion stack.
        visit[node] = True
        inStack[node] = True
        for neighbor in adj[node]:
            if self.dfs(neighbor, adj, visit, inStack):
                return True
        # Remove the node from the stack.
        inStack[node] = False
        return False

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # adj = [[] for _ in range(numCourses)]
        # for prerequisite in prerequisites:
        #     adj[prerequisite[1]].append(prerequisite[0])

        # visit = [False] * numCourses
        # inStack = [False] * numCourses
        # for i in range(numCourses):
        #     if self.dfs(i, adj, visit, inStack):
        #         return False
        # return True

        inDegree = [0]*numCourses
        graph = defaultdict(list)
        
        for course, prereq in prerequisites:
            graph[prereq].append(course)
            inDegree[course] += 1
        
        queue = []

        for node in range(numCourses):
            if(inDegree[node] == 0):
                queue.append(node)
        
        while(queue):
            node = queue.pop()

            for adjNode in graph[node]:
                inDegree[adjNode] -= 1
                if(inDegree[adjNode] == 0):
                    queue.append(adjNode)
        
        for node in range(numCourses):
            if(inDegree[node]):
                return False
        
        return True