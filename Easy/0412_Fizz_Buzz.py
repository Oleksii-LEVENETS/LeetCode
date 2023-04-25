class Solution:
    def fizz_buzz(self, n: int) -> list[str]:
        result = []
        for x in range(1, n + 1):
            if x % 15 == 0:
                result.append("FizzBuzz")
            elif x % 3 == 0:
                result.append("Fizz")
            elif x % 5 == 0:
                result.append("Buzz")
            else:
                result.append(str(x))

        return result


res = Solution()

assert res.fizz_buzz(n=3) == ["1", "2", "Fizz"]
assert res.fizz_buzz(5) == ["1", "2", "Fizz", "4", "Buzz"]
assert res.fizz_buzz(15) == [
    "1",
    "2",
    "Fizz",
    "4",
    "Buzz",
    "Fizz",
    "7",
    "8",
    "Fizz",
    "Buzz",
    "11",
    "Fizz",
    "13",
    "14",
    "FizzBuzz",
]

print("Assertion OK!")
