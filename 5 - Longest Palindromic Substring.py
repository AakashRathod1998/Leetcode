class Solution(object):
    def longestPalindrome(self, s):

        if len(s) <= 1:
            return s
        start = 0
        
        def _in_out_(s, left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left  -= 1
                right += 1
            # return s[left:right+1]
            return right-left-1

        maxStr = i = 0

        while i < len(s):

            odd  = _in_out_(s, i, i)
            even = _in_out_(s, i, i+1)
            length = max(odd, even)

            if length > maxStr:
                maxStr = length
                start = i - (length-1) // 2

            i += 1
        
        return s[start:start + maxStr]



    #     if len(s) <= 1:
    #         return s

    #     start = 0
    #     max_length = 0

    #     for i in range(len(s)):
    #         # For odd-length palindrome
    #         len1 = self.expand_around_center(s, i, i)
    #         # For even-length palindrome
    #         len2 = self.expand_around_center(s, i, i + 1)
            
    #         # Find the maximum length palindrome centered at position i
    #         length = max(len1, len2)
            
    #         # If the palindrome centered at position i is longer than the current longest palindrome
    #         if length > max_length:
    #             max_length = length
    #             start = i - (length - 1) // 2

    #     return s[start:start + max_length]

    # def expand_around_center(self, s, left, right):
    #     # Expand outward from the center
    #     while left >= 0 and right < len(s) and s[left] == s[right]:
    #         left -= 1
    #         right += 1
    #     # Return the length of the palindrome found
    #     return right - left - 1
