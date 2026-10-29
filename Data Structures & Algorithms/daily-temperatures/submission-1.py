class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        st = []  # stack of indexes waiting for warmer day
        res = [0] * len(temperatures)  # answer, default 0

        for i in range(len(temperatures)):  # go through each day
            while st and temperatures[i] > temperatures[st[-1]]:  # today is warmer than top day
                idx = st.pop()  # pop that waiting day
                res[idx] = i - idx  # days it waited
            st.append(i)  # push today, wait for warmer

        return res  # return answer
