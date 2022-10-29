//{ Driver Code Starts
// Initial Template for C++

#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends
// User function Template for C++

class Solution{
public:
void isPrefix(string str,string contact[],int n,set<string>&s){
        for(int i=0;i<n;i++){
             int i1=0;
             int j=0;
             bool flag=true;
             while(i1<str.size() && j<contact[i].size()){
                 if(str[i1]!=contact[i][j]){
                     flag=false;
                     break;
                 }
                 i1++;
                 j++;
             }
             if(i1==str.size()){
                 s.insert(contact[i]);
             }
        }
    }
    vector<vector<string>> displayContacts(int n, string contact[], string s)
    {
        // code here
        string str="";
        vector<vector<string>>ans;
        for(int i=0;i<s.size();i++){
            str+=s[i];
            set<string>s;
           isPrefix(str,contact,n,s);
           vector<string>temp;
           for(string x:s){
               temp.push_back(x);
           }
           if(temp.empty()){
               ans.push_back({"0"});
           }
           else{
           ans.push_back(temp);
           }
        }
        return ans;
    }
};

//{ Driver Code Starts.

int main(){
    int t;
    cin>>t;
    while(t--){
        int n;
        cin>>n;
        string contact[n], s;
        for(int i = 0;i < n;i++)
            cin>>contact[i];
        cin>>s;
        
        Solution ob;
        vector<vector<string>> ans = ob.displayContacts(n, contact, s);
        for(int i = 0;i < s.size();i++){
            for(auto u: ans[i])
                cout<<u<<" ";
            cout<<"\n";
        }
    }
    return 0;
}
// } Driver Code Ends