class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1  # search range

        while left <= right:  # while range is valid
            mid = (left + right) // 2  # middle index

            if nums[mid] == target:  # found target
                return mid  # return index
            elif nums[mid] < target:  # middle too small
                left = mid + 1  # search right half
            else:  # middle too big
                right = mid - 1  # search left half

        return -1  # not found
