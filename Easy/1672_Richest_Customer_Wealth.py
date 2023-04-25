class Solution:
    def maximum_wealth(self, accounts: list[list[int]]) -> int:
        return max([sum(i) for i in accounts])


item = Solution()
assert item.maximum_wealth([[1, 2, 3], [3, 2, 1]]) == 6
assert item.maximum_wealth([[1, 5], [7, 3], [3, 5]]) == 10
assert item.maximum_wealth([[2, 8, 7], [7, 1, 3], [1, 9, 5]]) == 17
