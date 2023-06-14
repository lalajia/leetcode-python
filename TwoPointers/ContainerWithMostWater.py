"""
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
"""


from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        res = 0
        while l < r:
            # while r > l:
            #     temp = (r - l) * min(height[r], height[l])
            #     res = max(temp, res)
            #     r -= 1
            # r = len(height) - 1
            # l += 1
            temp = (r - l) * min(height[r], height[l])
            res = max(temp, res)

            if height[l] <= height[r]:
                l += 1
            elif height[l] > height[r]:
                r -= 1

        return res


print(Solution().maxArea(height=[1, 8, 6, 2, 5, 4, 8, 3, 7]))
