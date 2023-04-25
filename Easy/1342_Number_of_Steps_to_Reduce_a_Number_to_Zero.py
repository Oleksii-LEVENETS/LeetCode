class Solution:
    def number_of_steps(self, num: int) -> int:
        if num == 0:
            return 0
        return 1 + self.number_of_steps(num - 1 if num % 2 != 0 else num / 2)
        # result = 0
        # while num > 0:
        #     if num % 2 == 0:
        #         num /= 2
        #         result += 1
        #     else:
        #         num -= 1
        #         result += 1
        #
        # return result


item = Solution()
assert item.number_of_steps(14) == 6
assert item.number_of_steps(8) == 4
assert item.number_of_steps(123) == 12
print("Assertion OK!")
