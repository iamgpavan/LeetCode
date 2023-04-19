class Solution {
    public int racecar(int target) {
        int[] dp = new int[target + 1];
        Arrays.fill(dp, Integer.MAX_VALUE);
        dp[0] = 0;
        dp[1] = 1;
        
        for (int i = 2; i <= target; i++) {
            int k = 32 - Integer.numberOfLeadingZeros(i);
            if (i == (1 << k) - 1) {
                dp[i] = k;
                continue;
            }
            for (int j = 0; j < k - 1; j++) {
                dp[i] = Math.min(dp[i], dp[i - (1 << (k - 1)) + (1 << j)] + k - 1 + j + 2);
            }
            if ((1 << k) - 1 - i < i) {
                dp[i] = Math.min(dp[i], dp[(1 << k) - 1 - i] + k + 1);
            }
        }
        return dp[target];
    }
}
