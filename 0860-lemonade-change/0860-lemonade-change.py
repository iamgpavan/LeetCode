class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        
        five_doller = 0
        ten_doller = 0
        twenty_doller = 0
        
        for money in bills:
            if(money == 5):
                five_doller += 1
            elif(money == 10):
                five_doller -= 1
                ten_doller += 1
                if(five_doller == -1):
                    return False
            else:
                twenty_doller += 1
                if(five_doller > 0 and ten_doller > 0):
                    five_doller -= 1
                    ten_doller -= 1
                elif(five_doller > 2):
                    five_doller -= 3
                else:
                    return False
        return True
        