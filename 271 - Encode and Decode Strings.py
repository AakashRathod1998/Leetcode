class Codec:
    def encode(self, strs):
        """Encodes a list of strings to a single string."""
        return 'π'.join(strs)
        
    def decode(self, s):
        """Decodes a single string to a list of strings."""
        return s.split('π')


# class Codec:
#     def encode(self, strs: List[str]) -> str:
#         result = []
        
#         for string in strs:
#             for c in string:
#                 result.append(str(ord(c)))
#                 result.append(';')
#             result.append(' ')
                
#         return ''.join(result)
        

#     def decode(self, s: str) -> List[str]:
#         result = []
#         strings = s.split(' ')
#         print(strings)
		
#         for string in strings:
#             temp = []
#             for c in string.split(';'):
#                 if c:
#                     temp.append(chr(int(c)))
#             result.append(''.join(temp))
			
#         result.pop()
#         return result
