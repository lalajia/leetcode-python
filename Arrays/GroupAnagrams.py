"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
"""
"""
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
"""

from typing import List


# 用dictionary记录所有字母的出现频率{[1,1,0,0,...0]: ["nat", "tan"], ...} 最后return value
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for str in strs:
            count = [0] * 26
            for char in str:
                count[ord(char) - ord("a")] += 1
            key = tuple(count)  # Convert the list to a tuple to make it hashable
            # print(key)
            if key in res:
                res[key].append(str)
            else:
                res[key] = [str]
            # print(res)
        """
        The res.values() function returns a view object that provides a dynamic view on the values of the dictionary res. While it behaves similar to a list in some ways, it is not actually a list.
        By using list(res.values()), we convert the view object into a list. This ensures that the return value of the groupAnagrams method is a list of lists, where each inner list represents a group of anagrams.
        """
        return list(res.values())


print(Solution().groupAnagrams(strs=["eat", "tea", "tan", "ate", "nat", "bat"]))
