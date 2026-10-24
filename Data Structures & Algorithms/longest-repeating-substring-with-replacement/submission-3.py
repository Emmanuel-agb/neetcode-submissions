class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}  # count chars in window
        res = 0  # longest valid window
        left = 0  # left pointer

        for right in range(len(s)):  # expand window right
            freq[s[right]] = freq.get(s[right], 0) + 1  # add right char

            while (right - left + 1) - max(freq.values()) > k:  # replacements needed > k
                freq[s[left]] -= 1  # remove left char
                left += 1  # shrink window

            res = max(res, right - left + 1)  # update longest

        return res  # return longest
