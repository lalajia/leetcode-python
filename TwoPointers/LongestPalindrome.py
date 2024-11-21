"""
Given a string s, return the longest 
palindromic substring in s.

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        res_len = 0

        for i in range(len(s)):
            # odd
            left, right = i, i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if res_len < right - left + 1:
                    res_len = max(res_len, right - left + 1)
                    res = s[left : right + 1]
                left -= 1
                right += 1

            # even
            left, right = i, i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if res_len < right - left + 1:
                    res_len = max(res_len, right - left + 1)
                    res = s[left : right + 1]
                left -= 1
                right += 1

        return res


print(Solution().longestPalindrome(s="cbbd"))
