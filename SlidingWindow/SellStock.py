"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
"""

from typing import List


# 当右指针小于左指针，左指针=右指针，记录最低点，然后记录最大值
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0, 1
        res = 0
        for right in range(len(prices)):
            # 找到最低点
            if prices[right] - prices[left] < 0:
                left = right
            else:
                res = max(res, prices[right] - prices[left])
            # right += 1
        return res


print(Solution().maxProfit(prices=[0, 3]))
