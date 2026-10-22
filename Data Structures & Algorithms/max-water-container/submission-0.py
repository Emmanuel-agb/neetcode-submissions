class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0  # left pointer starts at the first line, so we start with the widest container
        right = len(heights) - 1 # right pointer starts at the last line, the other end of the container
        max_area = 0 # stores the largest area we have found so far, starts at 0

        # keep checking pairs until the two pointers meet in the middle
        while left < right:
            # area = width (right - left) * height
            max_area = max(max_area, (right - left) * min(heights[left], heights[right]))

            if heights[left] < heights[right]: # left is shorter
                left += 1 # move in left inward to find a taller left line
            else: # else right line is shorter
                right -= 1 # move right pointer one step inward to try to find a taller right line
        return max_area # after checking all, return the biggest area we found