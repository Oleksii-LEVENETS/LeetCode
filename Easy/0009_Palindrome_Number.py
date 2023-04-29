"""
2023-04-29

9. Palindrome Number
Easy, Acceptance Rate 53.6%

Given an integer x, return true if x is a palindrome, and false otherwise.

Example 1:
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

Example 2:
Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:
Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.


Constraints:
-231 <= x <= 231 - 1
Follow up: Could you solve it without converting the integer to a string?

"""


class Solution:
    def is_palindrome(self, x: int) -> bool:
        start_x = x
        reversed_x = 0
        while x > 0:
            reversed_x = (reversed_x * 10) + (x % 10)
            x = x // 10
        return start_x == reversed_x


assert Solution().is_palindrome(1221) is True
assert Solution().is_palindrome(5234) is False
assert Solution().is_palindrome(212) is True
assert Solution().is_palindrome(-121) is False
assert Solution().is_palindrome(10) is False
assert Solution().is_palindrome(1) is True
print("OK assertion!")
