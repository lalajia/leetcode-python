from typing import List


# 还是hashset的创建hashset = set()
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False


print(Solution().containsDuplicate(nums=[2, 7, 11, 11]))
