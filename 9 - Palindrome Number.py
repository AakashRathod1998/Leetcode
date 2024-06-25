class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        # return str(x) == str(x)[::-1]

        if x < 0:
            return False

        x1 = x
        rev = 0

        while x1 > 0:
            rev = (rev * 10) + x1%10
            x1 //= 10
        
        return x == rev
