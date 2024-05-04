class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for index,value in enumerate(nums):
            difference = target - value
            if difference in seen:
                return (index,seen[difference])
            else:
                seen[value] = index
