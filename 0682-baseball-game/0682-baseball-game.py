class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        ans = 0
        
        for i in operations:
            if i == 'C':
                ans -= stack.pop()
            elif i == 'D':
                num = stack.pop()
                ans += (2*num)
                stack.append(num)
                stack.append(2*num)
            elif i == '+':
                num2 = stack.pop()
                num1 = stack.pop()
                
                ans += (num1+num2)
                stack.append(num1)
                stack.append(num2)
                stack.append(num1+num2)
            else:
                ans += int(i)
                stack.append(int(i))
            
        return ans