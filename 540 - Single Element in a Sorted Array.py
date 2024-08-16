class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        
        left = 0
        right = len(nums) - 1

        if len(nums) == 1:
            return nums[0]

        while left < right:

            mid = (right+left)//2

            if (right-left) == 2:
                if nums[mid] == nums[right]:
                    return nums[left]
                else:
                    return nums[right]

            if nums[mid] != nums[mid+1]:
                if (nums[mid-1] != nums[mid]):
                    return nums[mid]
                if (right-mid)%2 == 0:
                    right = mid-2
                elif (right-mid)%2 != 0:
                    left = mid+1
            elif nums[mid] == nums[mid+1]:
                if ((mid - left) %2 == 0) and (sum(nums[left:mid])%2 == 0):
                    left = mid + 2
                else:
                    right = mid-1
                
        return nums[left]

