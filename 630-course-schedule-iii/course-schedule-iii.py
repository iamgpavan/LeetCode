
class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key = lambda x:x[1])
        pq = []

        max_day = 0

        for day, endDay in courses:
            max_day += day
            heapq.heappush(pq, -day)

            if(max_day > endDay):
                max_day -= (-1*heapq.heappop(pq))
        
        return len(pq)
