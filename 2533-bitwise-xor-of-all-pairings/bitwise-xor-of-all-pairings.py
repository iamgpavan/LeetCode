class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        n1 = len(nums1)
        n2 = len(nums2)
        if(n1%2==0) and (n2%2==0):
            return 0
        
        ans = 0
        if(n1&1 and n2&1):
            for i in nums1:
                ans ^= i
            for i in nums2:
                ans ^= i
        elif(n1&1):
            for i in nums2:
                ans ^= i
        else:
            for i in nums1:
                ans ^= i
        
        return ans

        