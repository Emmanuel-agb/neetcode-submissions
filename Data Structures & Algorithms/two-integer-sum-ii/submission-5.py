class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Initialize Two Pointers
        left, right = 0, len(numbers) - 1

        while left < right:
            curSum = numbers[left] + numbers[right] # Compute curSum = numbers[l] + numbers[r].

            if curSum > target: # If curSum > target, move r left to reduce the sum.
                right -= 1
            elif curSum < target: # If curSum < target, move l right to increase the sum.
                left += 1
            else:
                return [1 + left, right + 1] # If curSum == target, return [l + 1, r + 1].
        return []