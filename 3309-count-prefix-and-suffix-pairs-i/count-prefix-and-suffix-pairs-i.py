class Solution:
    def isPrefixSufix(self, str1, str2):
        return len(str2) >= len(str1) and (str2[:len(str1)] == str1 and str2[-1-len(str1)+1:]==str1)
        
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        
        ans = 0
        
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                # str1 = words[i]
                # str2 = words[j]
                # print(str2[-1-len(str1)+1:], str1)
                if(self.isPrefixSufix(words[i], words[j])):
                    ans += 1
        
        return ans