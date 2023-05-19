class Solution {
    public boolean isBipartite(int[][] graph) {
        int n = graph.length;
        int[] color = new int[n];
        Arrays.fill(color, -1);
        int comps = 0;
        for (int u = 0; u < n; u++) {
            if (color[u] == -1) {
                comps++;
                if (!dfs(graph, u, 0, color)) return false;
            }
        }
        return true;
    }

    boolean dfs(int[][] graph, int u, int col, int[] color) {
        if (color[u] != -1) return color[u] == col;
        color[u] = col;
        for (int v : graph[u]) {
            if (!dfs(graph, v, col ^ 1, color)) return false;
        }
        return true;
    }
}