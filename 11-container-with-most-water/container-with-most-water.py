class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0 
        l,r = 0, len(height)-1

        while l < r:
            width_w = (r-l)
            height_h  = min(height[l], height[r])
            area = width_w * height_h
            max_area = max(max_area, area)

            if height[l] <  height[r]:
                l += 1 
            else:
                r -= 1 
        return max_area