class Solution:
    def calculate(self, num1, num2, symbol):
        if(symbol == '+'):
            return num1 + num2
        
        if(symbol == "-"):
            return num1 - num2
        
        if(symbol == "*"):
            return num1 * num2
    
        if(symbol == "/"):
            return int(num1 / num2)
    
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        symbols = {"+", "-", "*", "/"}
        
        for value in tokens:
            if(value in symbols):
                # print(value, stack)
                num2 = stack.pop()
                num1 = stack.pop()
            
                stack.append(self.calculate(num1, num2, value))
            else:
                stack.append(eval(value))
        
        return stack[-1]