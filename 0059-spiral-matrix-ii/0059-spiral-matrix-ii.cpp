class Solution {
public:
    vector<vector<int>> generateMatrix(int n) {
        vector<vector<int>> mat(n, vector<int> (n,0));
        
        int k = 1;
        int dir = 0;
        // 0 - R 
        // 1 - D
        // 2 - L
        // 3 - U
        
        int i = 0;
        int j = 0;
        
        while(k <= n*n){
            mat[i][j] = k;
            k += 1;
            
            if(dir == 0){
                j += 1; 
                if(j == n || mat[i][j] != 0){ 
                    j -= 1;
                    dir = 1;
                    i += 1;                    
                }
            }else if(dir == 1){
                i += 1;
                if(i == n || mat[i][j] != 0){
                    i -= 1;
                    dir = 2;
                    j -= 1;
                }
            }else if(dir == 2){
                j -= 1;
                if(j == -1 || mat[i][j] != 0){
                    j += 1;
                    dir = 3;
                    i -= 1;
                }
            }else if(dir == 3){
                i -= 1;
                if(i == -1 || mat[i][j] != 0){
                    i += 1;
                    dir = 0;
                    j += 1;
                }
            }
        }
        
        return mat;
    }
};