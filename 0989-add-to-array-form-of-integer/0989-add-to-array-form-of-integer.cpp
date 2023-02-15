class Solution {
public:
    vector<int> addToArrayForm(vector<int>& num, int k) {
        vector<int> result;
        vector<int> num1;
        string s="";
        int ans=0;
        while(k>9)
        {
            num1.push_back(k%10);
            k/=10;
        }
        if(k!=0)
        {
            num1.push_back(k);
        }
        reverse(num.begin(),num.end());
        int i=0;int j=0;int carry=0;
        while(i<num.size() && j<num1.size())
        {   
            int x=num[i];int y=num1[j];
            if(carry)
            {   
                if((x+y+1)<10){carry=0;}
                result.push_back((x+y+1)%10);
            }
            else{
                if(x+y>=10){carry=1;}
                result.push_back((x+y)%10);
            }
            i++;j++;
        }

        while(i<num.size())
        {
            if(carry)
            {
                if(num[i]+1<10)
                {
                    carry=0;
                }

                result.push_back((num[i]+1)%10);
            }

            else{
                result.push_back(num[i]);
            }
            i++;
        }

        while(j<num1.size())
        {
            if(carry)
            {
                if(num1[j]+1<10)
                {
                    carry=0;
                }

                result.push_back((num1[j]+1)%10);
            }

            else{
                result.push_back(num1[j]);
            }
            j++;
        }

        if(carry)
        {
            result.push_back(1);
        }
        for(auto x:result)
        {
            cout<<x<<":";
        }
        reverse(result.begin(),result.end());
        return result;
    }
};