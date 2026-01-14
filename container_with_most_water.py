# 11. Container With Most Water
# You are given an integer array height of length n. There are n vertical lines drawn such that the two
# endpoints of the ith line are (i, 0) and (i, height[i]).
# Find two lines that together with the x-axis form a container, such that the container contains the most water.
# Return the maximum amount of water a container can store.
# Notice that you may not slant the container.
# Example 1:
# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, 
# the max area of water (blue section) the container can contain is 49.
# Example 2:
# Input: height = [1,1]
# Output: 1
# Constraints:
# n == height.length
# 2 <= n <= 10^5
# 0 <= height[i] <= 10^4

def maxArea(height):
        n = len(height)
        l = 0
        r = n - 1
        max_area = 0

        while l < r:
            # Alto * ancho
            area = min(height[l], height[r]) * (r - l)
            max_area = max(max_area, area)

            if height[l] < height[r]:
                l+=1
            else: 
                r -=1

        return max_area            
        
print(maxArea([8,7,2,1]))        