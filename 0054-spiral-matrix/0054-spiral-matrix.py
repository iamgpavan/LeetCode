class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        row = len(matrix)
        col = len(matrix[0])
        top = 0
        bottom = row-1
        left = 0
        right = col - 1
        lis = []
        # Defining the direction in which the array is to be traversed.
        dir = 0
    
        while (top <= bottom and left <=right):    
            if dir ==0:
                for i in range(left,right+1): # moving left->right
                    lis.append(matrix[top][i])

                # Since we have traversed the whole first
                # row, move down to the next row.
                top +=1
                dir = 1

            elif dir ==1:
                for i in range(top,bottom+1): # moving top->bottom
                    lis.append(matrix[i][right])

                # Since we have traversed the whole last
                # column, move down to the previous column.
                right -=1 
                dir = 2
            
            elif dir ==2:
                for i in range(right,left-1,-1): # moving right->left
                    lis.append(matrix[bottom][i])

                # Since we have traversed the whole last
                # row, move down to the previous row.
                bottom -=1
                dir = 3
            
            elif dir ==3:
                for i in range(bottom,top-1,-1): # moving bottom->top
                    lis.append(matrix[i][left])
                # Since we have traversed the whole first
                # column, move down to the next column.
                left +=1
                dir = 0
        return lis