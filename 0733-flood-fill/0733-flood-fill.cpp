class Solution {
private:
    void dfs(int sr, int sc, int m, int n, int baseColor, int color, vector<vector<int>> &image, int dx[], int dy[]){
        image[sr][sc] = color;
        
        
        for(int i=0; i<4; i++){
            int nrow = sr + dx[i];
            int ncol = sc + dy[i];
            
            if(nrow>=0 && nrow<m && ncol>=0 && ncol<n && image[nrow][ncol] == baseColor && image[nrow][ncol] != color){
                dfs(nrow, ncol, m, n, baseColor, color, image, dx, dy);
            }
        }
    }
public:
    vector<vector<int>> floodFill(vector<vector<int>>& image, int sr, int sc, int color) {
        int dx[] = {-1,0,1,0};
        int dy[] = {0,1,0,-1};
     
        dfs(sr, sc, image.size(), image[0].size(), image[sr][sc], color, image, dx, dy);
        
        return image;
    }
};