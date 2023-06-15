"""
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
"""
from collections import defaultdict
from typing import List


# 用dict把num出现的次数count记录，之后利用list的index越大越靠后list[count] = [num1, num2..]，最后从后面loop这个list，要几个k就先loop List[List],再[List[int]]
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        temp = defaultdict(int)
        # len(nums) + 1 bc if nums only have one the count of the frequence will also be 1 which will need the freq list be length of 2
        freq = [[] for _ in range(len(nums) + 1)]
        res = []
        for num in nums:
            temp[num] += 1

        # print(temp)

        # no sorted need to be under O(nlogn)
        # sortedTemp = sorted(temp.items(), key=lambda x: x[1], reverse=True)

        for num, count in temp.items():
            freq[count].append(num)
            # print(freq)

        # print(freq)

        # start point len(freq) - 1, end point smaller than 0, minus 1 each step
        for i in range(len(freq) - 1, -1, -1):
            if freq[i] == []:
                continue
            else:
                for num in freq[i]:
                    if len(res) < k:
                        res.append(num)
        return res


print(Solution().topKFrequent(nums=[3], k=1))
