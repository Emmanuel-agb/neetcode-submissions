class Solution:
    def isValid(self, s: str) -> bool:
        stack = []  # store open brackets
        mapping = {")": "(", "}": "{", "]": "["}  # close -> matching open

        for char in s:  # check each char
            if char in mapping.values():  # open bracket
                stack.append(char)  # push to stack
            elif char in mapping.keys():  # close bracket
                if not stack or mapping[char] != stack.pop():  # no match on top
                    return False  # invalid

        return not stack  # valid if stack empty
