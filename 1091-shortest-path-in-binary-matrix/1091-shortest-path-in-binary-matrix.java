class Solution {
    public int shortestPathBinaryMatrix(int[][] grid) {
        int n = grid.length;
        if(grid[0][0]==1)
            return -1;

        Queue<int[]> queue = new LinkedList<>();
        boolean[][] visited = new boolean[n][n];
        queue.add(new int[]{0,0,1});
        int res = Integer.MAX_VALUE;
        while(!queue.isEmpty())
        {
            int size = queue.size();
            int count = Integer.MAX_VALUE;
            for(int i=0;i<size;i++)
            {
                int[] adjArr = queue.poll();
                int x = adjArr[0];
                int y = adjArr[1];
                if(x<0||y<0||x>=n||y>=n||visited[x][y]||grid[x][y]==1)
                {
                    continue;
                }
                if(x==n-1&&y==n-1)
                {
                    return adjArr[2];
                }
                visited[x][y] = true;
                queue.add(new int[]{x-1,y-1,adjArr[2]+1});
                queue.add(new int[]{x,y-1,adjArr[2]+1});
                queue.add(new int[]{x+1,y-1,adjArr[2]+1});
                queue.add(new int[]{x-1,y,adjArr[2]+1});
                queue.add(new int[]{x+1,y,adjArr[2]+1});
                queue.add(new int[]{x-1,y+1,adjArr[2]+1});
                queue.add(new int[]{x,y+1,adjArr[2]+1});
                queue.add(new int[]{x+1,y+1,adjArr[2]+1});
            }
        }
        return -1;
    }
}