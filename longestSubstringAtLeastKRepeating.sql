from collections import defaultdict, Counter
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        
        # - Aakash's Approach - Code Timeout
        # left, right = 0, len(s)
        # max_str = 0

        # # If Entire String has more than K repetitions
        # if min(Counter(s[left:right]).values()) >= k:
        #     return len(s)
        
        # # if len(s) itself it only equal to k then return False
        # if len(s) <= k:
        #     return 0

        # # Look pointers from left and right 
        # while right >= 0 and right > left:
        #     print('string',s[left:right])
        #     temp_map = Counter(s[left:right])

        #     if min(temp_map.values()) >= k:
        #         max_str = max(max_str, right - left +1)
        #     right -= 1
        #     print(left, right)
        #     if right == left:
        #         right = len(s)
        #         left += 1

        #     print(temp_map, max_str)
            
        # return 0 if max_str == 0 else max_str - 1 

        # - Recursive Solution
        if len(s) == 0 or k > len(s):
            return 0
        c = Counter(s)
        sub1, sub2 = "", ""
        for i, letter in enumerate(s):
            if c[letter] < k:
                sub1 = self.longestSubstring(s[:i], k)
                sub2 = self.longestSubstring(s[i+1:], k)
                break
        else:
            return len(s)
        return max(sub1, sub2)
