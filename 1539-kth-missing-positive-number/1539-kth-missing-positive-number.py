class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        correct = list(range(1, max(arr) + 10000))

        missing = list(set(correct).symmetric_difference(set(arr)))

        return missing[k - 1]