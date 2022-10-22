class Solution {
public:
    string minWindow(string s, string t) {
        if(t.length() == 0 || t.length() > s.length())  return "";
       
        unordered_map<int, int> t_map;
        unordered_map<int, int> s_map;
        int had = 0;
        int have = 0;
        
        for(int i=0; i<t.length(); i++){
            t_map[t[i]] += 1;
        }
        had = t_map.size();
        
        int len = s.length()+1;
        int final_start = -1;
        int final_end = -1;
        int start = 0;
        int end = 0;
        
        while(start < s.length()){
            //cout << "1 "<<"start : "<< start << " end : " << end << " had : " << had << " have : " << have << "\n";
            while(have != had && end < s.length()){
                if(t_map.find(s[end]) != t_map.end()){
                    s_map[s[end]] += 1;
                    if(s_map[s[end]] == t_map[s[end]]){
                        have += 1;
                    }
                }
                end += 1;
            }
            //cout << "2 " <<"start : "<< start << " end : " << end << " had : " << had << " have : " << have << "\n";
           
            if(had == have && end-start < len){
                len = end-start;
                final_start = start;
                final_end = end-1;
                //cout<<"final start: " << final_start << " final end: " << final_end << " len " << len << "\n";
            }
            
            if(t_map.find(s[start]) != t_map.end()){
                s_map[s[start]] -= 1;
                if(s_map[s[start]] < t_map[s[start]]){
                    have -= 1;
                }
            }
            
            start += 1;
        }
        
        if(final_start == -1 && final_end == -1)    return "";
       
        string ans = "";
        
        for(int i=final_start; i<=final_end; i++){
            ans += s[i];
        }
        
        return ans;
    }
};