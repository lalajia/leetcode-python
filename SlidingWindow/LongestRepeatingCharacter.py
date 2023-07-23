"""
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.
Return the length of the longest substring containing the same letter you can get after performing the above operations.

Example 1:
Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.
"""


from collections import defaultdict


# 左右点都从0开始，已right为限制，相同出现的字母count + 1，记录最大值。如果当前window减去需要取代的数字大于可以取代的数字k，那么挪动左边的指针
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left, right = 0, 0
        count = {}
        temp = 0
        for right in range(len(s)):
            count[s[right]] = count.get(s[right], 0) + 1
            # Update temp to the maximum frequency of any character in the current window
            temp = max(count[s[right]], temp)
            # If the size of the current window minus temp is greater than k,
            # we need to shrink the window from the left side
            if (right - left + 1) - temp > k:
                # Decrease the frequency of the character at the left pointer
                count[s[left]] -= 1
                # Move the left pointer to the right, shrinking the window
                left += 1
        return right - left + 1


print(Solution().characterReplacement(s="BAAA", k=1))


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
