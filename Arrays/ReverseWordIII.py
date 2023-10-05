# Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

# Example 1:

# Input: s = "Let's take LeetCode contest"
# Output: "s'teL ekat edoCteeL tsetnoc"
# Example 2:

# Input: s = "God Ding"
# Output: "doG gniD"


class Solution:
    def reverseWords(self, s: str) -> str:
        res = ""
        if len(s) == 1:
            res = s

        i, j = 0, 0
        while i < len(s):
            # Find the start and end of a word
            while i < len(s) and s[i] == " ":
                i += 1
            j = i
            while j < len(s) and s[j] != " ":
                j += 1

            # Reverse the word and append it to the result
            word = s[i:j][::-1]
            res += word

            # Append a space unless it's the last word
            if j < len(s):
                res += " "

            i = j + 1

        return res

        # while i in range(len(s)):
        #     temp = ""
        #     while s[j] != " " or j == len(s) - 1:
        #         temp += s[j]
        #         j += 1
        #     part = temp[::-1] + " "
        #     res += part
        #     i = j + 1
        #     j = i

        # return res


print(Solution().reverseWords(s="Let's take LeetCode contest"))
