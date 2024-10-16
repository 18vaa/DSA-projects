class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        n = x
        revNum = 0
        if n<0: return False

        while(n>0):
            d = n % 10
            revNum = revNum * 10 + d
            n /= 10
        if revNum == x: return True
