class Solution(object):
    def isValid(self, s):
        # d = {'(': ')', '{': '}', '[': ']'}
        # stack = []
        
        # for i in s:
        #     if i in d:  
        #         stack.append(i)
        #     elif len(stack) == 0 or d[stack.pop()] != i:  
        #         return False
        
        # return len(stack) == 0

        open_bracks = []
        
        for i in s:
            if i in '([{':
                open_bracks.append(i)
            else:
                if not open_bracks or \
                    (i == ')' and open_bracks[-1] != '(') or \
                    (i == '}' and open_bracks[-1] != '{') or \
                    (i == ']' and open_bracks[-1] != '['):
                    return False
                else:
                    open_bracks.pop()
        return not open_bracks

