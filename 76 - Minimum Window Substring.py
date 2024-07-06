class Solution:
    def minWindow(self, s: str, t: str) -> str:

        countT = collections.Counter(t)
        window = {}
        res, resLen = [-1,-1], float(inf)
        have = 0
        need = len(countT)

        l = r = 0

        while r < len(s):
            char = s[r]

            if char not in window:
                window[char] = 1
            else:
                window[char] += 1
            
            if char in countT and window[char] == countT[char]:
                have += 1
    
            while have == need:
                if (r-l+1) < resLen:
                    res = [l,r]
                    resLen = (r-l+1)
    
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
            r += 1

        return s[res[0]: res[1]+1]
