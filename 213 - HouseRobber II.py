class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]
                    
        first = second = 0

        for third in nums[:-1]:
            odd = max(first + third, second)
            first = second
            second = odd
        OddProfit = second

        first = second = 0

        for third in nums[1:]:
            even = max(first + third, second)
            first = second
            second = even
        return max(OddProfit, second)
        
