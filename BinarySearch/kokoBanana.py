"""
Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.
Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.
Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.
Return the minimum integer k such that she can eat all the bananas within h hours.
Example 1:
Input: piles = [3,6,7,11], h = 8
Output: 4
"""
from typing import List
import math


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # res = max(piles)
        # new_list = list(range(res + 1))
        # left = 1
        # right = len(new_list) - 1
        left = 1
        right = max(piles)
        res = right

        while left <= right:
            mid = left + (right - left) // 2
            temp = 0
            for pile in piles:
                temp += math.ceil(pile / mid)
            if temp <= h:
                res = min(res, mid)
                right = mid - 1
            else:
                left = mid + 1

        return res


print(Solution().minEatingSpeed(piles=[30, 11, 23, 4, 20], h=5))
