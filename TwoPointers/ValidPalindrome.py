"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
Given a string s, return true if it is a palindrome, or false otherwise.
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
"""


# 主要是isalnum()针对string 和 character对于非字母和数字的检测
class Solution:
    def isPalindrome(self, s: str) -> bool:
        temp = s.lower()
        i, j = 0, len(s) - 1
        while i < j:
            while i < j and not temp[i].isalnum():
                # print(temp[i].isalnum())
                i += 1

            while i < j and not temp[j].isalnum():
                # print("A")
                j -= 1

            if temp[i] != temp[j]:
                return False
            i += 1
            j -= 1

        return True


print(Solution().isPalindrome(" "))
