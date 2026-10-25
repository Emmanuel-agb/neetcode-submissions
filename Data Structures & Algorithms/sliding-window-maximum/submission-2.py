class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []  # max-heap using negative values
        output = []  # max for each window

        for i in range(len(nums)):  # go through nums
            heapq.heappush(heap, (-nums[i], i))  # push value and index

            if i >= k - 1:  # window is full size k
                while heap[0][1] <= i - k:  # top is outside window
                    heapq.heappop(heap)  # remove old top

                output.append(-heap[0][0])  # top is window max

        return output  # return all window maxes
