class Solution:
    def isPathCrossing(self, path: str) -> bool:
        visited = {(0,0):True}
        curr_x = 0
        curr_y = 0
        
        for i in path:
            if(i == 'N'):
                curr_y += 1
            elif(i == 'E'):
                curr_x += 1
            elif(i == 'S'):
                curr_y -= 1
            elif(i == 'W'):
                curr_x -= 1
            
            new_coordinates = (curr_x, curr_y)
            # print(visited)
            
            if new_coordinates in visited:
                return True
            visited[new_coordinates] = True
        
        return False