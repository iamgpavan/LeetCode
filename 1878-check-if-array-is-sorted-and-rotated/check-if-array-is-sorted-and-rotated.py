class Solution:
    def check(self, nums: List[int]) -> bool:
        dec = False
        val = nums[0]

        i = 1
        while(i < len(nums)):
            if(nums[i-1] > nums[i]):
                if(dec):
                    return False
                dec = True
            
            if(dec and val < nums[i]):
                return False
            
            i += 1


        return True