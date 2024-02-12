class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        ans = ""
        
        for directory in path.split("/"):
            # print(directory)
            if(directory == ".."):
                if(len(stack)):
                    stack.pop()
            elif(directory == "." or directory == '/' or directory == ""):
                continue
            else:
                stack.append(directory)
        
        # print(stack)
        while(len(stack)):
            directory = stack.pop()
            # print("dir and ans", directory, ans)
            ans = "/" + directory + ans
            
        if(len(ans) == 0):
            return "/"
        
        return ans