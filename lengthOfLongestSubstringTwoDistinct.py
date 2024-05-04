from collections import defaultdict
class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:

        k = 2
        if len(s) <= k:
            return len(s)
        
        hashmap = defaultdict()
        left, right = 0, 0
        max_str = 0

        while right < len(s):

            hashmap[s[right]] = right

            if len(hashmap) > k:
                rm_key = min(hashmap, key=lambda k: hashmap[k])
                re_index = hashmap[rm_key]
                del hashmap[rm_key]
                left = re_index + 1
            else:
                max_str = max(max_str, right - left + 1)

            right += 1
        
        return max_str


