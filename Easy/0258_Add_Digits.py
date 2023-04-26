"""
2023-04-26

258. Add Digits
Easy, Acceptance Rate 64.9%

Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.

Example 1:
Input: num = 38
Output: 2
Explanation: The process is
38 --> 3 + 8 --> 11
11 --> 1 + 1 --> 2
Since 2 has only one digit, return it.

Example 2:
Input: num = 0
Output: 0

Constraints:
0 <= num <= 231 - 1

Follow up: Could you do it without any loop/recursion in O(1) runtime?
"""
# from functools import reduce


# class Solution:
#     def addDigits(self, num: int) -> int:
#         while True:
#             list_ = [int(i) for i in str(num)]
#             if len(list_) == 1:
#                 break
#             num = reduce(lambda x, y: x + y, list_)
#         return list_[0]


class Solution:
    def add_digits(self, num: int) -> int:
        if num % 9 == 0 and num != 0:
            return 9
        return num % 9


assert Solution().add_digits(38) == 2
assert Solution().add_digits(0) == 0
