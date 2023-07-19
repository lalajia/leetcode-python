"""
Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:
[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].
Given the sorted rotated array nums of unique elements, return the minimum element of this array.
You must write an algorithm that runs in O(log n) time.


Example 1:
Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.
"""

from typing import List


# 分类：mid小于右边，最小值在左边或者中间（12345，45123），mid大于右边，最小值在右边（34512）
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            if nums[mid] < nums[right]:
                right = mid
            else:
                left = mid + 1

        # while l <= r:
        #     if nums[l] <= nums[r]:
        #         return nums[l]
        #     mid = (l + r) // 2
        #     if nums[mid] <= nums[r]:
        #         r = mid
        #     else:
        #         l = mid + 1

        return nums[left]


print(Solution().findMin(nums=[3, 4, 5, 1, 2]))
