"""
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
In other words, return true if one of s1's permutations is the substring of s2.

Example 1:
Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:
Input: s1 = "ab", s2 = "eidboaoo"
Output: false
"""


# 把s1字母出现的次数放到int array里面。右指针loop s2，右指针出现的字母在减去int array。while loop如果该字母s1里面没有的话，把当前左指针的字母再加回去，左指针+1。最后如果左右指针和s1的长度相同，return True
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        temp = [0] * 26
        for c in s1:
            temp[ord(c) - ord("a")] += 1

        left, right = 0, 0
        for right in range(len(s2)):
            temp[ord(s2[right]) - ord("a")] -= 1

            while temp[ord(s2[right]) - ord("a")] < 0:
                temp[ord(s2[left]) - ord("a")] += 1
                left += 1

            if right - left + 1 == len(s1):
                return True

        return False


print(Solution().checkInclusion(s1="adc", s2="dcda"))
