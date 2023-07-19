"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

Example 1:
Input: s = "([{}])"
Output: true
"""


# 主要要有dict对应起来所有的括号，之后遍历input来确定是否每一个左括号都有对应的右括号
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        stack = []
        dict = {")": "(", "]": "[", "}": "{"}
        for char in s:
            if char in dict:
                if stack and stack[-1] == dict[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)

        if stack:
            return False
        else:
            return True


print(Solution().isValid(""))
