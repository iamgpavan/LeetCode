class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hs = set(nums)

        ans = 0

        for i in nums:
            if i in hs:
                length = 1
                hs.remove(i)
                # towards right
                right = i+1
                while(right in hs):
                    length += 1
                    hs.remove(right)
                    right += 1

                # towards left
                left  = i-1
                while(left in hs):
                    length += 1
                    hs.remove(left)
                    left -= 1
                
                ans = max(ans, length)

        return ans