class Solution {
public:
    bool isPalindrome(int x) {
        long long revNum = 0; // have to use long long because one of the test cases is too big for int
        long long n = x;
        if(n<0) return false;

        while(n>0){
            int d = n%10;
            revNum = revNum*10 + d;
            n = n/10;
        }

        if(revNum == x) return true;
        else return false;
    }
};
