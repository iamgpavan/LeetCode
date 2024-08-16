class Solution(object):
    def maxDistance(self, arrays):
        """
        :type arrays: List[List[int]]
        :rtype: int
        """
        global_min = arrays[0][0]
        global_max = arrays[0][-1]
        max_distance = 0

        for i in range(1, len(arrays)):
            curr_min = arrays[i][0]
            curr_max = arrays[i][-1]

            max_distance = max(max_distance, abs(curr_max - global_min))
            max_distance = max(max_distance, abs(global_max - curr_min))

            global_min = min(global_min, curr_min)
            global_max = max(global_max, curr_max)

        return max_distance