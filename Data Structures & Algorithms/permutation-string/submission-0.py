class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)  # lengths of s1 and s2
        ctr1, ctr2 = Counter(s1), Counter(s2[:n1])  # count s1, count first window in s2

        for i in range(n1, n2):  # slide window through s2
            if ctr1 == ctr2: return True  # window matches s1

            ctr2[s2[i - n1]] -= 1  # remove left char
            ctr2[s2[i]] += 1  # add new right char

        return ctr1 == ctr2  # check last window
