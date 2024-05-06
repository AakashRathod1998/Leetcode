class Solution:
    def maxArea(self, height: List[int]) -> int:

        left = 0
        right = len(height) - 1
        water = 0

        if not height:
            return 0
        
        while left < right:

            curr_fill = abs(left - right) * min(height[left], height[right])
            water = max(water, curr_fill)

            if height[left] < height[right]:
                left = left + 1
            else:
                right = right - 1
        
        return water

        # l,r,area = 0,len(height)-1,0

        # if not height:
        #     return 0

        # while l < r:
        #     area = max(area,(r-l)*min(height[l],height[r]))
        #     if height[l] < height[r]:
        #         l+=1
        #     else:
        #         r-=1
        # return area
