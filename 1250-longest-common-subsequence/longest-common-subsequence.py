class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memory = [[-1 for j in range(len(text2))] for i in range(len(text1))]
        def lcs(i,j, s1, s2, memory):
            if(i >= len(s1) or j >= len(s2)):
                return 0
            
            if(memory[i][j] != -1):
                return memory[i][j]
            
            if(s1[i] == s2[j]):
                memory[i][j] = 1 + lcs(i+1, j+1, s1, s2, memory)
                return memory[i][j] 
            
            memory[i][j] = max(lcs(i, j+1, s1, s2, memory), lcs(i+1, j, s1, s2, memory))
            return memory[i][j]
        
        return lcs(0, 0, text1, text2, memory)