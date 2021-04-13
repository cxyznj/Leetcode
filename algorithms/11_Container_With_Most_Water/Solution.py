class Solution:
    def maxArea(self, height: List[int]) -> int:
        mostwater = 0
        left = 0
        right = len(height) - 1
        while left < right:
            if height[left] < height[right]:
                # right index should not move to the left more
                water = (right - left) * height[left]
                left += 1
            elif height[left] > height[right]:
                # left index should not move to the right more
                water = (right - left) * height[right]
                right -= 1
            else:
                # height[left] == height[right]
                # left and right should not move to the middle 
                water = (right - left) * height[left]
                left += 1
                right -= 1
            mostwater = water if mostwater < water else mostwater
        return mostwater
