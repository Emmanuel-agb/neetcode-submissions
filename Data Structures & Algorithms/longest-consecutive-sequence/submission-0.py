class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums) # convert list to numSet for O(1) lookups
        longest = 0 # initialize longest to track the length of lcs
        
        # For each number in nums
        for n in nums:
            # check if its start of sequence
            if (n - 1) not in numSet:
                length = 1
                while (n + length) in numSet: # Increase length
                    length += 1
                longest = max(length, longest) # update longest with max length found
        return longest # return the longest after scanning all numbers