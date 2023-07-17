"""
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.
Return the length of the longest substring containing the same letter you can get after performing the above operations.

Example 1:
Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.
"""


from collections import defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left, right = 0, 0
        # count = defaultdict(int)
        # 如果不是最开始的点开始的substring就不成立了
        # for c in s:
        #     count[c] += 1
        #     temp = max(count.values())
        #     if right + 1 - temp <= k:
        #         res = max(res, right - left + 1)
        #         right += 1
        #     else:
        #         left += 1
        #         count[s[left]] -= 1

        count = {}
        temp = 0
        for right in range(len(s)):
            count[s[right]] = count.get(s[right], 0) + 1
            temp = max(count[s[right]], temp)
            if (right - left + 1) - temp > k:
                count[s[left]] -= 1
                left += 1
        return right - left + 1


print(Solution().characterReplacement(s="BAAA", k=0))
