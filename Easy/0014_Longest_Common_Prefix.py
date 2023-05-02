"""
2023-05-02

14. Longest Common Prefix
Easy, Acceptance Rate 40.9%

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".


Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.


Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.

"""


# class Solution:
#     def longest_common_prefix(self, strs: list[str]) -> str:
#         res = []
#
#         for index in range(len(strs[0])):
#             print("strs[0]: ", strs[0])
#             count = 0
#             for i in range(len(strs)):
#                 print("i: ", i)
#                 try:
#                     print("letter: ", strs[0][index])
#                     print("strs[i]: ", strs[i])
#                     if strs[0][index] == strs[i][index]:
#                         count += 1
#                         print("count: ", count)
#                 except:
#                     continue
#
#             if count == len(strs):
#                 res.append(strs[0][index])
#             else:
#                 break
#         print("res: ", res)
#         print("#"*50)
#
#         return "".join(res)


class Solution:
    def longest_common_prefix(self, strs: list[str]) -> str:
        res = ""
        strs = sorted(strs)
        first = strs[0]
        last = strs[-1]
        for i in range(min(len(first), len(last))):
            if first[i] != last[i]:
                return res
            res += first[i]
        return res


assert Solution().longest_common_prefix(["flower", "flow", "flight"]) == "fl"
assert Solution().longest_common_prefix(["dog", "racecar", "car"]) == ""
assert Solution().longest_common_prefix(["cir", "car"]) == "c"
assert Solution().longest_common_prefix(["c", "c"]) == "c"
assert Solution().longest_common_prefix(["aa", "ab"]) == "a"
assert Solution().longest_common_prefix(["a", "a", "a"]) == "a"
print("OK assertion!")
