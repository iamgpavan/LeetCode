//{ Driver Code Starts
#include <bits/stdc++.h>

using namespace std;

// } Driver Code Ends
class Solution{
public:
    vector<int> findRange(string str, int n) {
        // code here
        int arr[n] ;
        
        for(int i=0; i<n; i++){
            if(str[i] == '1'){
                arr[i] = -1;
            }else{
                arr[i] = 1;
            }
        }
        
        int L = -1, R = -1, dL = 0;
        int preSum = 0, maxSum = 0;
        
        for(int i=0; i<n; i++){
            preSum += arr[i];
            
            if(preSum > maxSum){
                maxSum = preSum;
                R = i;
                L = dL;
            }
            
            if(preSum < 0){
                
                preSum = 0;
                dL = i+1;
            }
        }
        
        if(R==-1) return {-1};
        
        return {L+1, R+1};
    }
};

//{ Driver Code Starts.

int main() {
    int t;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;
        string s;
        cin >> s;
        Solution ob;
        auto ans = ob.findRange(s, n);

        if (ans.size() == 1) {
            cout << ans[0] << "\n";
        } else {
            cout << ans[0] << " " << ans[1] << "\n";
        }
    }
    return 0;
}
// } Driver Code Ends