class Solution:
    def rob(self, nums: List[int]) -> int:

        first = second = 0

        for third in nums:
            odd = max(first + third, second)
            first = second
            second = odd
        return second
