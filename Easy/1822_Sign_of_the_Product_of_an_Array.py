"""
2023-05-02

1822. Sign of the Product of an Array
Easy, Acceptance Rate 66.0%

There is a function signFunc(x) that returns:

1 if x is positive.
-1 if x is negative.
0 if x is equal to 0.
You are given an integer array nums. Let product be the product of all values in the array nums.

Return signFunc(product).



Example 1:

Input: nums = [-1,-2,-3,-4,3,2,1]
Output: 1
Explanation: The product of all values in the array is 144, and signFunc(144) = 1

Example 2:
Input: nums = [1,5,0,2,-3]
Output: 0
Explanation: The product of all values in the array is 0, and signFunc(0) = 0

Example 3:
Input: nums = [-1,1,-1,1,-1]
Output: -1
Explanation: The product of all values in the array is -1, and signFunc(-1) = -1


Constraints:

1 <= nums.length <= 1000
-100 <= nums[i] <= 100
Accepted
207.4K
Submissions
314.4K
Acceptance Rate 66.0%

"""
# from functools import reduce


# class Solution:
#     def array_sign(self, nums: list[int]) -> int:
#         if 0 in nums:
#             return 0
#         return 1 if reduce(lambda x, y: x * y, nums) > 0 else -1


class Solution:
    def array_sign(self, nums: list[int]) -> int:
        res = 1
        for num in nums:
            if num == 0:
                return 0
            if num < 0:
                res = -1 * res
        return res


assert Solution().array_sign([-1, -2, -3, -4, 3, 2, 1]) == 1
assert Solution().array_sign([1, 5, 0, 2, -3]) == 0
assert Solution().array_sign([-1, 1, -1, 1, -1]) == -1
print("OK assertion!")
