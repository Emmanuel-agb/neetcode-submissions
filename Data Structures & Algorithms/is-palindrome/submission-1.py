class Solution:
    def isPalindrome(self, s: str) -> bool:

        # Convert all letters to lowercase
        # Keep only letters and numbers, removing spaces and punctuation
        s = ''.join(filter(str.isalnum, s.lower()))

        # Reverse the cleaned string and compare it with the original
        # If both are equal, the string is a palindrome
        return s==s[::-1]