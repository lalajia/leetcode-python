"""
Given a string s, find the length of the longest 
substring without repeating characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
"""
from typing import Set


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        temp = set()
        left, right = 0, 0
        res = 0
        for right in range(len(s)):
            # if s[right] in temp:
            #     left = right
            #     temp.clear()
            # 不能用if全删掉因为会有只有一个重复的字母的情况
            while s[right] in temp:
                # 不能删right因为是挪left指针要保留right的内容在temp里面
                temp.remove(s[left])
                left += 1
            temp.add(s[right])
            res = max(res, right - left + 1)
            # res = max(res, len(temp)) #一样的效果

        return res


# print(Solution().lengthOfLongestSubstring(s="dvdf"))
print(Solution().lengthOfLongestSubstring(s="pwwkew"))
