class Solution {
public:
    vector<vector<int>> generateMatrix(int n) {
        vector<vector<int>> mat(n, vector<int> (n,0)); // filled with zeros
        // 1 - right    2 - down    3 - left    4 - up
        int value = 1;
        int i = 0;
        int j = 0;
        int dir = 1;
        
        while(value <= n*n){
            mat[i][j] = value;
            value += 1;
            
            if(dir == 1){
                j += 1;
                // check for edge case that is right corner
                // 1 -> 2
                if(j==n || mat[i][j] != 0){ // || mat[i][j] != 0 is to avoid refilling
                    j -= 1;
                    dir = 2;
                    i += 1;
                }
            }else if(dir == 2){
                i += 1;
                // check for edge case that is dowm corner
                // 2 -> 3
                if(i == n || mat[i][j] != 0){
                    i -= 1;
                    dir = 3;
                    j -= 1;
                }
            }else if(dir == 3){
                j -= 1;
                // check for edge case that is left corner
                // 3 -> 4
                if(j < 0 || mat[i][j] != 0){
                    j += 1;
                    dir = 4;
                    i -= 1;
                }
            }else if(dir == 4){
                i -= 1;
                // check for edge case that is upper corner
                // 4 -> 1
                if(i < 1 || mat[i][j] != 0){
                    i += 1;
                    dir = 1;
                    j += 1;
                }
            }
        }
        
        return mat;        
    }
};