class Solution:
    def maximumLength(self, s: str) -> int:
        groups = defaultdict(list)
        
        i = 1
        prev = s[0]
        currCount = 1
        
        while i <= len(s):
            if i == len(s):
                groups[prev].append(currCount)
                groups[prev] = sorted(groups[prev], reverse=True)[:3]
            elif s[i] != prev:
                groups[prev].append(currCount)
                groups[prev] = sorted(groups[prev], reverse=True)[:3]
                prev = s[i]
                currCount = 1
            else:
                currCount += 1
            
            i += 1
        
        res = -1

        for key, values in groups.items():
            no_of_groups = len(values)
            ans = values[0] - 2
            
            if no_of_groups == 2:
                x, y = values
                if y >= x - 1:
                    ans = max(ans, x - 1)
            elif no_of_groups == 3:
                x, y, z = values
                if x == y == z:
                    ans = max(ans, x)
                elif y >= x - 1:
                    ans = max(ans, x - 1)
            
            if ans > 0:
                res = max(ans, res)
        
        return res
