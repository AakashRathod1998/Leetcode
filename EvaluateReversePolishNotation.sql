class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        li = [] 
        i = 0
        val1, val2 = 0, 0

        while i < len(tokens):

            if tokens[i] in '+ - * /':
                
                if not li:
                    return
                
                val1 = li.pop(-1)
                val2 = li.pop(-1)

                if tokens[i] == '+':
                    var = val2 + val1
                    li.append(var)
                elif tokens[i] == '-':
                    var = val2 - val1
                    li.append(var)
                elif tokens[i] == '/':
                    var = int(val2 / val1)
                    li.append(var)
                elif tokens[i] == '*':
                    var = val2 * val1
                    li.append(var)

            else:
                li.append(int(tokens[i])) 

            i += 1

        return li[0] 
