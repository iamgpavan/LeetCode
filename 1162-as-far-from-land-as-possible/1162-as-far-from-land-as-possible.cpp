class Solution {
public:
    int maxDistance(vector<vector<int>>& grid) {
        queue<pair<int,int>> q;
        int m = grid.size();
        int n = grid[0].size();
        int res = -1;
        for(int i=0;i<m;i++){
            for(int j=0;j<n;j++){
                if(grid[i][j]==1){
                    q.push({i,j});
                }
            }
        }
        int dx[4][4] = {{0,1},{0,-1},{1,0},{-1,0}};
        while(!q.empty()){
            auto temp = q.front();
            int x = temp.first;
            int y = temp.second;
            res = grid[x][y];
            for(int i=0;i<4;i++){
                int newX = dx[i][0]+x;
                int newY = dx[i][1]+y;
                if(min(newX,newY)>=0 && max(newX,newY)<n && !grid[newX][newY]){
                    q.push({newX,newY});
                    grid[newX][newY]= grid[x][y]+1;
                }
            }
            q.pop();
        }
        return res>1?res-1:-1;
    }
};