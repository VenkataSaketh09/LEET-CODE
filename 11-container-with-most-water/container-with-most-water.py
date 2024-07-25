class Solution:
    def maxArea(self, height: List[int]) -> int:
        left=0
        right=len(height)-1
        water=0
        temp_water=0
        while left<right:
            height_comparison=min(height[left],height[right])
            length=right-left
            temp_water=height_comparison*length
            water=max(water,temp_water)
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return water
            
        