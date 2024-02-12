class Solution:
    def countCollisions(self, directions: str) -> int:
        stack = []
        ans = 0
        
        i = 0
        
        while(i  < len(directions)):
            if(directions[i] == 'L'):
                # print(stack, directions[i], i)
                if(len(stack) and stack[-1] == 'R'):
                    stack.pop()
                    stack.append('S')
                    ans += 2
                    
                elif(len(stack) and stack[-1] == 'S'):
                    ans += 1
            else:
                stack.append(directions[i])
            
            i += 1
        
        while(len(stack)):
            direction = stack.pop()
            if(direction == 'S'):
                break
        
        while(len(stack)):
            direction = stack.pop()
            if(direction == 'R'):
                ans += 1
        
        return ans