class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)  # add 0 to flush stack at end
        stack = [-1]  # stack of indexes, -1 is sentinel
        ans = 0  # largest area so far

        for i in range(len(heights)):  # go through each bar
            while heights[i] < heights[stack[-1]]:  # current bar is shorter
                height = heights[stack.pop()]  # pop bar to calculate
                width = i - stack[-1] - 1  # width between smaller bars
                ans = max(ans, width * height)  # update largest area
            stack.append(i)  # push current index

        heights.pop()  # remove the 0 we added
        return ans  # return largest area
