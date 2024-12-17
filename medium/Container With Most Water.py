class Solution:
    def maxArea(self, heights: list[int]) -> int:
        if len(heights) < 2:
            return 0
        left = res = 0
        right = len(heights)-1
        while left < right:
            lower = min(heights[left],heights[right])
            water = (right-left) * lower
            res = max(water,res)
            if lower == heights[left]:
                left += 1
            else:
                right -= 1
        return res