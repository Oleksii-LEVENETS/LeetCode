"""
2023-04-28

839. Similar String Groups
Hard, Acceptance Rate 51.4%

Two strings X and Y are similar if we can swap two letters (in different positions) of X,
so that it equals Y. Also two strings X and Y are similar if they are equal.

For example, "tars" and "rats" are similar (swapping at positions 0 and 2), and "rats" and "arts" are similar,
but "star" is not similar to "tars", "rats", or "arts".

Together, these form two connected groups by similarity: {"tars", "rats", "arts"} and {"star"}.
Notice that "tars" and "arts" are in the same group even though they are not similar.
Formally, each group is such that a word is in the group if and only if it is similar to at least one
other word in the group.

We are given a list strs of strings where every string in strs is an anagram of every other string in strs.
How many groups are there?

Example 1:
Input: strs = ["tars","rats","arts","star"]
Output: 2

Example 2:
Input: strs = ["omv","ovm"]
Output: 1


Constraints:
1 <= strs.length <= 300
1 <= strs[i].length <= 300
strs[i] consists of lowercase letters only.
All words in strs have the same length and are anagrams of each other.

"""


class Solution:
    def num_similar_groups(self, strs: list[str]) -> int:
        groups = 0
        n = len(strs)
        vis = [False] * n
        for i in range(n):
            if vis[i]:
                continue
            groups += 1
            self.dfs(i, strs, vis)
        return groups

    def dfs(self, i: int, strs: list[str], vis: list[bool]) -> None:
        vis[i] = True
        for j in range(len(strs)):
            if vis[j]:
                continue
            if self.is_similar(strs[i], strs[j]):
                self.dfs(j, strs, vis)

    def is_similar(self, a: str, b: str) -> bool:
        count = 0
        for i in range(len(a)):
            if a[i] != b[i]:
                count += 1
        return count == 2 or count == 0


# class Solution:
#     def num_similar_groups(self, strs: list[str]) -> int:
#         list_set =[]
#         for word in strs:
#             word_set = {f"{index}{letter}" for index, letter in enumerate(word)}
#             list_set.append(word_set)
#
#         list_groups = [0 for i in range(len(strs))]
#         print("list_groups: ", list_groups)
#         count_list_groups = 0
#         for item_set in list_set:
#             for i in range(len(list_set)):
#                 if len(tuple(item_set | list_set[i])) == len(item_set) + 2:
#                     print(f"{sorted(list(item_set))} and {sorted(list(list_set[i]))}")
#                     count_list_groups += 1
#                     list_groups[i] = count_list_groups
#                     print("list_groups: ", list_groups)
#
#         print('#' * 10)
#         single = list_groups.count(0)
#         print("single: ", single)
#         if max(list_groups) == 0 and len(strs) > 0:
#             return 1
#         return max(list_groups) + single


assert Solution().num_similar_groups(["tars", "rats", "arts", "star"]) == 2
assert Solution().num_similar_groups(["omv", "ovm"]) == 1
assert Solution().num_similar_groups(["blw", "bwl", "wlb"]) == 1
assert Solution().num_similar_groups(["nmiwx", "mniwx", "wminx", "mnixw", "xnmwi"]) == 2
assert Solution().num_similar_groups(["abc", "abc"]) == 1
assert Solution().num_similar_groups(["jvhpg", "jhvpg", "hpvgj", "hvpgj", "vhgjp"]) == 3
print("OK assertion!")
