class RangeFreqQuery:
    def __init__(self, arr: List[int]):
        self.d = {}
        for i in range(len(arr)):
            if arr[i] not in self.d:
                self.d[arr[i]] = [i]
            else:
                self.d[arr[i]].append(i)

    def query(self, left: int, right: int, value: int) -> int:
        indices = self.d.get(value)
        if not indices:
            return 0
        l = bisect_left(indices, left)
        r = bisect_right(indices, right)
        return r - l
        


# Your RangeFreqQuery object will be instantiated and called as such:
# obj = RangeFreqQuery(arr)
# param_1 = obj.query(left,right,value)