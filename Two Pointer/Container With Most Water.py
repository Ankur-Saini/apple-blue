class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        left = 0
        right = n - 1
        max_area = 0
        area = 0
        while left < right:
            area = (right - left) * min(height[left], height[right])
            if area > max_area:
                max_area = area
            if height[left] <= height[right]:
                left += 1
            elif height[left] > height[right]:
                right -= 1
        return max_area
# Time complexity - O(n)
