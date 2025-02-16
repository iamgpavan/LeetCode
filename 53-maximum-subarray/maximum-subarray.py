class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        threshold = 0
        curr_sum = threshold

        for i in range(len(nums)):
            curr_sum += nums[i]
            max_sum = max(max_sum, curr_sum)

            if(curr_sum < threshold):
                curr_sum = threshold
        
        return max_sum