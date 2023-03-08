class Solution {
public:
     int check(int mid,vector<int>& piles){
        
        long long h=0;
        for(int i=0;i<piles.size();i++){
            h+= ((long long)(piles[i]+mid-1))/mid;
        }
        return (int)h;
    }
    
    int minEatingSpeed(vector<int>& piles, int h) {
        
        int l=1,r=*max_element(piles.begin(),piles.end());
        
        while(l<r){
            int mid= l+(-l+r)/2;
            if(check(mid,piles)>h){
                l=mid+1;
            }
            else{
                r= mid;
            }
        }
        
        return l;
    }
};