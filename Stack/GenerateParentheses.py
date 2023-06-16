"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example 1:
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
"""


from typing import List


class Solution:
    def generateParentheses(self, n: int) -> List[str]:
        stack = []
        res = []
        # 1. n == leftN == rightN
        # 2. n > leftN "+("
        # 3. leftN > rightN "+)"

        def backTrack(leftN, rightN):
            if n == leftN == rightN:
                """res.append("".join(stack)): This line joins the elements in the stack list into a single string, using an empty string "" as the separator. The resulting string is then appended to the res list. For example, if stack is ["a", "b", "c"], " ".join(stack) will result in the string "abc". So, "abc" will be appended to the res list as a single element."""
                res.append("".join(stack))
                # res.append(stack)
                return
            if n > leftN:
                stack.append("(")
                backTrack(leftN + 1, rightN)
                stack.pop()

            if leftN > rightN:
                stack.append(")")
                backTrack(leftN, rightN + 1)
                stack.pop()

        backTrack(0, 0)
        return res


print(Solution().generateParentheses(3))
