class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        seen = set()

        for freq in collections.Counter(arr).values():

            if freq in seen:

                return False

            seen.add(freq)

        return True