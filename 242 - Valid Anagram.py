class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        return (sorted(s) == sorted(t))
        
        # sorted_s = ''.join(sorted(s,key = lambda x: x))
        # sorted_t = ''.join(sorted(t,key = lambda x: x))
        
        # print(sorted_s, sorted_t)
        
        # if sorted_s == sorted_t:
        #     return True
        # else:
        #     return False
        
