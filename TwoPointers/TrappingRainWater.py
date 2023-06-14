"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.
Example 1:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
"""
from collections import defaultdict
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        # maxLeft, maxRight = 0, 0
        maxLeft, maxRight = height[l], height[r]
        res = 0
        while l < r:
            if maxLeft <= maxRight:
                l += 1
                # maxLeft = max(maxLeft, height[l - 1])
                maxLeft = max(maxLeft, height[l])
                # if height[l] - min(maxLeft, maxRight) > 0:
                #     res += height[l - 1] - min(maxLeft, maxRight)
                res += maxLeft - height[l]

            else:
                r -= 1
                # maxRight = max(maxRight, height[r + 1])
                maxRight = max(maxRight, height[r])
                # if height[r] - min(maxLeft, maxRight) > 0:
                #     res += height[r + 1] - min(maxLeft, maxRight)
                res += maxRight - height[r]

        return res


print(Solution().trap(height=[1, 2, 3, 2, 1]))


# def wasted(self, height: List[int]) -> int:
#         heightDic = defaultdict(set)
#         i = 0
#         while i < len(height) and height[i] <= max(height):
#             if height[i] == 0:
#                 i += 1
#                 continue
#             j = 0
#             while j < len(height):
#                 if height[j] >= height[i]:
#                     heightDic[height[i]].add(j)
#                 j += 1
#             i += 1
#         print(heightDic)
#         res = 0
#         for index in heightDic.values():
#             value = sorted(index)
#             # print(value)
#             for i, num in enumerate(value):
#                 if value[i] < value[i - 1]:
#                     # print("A")
#                     continue
#                 else:
#                     if len(value) <= 1:
#                         res += value[i] - value[i - 1]
#                     else:
#                         res += value[i] - value[i - 1] - 1
#         return res
