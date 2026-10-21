class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums) # Initialize output with all values set to 1

        left = 1 # Initialize the left variable
        for i in range(len(nums)): # Left-to-right loop (calculate left-side products)
            output[i] *= left
            left *= nums[i]

        right = 1 # Initialize the right variable
        for i in range(len(nums) -1, -1, -1): # Right-to-left loop (calculate right-side products)
            output[i] *= right
            right *= nums[i]

        return output
