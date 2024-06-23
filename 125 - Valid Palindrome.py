class Solution:
    def isPalindrome(self, s: str) -> bool:

        str1 = ''.join([char.lower() for char in s if char.isalnum()])
        return str1 == str1[::-1]

        # string = ''

        # for i in s:
        #     if i.isalnum():
        #         string+=i
        # l,r = 0,len(string)-1
        # string = string.lower()
        # while l <r:
        #     if string[l] != string[r]:
        #         return False
        #     l+=1
        #     r-=1
        # return True
