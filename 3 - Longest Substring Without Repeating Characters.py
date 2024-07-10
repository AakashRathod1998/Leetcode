class Solution(object):
    def lengthOfLongestSubstring(self, s):

        seen = {}
        maxLen = 0
        start = 0

        for i, val in enumerate(s):

            if val in seen and start <= seen[val]:
                start = seen[val] + 1
            
            seen[val] = i

            maxLen = max(maxLen, i-start+1)
        
        return maxLen
        
# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
        
#         left = 0
#         right = left+1
#         temp = ''
#         res,ctr = 0,0
#         if len(s) == 0 or len(s) == 1:
#             return len(s)
#         while right < len(s):
            
#             if temp == '':
#                 temp+=s[left]
#                 ctr = len(temp)
#             if s[right] not in temp:
#                 temp+=s[right]
#                 right+=1
#                 ctr = len(temp)
#             else:
#                 ctr = len(temp)
#                 temp=''
#                 left = left+1
#                 right = left+1
            
#             res = max(res,ctr)
        
#         return res
