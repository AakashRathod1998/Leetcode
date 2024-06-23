class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagrams = collections.defaultdict(list)

        for i, val in enumerate(strs):
            curr_str = ''.join(sorted(val)) 

            if curr_str not in anagrams:
                anagrams[curr_str] = []
            anagrams[curr_str].append(val)
        
        return (list(anagrams.values()))

        # strs_table = {}

        # for string in strs:
        #     sorted_string = ''.join(sorted(string))
        #     print(sorted_string)

        #     if sorted_string not in strs_table:
        #         strs_table[sorted_string] = []

        #     strs_table[sorted_string].append(string)

        # print(strs_table)
        # return list(strs_table.values())
