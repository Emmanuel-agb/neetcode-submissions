class Solution:

    def encode(self, strs: List[str]) -> str:
        res = [] # Initialize an empty list to encode strings
        for s in strs: # Computed each string in the list
            # Appended the length string to the builder
            res.append(str(len(s)))
            res.append("#")
            res.append(s)
        return "".join(res) # Return the final encoding

    def decode(self, s: str) -> List[str]:
        res = [] # Initialize empty list to decode surings
        i = 0 

        while i < len(s): # move j forward till I find "#"
            j = i

            while s[j] != "#":
                j += 1
            length = int(s[i:j]) # convert substring to an integer
            i = j + 1
            j = i + length # extracting the next length characters
            res.append(s[i:j]) # append the extracted results
            i = j # move i forward to decode the next segment
        return res # return the decoded list