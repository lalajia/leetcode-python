"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.
Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]
"""


from typing import List


# 从左到num x 从右到num
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left, right = [1] * len(nums), [1] * len(nums)
        temp = 1
        for i in range(len(left)):
            left[i] = temp
            temp *= nums[i]
            print(left)

        # method 1
        # temp = 1
        # for i in range(len(right) - 1, -1, -1):
        #     right[i] = temp
        #     temp *= nums[i]
        #     print(right)

        # res = [0] * len(nums)
        # for i in range(len(res)):
        #     res[i] = left[i] * right[i]
        # return res

        # method 2
        temp = 1
        for i in range(len(right) - 1, -1, -1):
            right[i] = left[i] * temp
            temp *= nums[i]

        return right


print(Solution().productExceptSelf(nums=[1, 2, 3, 4]))
