class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Sort the array in non-decreasing order.
        nums.sort()
        for i in range(1, len(nums)): # Iterate through the array starting from index 1
            if nums[i] == nums[i-1]: # Compare the current element with the previous element.
                return True # if it is duplicate or equal, I return True
        return False # if it is not then False