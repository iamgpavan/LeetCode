class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        inDegree = [0]*numCourses
        graph = defaultdict(list)
        
        for course, prereq in prerequisites:
            graph[prereq].append(course)
            inDegree[course] += 1
        
        queue = []
        ans = []

        for node in range(numCourses):
            if(inDegree[node] == 0):
                queue.append(node)
                ans.append(node)
        
        if(not queue):
            return []
        
        while(queue):
            node = queue.pop()

            for adjNode in graph[node]:
                inDegree[adjNode] -= 1
                if(inDegree[adjNode] == 0):
                    queue.append(adjNode)
                    ans.append(adjNode)
        # print(inDegree)
        for node in range(numCourses):
            if(inDegree[node]):
                return []
        
        return ans