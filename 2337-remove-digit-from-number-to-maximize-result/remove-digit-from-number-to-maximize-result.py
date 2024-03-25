class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        
        
        ind = 0
        last_occur = -1
        
        while(ind < len(number)):
            if(number[ind] == digit):
                
                if(ind+1 == len(number) or (number[ind] < number[ind+1])):
                    last_occur = ind
                    break
                                    
                last_occur = ind
            ind += 1
        
        
        return number[:last_occur] + number[last_occur+1:]