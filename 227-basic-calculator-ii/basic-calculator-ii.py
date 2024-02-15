class Solution:  
    def evaluate(self, num1, num2, symbol):
        if(symbol == '+'):
            return num1 + num2
        
        if(symbol == "-"):
            return num1 - num2
        
        if(symbol == "*"):
            return num1 * num2
    
        if(symbol == "/"):
            return int(num1 / num2)
    
    def infix_to_postfix(self, infix):
        stack = []
        postfix = ""
        precidency = {'*':2, '/':2, '+':1, '-':1}
        
        i = 0
        while(i < len(infix)):
            # Operand 
            while(i < len(infix) and infix[i].isdigit()):
                postfix += infix[i]
                i += 1
            else:
                postfix += " "
            
            if(i < len(infix)):
                # Operator 
                # + 
                if(infix[i] == ')'):
                    while(stack[-1] != '('):
                        postfix += stack.pop()
                        postfix += " "
                    stack.pop()
                elif(infix[i] == '('):
                    stack.append(infix[i])
                elif(infix[i] != " "):
                    while(len(stack) and precidency[stack[-1]] >= precidency[infix[i]]):
                        postfix += stack.pop()
                        postfix += " "
                    
                    stack.append(infix[i])
            i += 1
        
        while(len(stack)):
            postfix += stack.pop()
            postfix += " "
        
        
        return postfix
        
        
    
    def calculate(self, s: str) -> int:
        
        postfix = self.infix_to_postfix(s)
        # print(postfix.split(" "))
        stack = []
        symbols = {"+", "-", "*", "/"}
        
        for value in postfix.split(" "):
            
            if(value in symbols):
                # print(value, stack)
                num2 = stack.pop()
                num1 = stack.pop()
                # print(num1, num2,self.evaluate(num1, num2, value) )
            
                stack.append(self.evaluate(num1, num2, value))
            elif(value.strip() != ""):
                # print("Value", value)
                stack.append(eval(value))
        
        return stack[-1]