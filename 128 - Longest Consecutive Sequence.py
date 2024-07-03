class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if len(nums) <= 1:
            return len(nums)

        num = sorted(list(set(nums)))
        # print(num)

        start = 0
        max_seq = 0

        for i,val in enumerate(num):
            
            if i == 0:
                continue
            if val == num[i-1]+1:
                max_seq = max(max_seq, i-start+1)
            else:
                start = i
            # print(start,i)
            # print('----',val,num[i-1])
        return max(max_seq,1)


        # Approach 2
        nums = set(nums)
        best = 0
        for x in nums:
            if x - 1 not in nums:
                y = x + 1
                while y in nums:
                    y += 1
                best = max(best, y - x)
        return best
