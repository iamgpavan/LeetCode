class Solution:
    def mostPopularCreator(self, creators: List[str], ids: List[str], views: List[int]) -> List[List[str]]:
        d = dict()
        
        for i in range(len(creators)):
            if creators[i] not in d:
                d[creators[i]] = [ids[i], views[i], views[i]]
            else:
                if(d[creators[i]][2] < views[i]):
                    d[creators[i]][0] = ids[i]
                    d[creators[i]][2] = views[i]
                elif(d[creators[i]][2] == views[i] and d[creators[i]][0] > ids[i]):
                    d[creators[i]][0] = ids[i]
                d[creators[i]][1] += views[i]
                
        lis = sorted(list(d.items()), reverse = True, key = lambda x:[x[1][1],x[0],x[1][0]])
        ans = []
        
        maxi = lis[0][1][1]
        
        for i in lis:
            if(i[1][1] == maxi):
                ans.append([i[0],i[1][0]])
        
        return ans