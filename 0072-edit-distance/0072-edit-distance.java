class Solution {

    public int countOp(String word1, String word2, int i, int j, int[][] dp){
        if(i==-1){
            // if word1 is empty then insert all left letters from word2 
            // where each letter costs 1 (ins) operation
            return j+1;
        }
        else if(j==-1){
            // if word2 is empty then delete all left letters from word1
            // where it costs 1 op for each letter/ character
            return i+1;
        }
        else{
            if(dp[i][j]!=0) return dp[i][j];
            else if((word1.charAt(i))==(word2.charAt(j))){
                // character matches then just decrement indices of both strings
                dp[i][j] = countOp(word1, word2, i-1, j-1, dp);
            }
            else {
                // its dp question so, explore all possibilities and take minimum
                // of it
                dp[i][j] = Math.min((1+countOp(word1, word2, i-1, j, dp)),Math.min((1+countOp(word1, word2, i-1, j-1, dp)),(1+countOp(word1, word2, i, j-1, dp))));
            } 
        }
        return dp[i][j];
    }

    public int minDistance(String word1, String word2) {
        int[][] dp = new int[word1.length()][word2.length()];
        return countOp(word1, word2, word1.length()-1, word2.length()-1, dp);
    }
}