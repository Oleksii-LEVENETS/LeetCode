class Solution:
    def running_sum(self, nums):
        return [sum(nums[: (i + 1)]) for i in range(len(nums))]


item = Solution()
assert item.running_sum([1, 2, 3, 4]) == [1, 3, 6, 10]
assert item.running_sum([1, 1, 1, 1, 1]) == [1, 2, 3, 4, 5]
assert item.running_sum([3, 1, 2, 10, 1]) == [3, 4, 6, 16, 17]
