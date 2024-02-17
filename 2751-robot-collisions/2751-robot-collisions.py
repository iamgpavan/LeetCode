class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        data = []
        
        for i in range(len(positions)):
            data.append([positions[i], healths[i], directions[i]])
        
        ans = {}
        stack = []
        
        data.sort()
        
        i = 0
        
        while(i < len(data)):
            direction = data[i][2]
            # print("start,",data[i], stack)
            
            if(direction == 'R'):
                stack.append(data[i])
            else:
                if(len(stack)):
                    
                    if(data[i][1] < stack[-1][1]):
                        collide = stack.pop()
                        stack.append([collide[0], collide[1]-1, 'R'])
                    elif(data[i][1] > stack[-1][1]):
                        while(len(stack) and data[i][1] > stack[-1][1]):
                            stack.pop()
                            data[i][1] -= 1
                            
                        
                        if(len(stack) == 0):
                            ans[data[i][0]] = data[i][1]
                        elif(data[i][1] == stack[-1][1]):
                            stack.pop()
                        else:
                            stack[-1][1] -= 1
                    else:
                        stack.pop()
                else:
                    ans[data[i][0]] = data[i][1]
            # print("end,",data[i], stack)
            i += 1
            
            
        while(stack):
            val = stack.pop()
            ans[val[0]] = val[1]
        
        
        result = []
        # print(ans)
        
        for i in positions:
            health = ans.get(i, None)
            if(health != None):
                result.append(health)
        
        return result