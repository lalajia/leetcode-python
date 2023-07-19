"""
There are n cars going to the same destination along a one-lane road. The destination is target miles away.
You are given two integer array position and speed, both of length n, where position[i] is the position of the ith car and speed[i] is the speed of the ith car (in miles per hour).
A car can never pass another car ahead of it, but it can catch up to it and drive bumper to bumper at the same speed. The faster car will slow down to match the slower car's speed. The distance between these two cars is ignored (i.e., they are assumed to have the same position).
A car fleet is some non-empty set of cars driving at the same position and same speed. Note that a single car is also a car fleet.
If a car catches up to a car fleet right at the destination point, it will still be considered as one car fleet.
Return the number of car fleets that will arrive at the destination.

Example 1:
Input: target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]
Output: 3
Explanation:
The cars starting at 10 (speed 2) and 8 (speed 4) become a fleet, meeting each other at 12.
The car starting at 0 does not catch up to any other car, so it is a fleet by itself.
The cars starting at 5 (speed 1) and 3 (speed 3) become a fleet, meeting each other at 6. The fleet moves at speed 1 until it reaches target.
Note that no other cars meet these fleets before the destination, so the answer is 3.
"""

from typing import List


# 先把速度和距离dict匹配后，根据距离sort。从后往前比较速度
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        temp = [[p, s] for p, s in zip(position, speed)]

        # sort by the first element of the sublist
        # sorted(temp) return a new list

        temp.sort()
        stack = []
        for p, s in reversed(temp):
            if len(stack) >= 1 and (target - p) / s <= stack[-1]:
                continue
            stack.append((target - p) / s)

        return len(stack)


print(Solution().carFleet(target=12, position=[10, 8, 0, 5, 3], speed=[2, 4, 1, 1, 3]))
# sort by the second element of the sublist x: x[1] (x: x[0] first element)
# sorted_result = sorted(temp, key=lambda x: x[1])
