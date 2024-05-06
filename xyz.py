import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = 1
        right = 1
        
        result = [0]* len(nums)
        
        for i in range(len(nums)-1,-1,-1):
            result[i] = left
            left = left * nums[i]
        
        for j in range(0,len(nums)):
            result[j] *=right
            right = right*nums[j]

        return result

