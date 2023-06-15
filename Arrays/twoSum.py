from typing import List


# 反过来用dict，算diff
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in hashMap:
                return [hashMap[diff], i]
            hashMap[nums[i]] = i

        return []


print(Solution().twoSum(nums=[2, 7, 11, 15], target=9))
