class Solution:
    def trap(self, height: list[int]) -> int:
        left = 0  # left pointer
        right = len(height) - 1  # right pointer
        left_max = height[left]  # max from left
        right_max = height[right]  # max from right
        water = 0  # total water

        while left < right:  # until pointers meet
            if left_max < right_max:  # left wall is smaller
                left += 1  # move left in
                left_max = max(left_max, height[left])  # update left max
                water += left_max - height[left]  # add trapped water
            else:  # right wall is smaller
                right -= 1  # move right in
                right_max = max(right_max, height[right])  # update right max
                water += right_max - height[right]  # add trapped water

        return water  # return total
