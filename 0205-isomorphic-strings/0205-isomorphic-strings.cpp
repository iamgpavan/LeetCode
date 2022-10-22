class Solution {
public:
    bool isIsomorphic(string s, string t) {
        if(s.length() != t.length())    return false;
        unordered_map<int, int> s_mp;
        unordered_map<int, int> t_mp;
        
        int i=0;
        int j=0;
        while(i<s.length()){
            if(s_mp.find(s[i]) != s_mp.end()){
                if(s_mp[s[i]] != t[j])    return false;
            }
            if(t_mp.find(t[j]) != t_mp.end()){
                if(t_mp[t[j]] != s[i])    return false;
            }
            s_mp[s[i]] = t[j];
            t_mp[t[j]] = s[i];
            i+=1;
            j+=1;
        }
        
        return true;        
    }
};