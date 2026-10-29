class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)  # speed range: 1 to max pile
        res = r  # best speed so far

        while l <= r:  # binary search the speed
            k = (l + r) // 2  # try middle speed

            totalTime = 0  # hours needed at speed k
            for p in piles:  # check each pile
                totalTime += math.ceil(float(p) / k)  # hours for this pile, round up

            if totalTime <= h:  # can finish in time
                res = k  # save this speed
                r = k - 1  # try slower speed
            else:  # too slow
                l = k + 1  # try faster speed

        return res  # minimum speed
