class Solution {
private:
    bool check(vector<int> weights, int days, int w){
        int daysCount = 1;
        int i=0;
        int weightSoFar = 0;
        
        while(i<weights.size()){
            weightSoFar += weights[i];
            if(weightSoFar > w){
                //cout << daysCount <<  " " << weightSoFar <<  " " << i << " " << w <<  "\n"; 
                daysCount += 1;
                weightSoFar = 0;
                if(weights[i] < w)  i-=1;
            }
            i += 1;
        }
        //cout << "**********" << "\n"; 
        if(daysCount > days)    return false;
        return true;
    }
public:
    int shipWithinDays(vector<int>& weights, int days) {
        int minWeight = 0;
        int maxWeight = 0;
        
        for(int i=0; i<weights.size(); i++){
            minWeight = max(minWeight, weights[i]);
            maxWeight += weights[i];
        }
        //check(weights, days, 6);
        while(minWeight <= maxWeight){
            int midWeight = (minWeight + maxWeight)/2;
            //cout << minWeight << " " << maxWeight << " " << midWeight << "\n";
            if(check(weights, days, midWeight)){
                maxWeight = midWeight-1;
            }else{
                minWeight = midWeight+1;
            }
        }
        
        
        return minWeight;
    }
};