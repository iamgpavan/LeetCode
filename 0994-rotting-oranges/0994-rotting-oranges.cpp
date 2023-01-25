class Solution {
private:
    int bfs(int m, int n, vector<vector<int>> grid, vector<vector<int>> &vis, int &rottened, int dx[], int dy[], queue<pair<int, pair<int, int>>> q){
        
        int mini = 0;
        while(!q.empty()){
            int row = q.front().first;
            int col = q.front().second.first;
            mini =  q.front().second.second;
            q.pop();
            vis[row][col] = 1;
            
            for(int i=0; i<4; i++){
                int nrow = row + dx[i];
                int ncol = col + dy[i];
                
                if(nrow>=0 && nrow<m && ncol>=0 && ncol<n && !vis[nrow][ncol] && grid[nrow][ncol] == 1){
                    //cout<< nrow << " " << ncol << " " << mini+1 << "\n";
                    rottened += 1;
                    q.push({nrow,{ncol,mini+1}});
                    vis[nrow][ncol] = 1;
                }
            }
        }
        
        return mini;
    }
    
public:
    int orangesRotting(vector<vector<int>>& grid) {
        int dx[] = {-1,0,1,0};
        int dy[] = {0,1,0,-1};
        int m = grid.size();
        int n = grid[0].size();
        
        vector<vector<int>> vis(m, vector<int> (n, 0));
        int fresh_count = 0;
        int rottened = 0;
        int mini = 0;
        queue<pair<int, pair<int, int>>> q; 
        
        for(int i=0; i<m; i++){
            for(int j=0; j<n; j++){
                if(grid[i][j] == 1) fresh_count += 1;
                if(grid[i][j] == 2){
                    q.push({i, {j, 0}});
                }
            }
        }  
        
        mini = bfs(m, n, grid, vis, rottened, dx, dy, q);
        
        if(rottened != fresh_count) return -1;
        
        return mini;
    }
};