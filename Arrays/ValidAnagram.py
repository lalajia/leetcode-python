# 用dict记录每一个字母是否出现，之后对比这两个dict如果一样就True
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        CountS, CountT = {}, {}
        for i in range(len(s)):
            # mind the parathesis
            CountS[s[i]] = 1 + CountS.get(s[i], 100)
            CountT[t[i]] = 1 + CountT.get(t[i], 100)

        return CountT == CountS


print(Solution().isAnagram("ab", "ab"))
