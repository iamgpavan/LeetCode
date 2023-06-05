class Solution:
    
    def rowGenerator(self, row):
        pascalRow = [0]*row
        pascalRow[0] = 1
        pascalRow[row-1] = 1
        value = 1
        
        for col in range(1,row-1):
            value = (value)*(row-col)
            value //= col
            
            pascalRow[col] = value
        
        return pascalRow
    
    def generate(self, numRows: int) -> List[List[int]]:
        ans = []
        
        for i in range(numRows):
            ans.append(self.rowGenerator(i+1))
        
        return ans
        