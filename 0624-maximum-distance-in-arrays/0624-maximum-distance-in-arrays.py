class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        first_max = arrays[0][-1]
        first_max_from = 0
        
        first_min = arrays[0][0]
        first_min_from = 0
        
        for i in range(len(arrays)):
            if(arrays[i][0] < first_min):
                first_min = arrays[i][0]
                first_min_from = i
            if(arrays[i][-1] > first_max):
                first_max = arrays[i][-1]
                first_max_from = i
            
        second_max = -10**5
        second_max_from = -1
        
        second_min = 10**5
        second_min_from = -1

        for i in range(len(arrays)):
            if((i != first_min_from or arrays[i][0] > first_min) and arrays[i][0] < second_min):
                second_min = arrays[i][0]
                second_min_from = i
            if((i != first_max_from or arrays[i][-1] < first_max) and arrays[i][-1] > second_max):
                second_max = arrays[i][-1]
                second_max_from = i
                
        

        if(first_min_from != first_max_from):
            return abs(first_max-first_min)

        
        
        # if(first_max_from != second_min_from):
        #     return abs(first_max-second_min)
        
        return max(abs(first_max - second_min), abs(second_max - first_min))
        
        