"""
2023-04-26

1. Two Sum
Easy, Acceptance Rate 49.8%

Given an array of integers nums and an integer target, return indices of the two numbers such that
they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]

Constraints:
2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.

Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
"""


class Solution:
    def two_sum(self, nums: list[int], target: int) -> list[int]:
        dict_nums = {}
        for i in range(len(nums)):
            second = target - nums[i]
            if second in dict_nums:
                return [dict_nums[second], i]
            dict_nums[nums[i]] = i
        return None


assert Solution().two_sum([2, 7, 11, 15], 9) == [0, 1]
assert Solution().two_sum([3, 2, 4], 6) == [1, 2]
assert Solution().two_sum([3, 3], 6) == [0, 1]
print("OK assertion!")
