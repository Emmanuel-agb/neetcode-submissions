class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""  # edge case, nothing to find

        countT, window = {}, {}  # need from t, count in window
        for c in t:  # build need map
            countT[c] = 1 + countT.get(c, 0)  # count char in t

        have, need = 0, len(countT)  # satisfied chars, total needed
        res, res_len = [-1, -1], float("inf")  # best window, best length
        left = 0  # left pointer

        for right in range(len(s)):  # expand window right
            c = s[right]  # current char
            window[c] = 1 + window.get(c, 0)  # add char to window

            if c in countT and window[c] == countT[c]:  # char satisfied
                have += 1  # one more satisfied

            while have == need:  # window has all of t
                if (right - left + 1) < res_len:  # smaller window found
                    res = [left, right]  # save window
                    res_len = right - left + 1  # save length

                window[s[left]] -= 1  # remove left char
                if s[left] in countT and window[s[left]] < countT[s[left]]:  # char now missing
                    have -= 1  # no longer satisfied
                left += 1  # shrink window

        l, r = res  # unpack best window
        return s[l : r + 1] if res_len != float("inf") else ""  # return substring or empty
