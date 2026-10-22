class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) # Initialize empty defaultdict(list) to store anagram groups

        for s in strs: # Start loop, current string s
            key = ''.join(sorted(s)) # Sort the characters of the string to form a key.
            res[key].append(s) # Append the original string to the list corresponding to this key.
        return list(res.values()) # Return values as list of lists