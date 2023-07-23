"""
Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".
The testcases will be generated such that the answer is unique.

Example 1:
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
"""


# 和longest repeat有点像，记录t的所有字母出现的次数；用右指针loop s，首先记录如果有与t相同的字母出现，have+1。当have=t当长度时，记录下更大的结果的长度和位置，如果当前左指针是t中的字母，have-1，挪动左指针
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left, right = 0, 0
        tCount = {}
        sCount = {}
        have = 0
        resLen = float("inf")
        res = []
        if len(t) > len(s):
            return ""
        for c in t:
            tCount[c] = tCount.get(c, 0) + 1

        for right in range(len(s)):
            rChar = s[right]
            if rChar in tCount:
                sCount[rChar] = sCount.get(rChar, 0) + 1
                if tCount[rChar] == sCount[rChar]:
                    have += 1

            # 这个condition很关键
            while have == len(tCount):
                lChar = s[left]
                if right - left + 1 < resLen:
                    resLen = right - left + 1
                    res = [left, right]
                if lChar in tCount:
                    sCount[lChar] -= 1
                    if sCount[lChar] != tCount[lChar]:
                        have -= 1
                left += 1

        return s[res[0] : res[1] + 1] if resLen != float("inf") else ""


print(Solution().minWindow(s="ADOBECODEBANC", t="ABC"))
print(Solution().minWindow(s="A", t="B"))
