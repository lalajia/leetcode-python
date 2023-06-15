"""
You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.
Evaluate the expression. Return an integer that represents the value of the expression.
Note that:
The valid operators are '+', '-', '*', and '/'.
Each operand may be an integer or another expression.
The division between two integers always truncates toward zero.
There will not be any division by zero.
The input represents a valid arithmetic expression in a reverse polish notation.
The answer and all the intermediate calculations can be represented in a 32-bit integer.

Input: tokens = ["4","13","5","/","+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6
"""

from typing import List
import math


# 必须要把算出来的结果存到stack里面，才能为下一个运算铺路
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for element in tokens:
            if element == "+":
                stack.append(stack.pop() + stack.pop())
            elif element == "-":
                temp = stack.pop()
                stack.append(stack.pop() - temp)
            elif element == "*":
                stack.append(stack.pop() * stack.pop())
            elif element == "/":
                temp = stack.pop()
                stack.append(math.trunc(stack.pop() / temp))
            else:
                stack.append(int(element))

        return stack[-1]


print(Solution().evalRPN(tokens=["4", "13", "5", "/", "+"]))
