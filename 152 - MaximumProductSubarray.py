class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        maxProd = prevMin = prevMax = nums[0]

        for i in nums[1:]:

            vals = (i, i*prevMax, i*prevMin)
            currMax, currMin = max(vals), min(vals)
            maxProd = max(maxProd, currMax)

            prevMax, prevMin = currMax, currMin
        
        return maxProd
        
        # curMax, curMin = 1, 1
        # res = max(nums)

        # for i in nums:

        #     if i == 0:
        #         curMax, curMin = 1, 1
        #         continue
            
        #     temp = curMax * i
        #     curMax = max(curMax * i, curMin * i, i)
        #     curMin = min(temp, curMin * i, i)
            
        #     res = max(res, curMax)
        
        # return res
