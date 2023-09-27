class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        # str = []
        # i, j = 0, 0
        # temp = []
        # while j < len(s) and i < len(s):
        #     if s[i].isalpha():
        #         if str != []:
        #             temp.append(str)
        #         while s[i].isalpha():
        #             temp.append(s[i])
        #             i += 1
        #     else:
        #         j = i
        #         i += 1
        #         count = int(s[j])
        #         while count != 0:
        #             str.append(temp)
        #             count -= 1
        #         temp = []
        # return "".join(str)

        size = 0

        # Calculate the size of the decoded string
        for char in s:
            if char.isalpha():
                size += 1
            else:
                size *= int(char)

        # Traverse the string in reverse to find the k-th character
        for char in reversed(s):
            k %= size
            if k == 0 and char.isalpha():
                return char

            if char.isalpha():
                size -= 1
            else:
                size //= int(char)

        return ""


solution = Solution()
res = solution.decodeAtIndex(s="leet2code3", k=10)
print(res)
