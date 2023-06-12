"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
You must write an algorithm that runs in O(n) time.
Example 1:
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4."""

from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # use set to save time
        temp = set(nums)
        res = 0
        for num in temp:
            # save more time
            if (num - 1) not in temp:
                i = 1
                while (num + i) in temp:
                    i += 1
                res = max(i, res)
        return res


print(Solution().longestConsecutive(nums=[100, 4, 101, 1, 3, 3, 4, 2]))
