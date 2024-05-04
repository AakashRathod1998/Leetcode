import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        left = [1] * len(nums)
        right = [1] * len(nums)

        for i in range(1, len(nums)):
            left[i] = left[i] * nums[i-1] * left[i-1]
        
        for i in range(len(nums)-2,-1,-1):
            right[i] = right[i+1] * nums[i+1]
            left[i] = left[i] * right[i]
        
        return left

        # prefix,postfix = 1,1
        # res = [0] * len(nums)

        # for i in range(len(nums)-1,-1,-1):
        #     res[i] = prefix
        #     prefix *=nums[i]
        
        # for j in range(0,len(nums)):
        #     res[j] *= postfix
        #     postfix *= nums[j]
        # return res



