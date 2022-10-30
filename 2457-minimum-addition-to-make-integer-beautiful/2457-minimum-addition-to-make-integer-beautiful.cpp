class Solution {
public:
    int digit_sum(long long num){
        int sum = 0;
        
        while(num){
            sum += num%10;
            num /= 10;
        }
        
        return sum;
    }
    long long makeIntegerBeautiful(long long n, int target) {
        long long ans = 0;
        int n_sum = digit_sum(n);
        int position = 0;
        
        while(n_sum > target){
            if(n%10 == 0){
                position += 1;
                n /=10;
            }else{
                int toAdd = 10-n%10;
                n += toAdd;
                n_sum = digit_sum(n);
                ans += pow(10,position)*toAdd;
            }
        }
        
        return ans;
    }
};