"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
"""
from typing import List


# 首先要sort之后two pointer。为避免重复，在于要让每一个重复的数第一次记录，之后全跳过【i-1】
class Solution:
    def threeSum(self, nums: List[int]) -> List[int]:
        # sort() will return None
        # temp = nums.sort()
        # sorted(nums) will return the sorted list
        # temp = sorted(nums)
        nums.sort()
        res = []
        for i in range(len(nums) - 2):
            if nums[i] > 0:
                break

            # compare i and i-1 for record the situation of i-1 when first round i=i-1
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1

            while l < r:
                if nums[l] + nums[r] < -nums[i]:
                    l += 1

                elif nums[l] + nums[r] > -nums[i]:
                    r -= 1

                # if nums[l] + nums[r] == -nums[i]:
                #     # print(res)
                #     res.append([nums[i], nums[l], nums[r]])
                elif nums[l] + nums[r] == -nums[i]:
                    # print(res)
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    # compare l and l-1 for record the situation of l-1 when first round l=l-1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1

            i += 1
        return res


print(Solution().threeSum(nums=[0, 0, 0, 0]))
