"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
You must implement a solution with O(1) time complexity for each function.

Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]
"""


class Solution:
    def __init__(self) -> None:
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        # if self.minStack is not None or self.minStack[-1] > val:
        #     self.minStack.clear()
        #     val = min
        #     self.minStack.append(val)
        if self.minStack:
            val = min(val, self.minStack[-1])

        self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]


obj = Solution()

obj.push(6)
obj.push(5)
obj.push(3)
print(obj.stack)
obj.pop()
print(obj.stack)
param_3 = obj.top()
param_4 = obj.getMin()

print(obj.minStack)
print(param_3, param_4)
