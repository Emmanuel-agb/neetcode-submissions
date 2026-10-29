class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [[p, s] for p, s in zip(position, speed)]  # pair position with speed
        stack = []  # times for each fleet

        for p, s in sorted(cars)[::-1]:  # closest to target first
            time_taken = (target - p) / s  # time for this car to reach

            if not stack or time_taken > stack[-1]:  # slower than fleet ahead, new fleet
                stack.append(time_taken)  # push fleet time

        return len(stack)  # number of fleets
