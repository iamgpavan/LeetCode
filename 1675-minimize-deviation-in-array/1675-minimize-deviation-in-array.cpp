class Solution {
public:
    int minimumDeviation(vector<int>& nums) {
        priority_queue<int> pq;
        int mn = INT_MAX;
        for (int x : nums) {
            if (x % 2 == 1) x *= 2; // multiply odd numbers by 2
            pq.push(x);
            mn = min(mn, x);
        }
        int ans = INT_MAX;
        while (true) {
            int x = pq.top(); pq.pop();
            ans = min(ans, x - mn); // update answer
            if (x % 2 == 0) {
                x /= 2; // divide even numbers by 2
                mn = min(mn, x); // update minimum value
                pq.push(x);
            } else {
                break; // stop when we reach an odd number
            }
        }
        return ans;
    }
};