class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        left = 0
        right = left+1
        temp = ''
        res,ctr = 0,0
        if len(s) == 0 or len(s) == 1:
            return len(s)
        while right < len(s):
            
            if temp == '':
                temp+=s[left]
                ctr = len(temp)
            if s[right] not in temp:
                temp+=s[right]
                right+=1
                ctr = len(temp)
            else:
                ctr = len(temp)
                temp=''
                left = left+1
                right = left+1
            
            res = max(res,ctr)
        
        return res

        
#         start = maxLength = 0
#         usedChar = {}
        
#         for i in range(len(s)):
#             if s[i] in usedChar and start <= usedChar[s[i]]:
#                 start = usedChar[s[i]] + 1
#             else:
#                 maxLength = max(maxLength, i - start + 1)

#             usedChar[s[i]] = i
#             print(usedChar)

#         return maxLength
