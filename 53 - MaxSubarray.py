# Sliding Window Technique
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        maxSum = currMax = nums[0]

        for i, num in enumerate(nums[1:]):
            currMax = max(num, num+currMax)
            maxSum = max(maxSum, currMax)
        
        return maxSum

        
# Approach 2
        maxSum = nums[0]
        currSum = 0

        for i in nums:
            if currSum < 0:
                currSum = 0
            currSum += i
            maxSum = max(maxSum, currSum)
            print(maxSum, currSum)
        return maxSum

# Approach 3
        left, right = 0, 0
        window_sum, max_sum = 0, float('-inf')
        while right < len(nums):
            # Expand the window to the right
            window_sum += nums[right]
            right += 1
            # Update the maximum subarray sum seen so far
            max_sum = max(max_sum, window_sum)
            # Shrink the window from the left if the sum is negative
            while window_sum < 0:
                window_sum -= nums[left]
                left += 1
        return max_sum
