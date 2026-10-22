class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # sort the array first, e.g. [-1,0,1,2,-1,-4] becomes [-4,-1,-1,0,1,2]
        res = set()  # res stores the answers, set = no duplicate triplets allowed

        for i, a in enumerate(nums):  # loop: i = index, a = first number of the triplet
            if i > 0 and nums[i] == nums[i - 1]:  # if this a is same as previous a, we already checked it
                continue  # skip it, to avoid duplicate work

            seen = set()  # for this a, seen remembers the b values we have already passed
            for b in nums[i + 1:]:  # b = second number, only check numbers AFTER a
                c = -a - b  # c = third number we NEED, because a + b + c must = 0

                if c in seen:  # if we saw c before as a b, then a + b + c = 0 is found
                    res.add((a, b, c))  # save this triplet in res

                seen.add(b)  # now add current b to seen, so future b can pair with it as c

        return list(res)  # res is a set, convert it to list and return it
