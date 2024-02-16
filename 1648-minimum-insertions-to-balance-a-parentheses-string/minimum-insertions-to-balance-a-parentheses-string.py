class Solution:
    def minInsertions(self, s: str) -> int:
        open_count = 0
        close_count = 0
        ans = 0
        
        i = 0
        
        while(i < len(s)):
            if(s[i] == '('):
                
                if(open_count>0 and close_count != 0):
                    # print(i, open_count, close_count)
                    ans += (close_count % 2)
                    close_count = 0
                    open_count -= 1
                
                open_count += 1 
            else:
                close_count += 1
                if(open_count == 0):
                    i += 1
                    while(i < len(s) and s[i] != '('):
                        close_count += 1
                        i += 1
                    # print(i, close_count, (ceil(close_count/2)), (close_count%2))
                    ans += ((ceil(close_count/2))+(close_count%2))
                    close_count = 0
                    i -= 1
                elif(close_count == 2):
                    close_count = 0
                    open_count -= 1             
            i += 1
            
        
        if(open_count):
            ans += (2*open_count - close_count)
        elif(close_count==1):
            ans += 1
        
        return ans