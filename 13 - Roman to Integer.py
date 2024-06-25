class Solution:
    def romanToInt(self, s: str) -> int:

        res, prev = 0, 0
        dict_roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        for i in s[ : :-1]:
            if dict_roman[i] >=prev:
                res+= dict_roman[i]
            else:
                res-= dict_roman[i]
            prev = dict_roman[i]
            print(i,dict_roman[i], prev, res)
        return res
