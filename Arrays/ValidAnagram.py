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
