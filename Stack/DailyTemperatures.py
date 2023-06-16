"""
Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

Example 1:
Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
"""

from typing import List


# 用stack做出一个monotonic decreasing的array，记录所有没有找到比他大的数的index，一旦有，就减去stack.pop最后一位的index，计算出当前index-stack最后一位的index，然后再把新的数的index加进去
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        for i in range(len(temperatures)):
            if stack == []:
                stack.append(i)
            else:
                while stack and temperatures[stack[-1]] < temperatures[i]:
                    temp = stack.pop()
                    res[temp] = i - temp
                stack.append(i)

        return res


print(Solution().dailyTemperatures(temperatures=[73, 74, 75, 71, 69, 72, 76, 73]))
