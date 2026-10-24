class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = left = 0  # best length, left pointer
        count = {}  # count chars in window

        for right, c in enumerate(s):  # right pointer, current char
            count[c] = 1 + count.get(c, 0)  # add c to window

            while count[c] > 1:  # c is duplicate
                count[s[left]] -= 1  # remove left char
                left += 1  # shrink window from left

            max_length = max(max_length, right - left + 1)  # update best length

        return max_length  # return best length
