"""
2023-04-27

319. Bulb Switcher
Medium, Acceptance Rate 50.4%

There are n bulbs that are initially off. You first turn on all the bulbs, then you turn off every second bulb.
On the third round, you toggle every third bulb (turning on if it's off or turning off if it's on).
For the i-th round, you toggle every i bulb. For the n-th round, you only toggle the last bulb.
Return the number of bulbs that are ON after n rounds.

Example 1:
Input: n = 3
Output: 1
Explanation: At first, the three bulbs are [off, off, off].
After the first round, the three bulbs are [on, on, on].
After the second round, the three bulbs are [on, off, on].
After the third round, the three bulbs are [on, off, off].
So you should return 1 because there is only one bulb is on.

Example 2:
Input: n = 0
Output: 0

Example 3:
Input: n = 1
Output: 1


Constraints:
0 <= n <= 109

"""
from math import sqrt


# class Solution:
#     def bulb_switch(self, n: int) -> int:
#         if n == 0:
#             return 0
#         elif n == 1:
#             return 1
#
#         # 0 -- off, 1 -- on
#         list_bulb = [1 for i in range(n)]  # 1 -- turn on all the bulbs
#         print("len(list_bulb): ", len(list_bulb))
#         print("#1 - turn on all the bulbs.  list_bulb: ", list_bulb)
#
#         for index_bulb in range(1, n, 2):
#             list_bulb[index_bulb] = 0  # 2 -- turn on every second bulb
#         print("#2 - turn off every second bulb. list_bulb: ", list_bulb)
#
#         for iteration in range(3, n+1):
#             for index_bulb in range(2, len(list_bulb)):
#                 if (index_bulb + 1) % iteration == 0 and iteration != n:
#                     current = list_bulb[index_bulb]
#                     list_bulb[index_bulb] = 0 if current == 1 else 1
#                     print(f"#{iteration} toggle every {iteration} bulb. list_bulb:: ", list_bulb)
#
#             if iteration == n:
#                 last = list_bulb[-1]
#                 list_bulb[-1] = 0 if last == 1 else 1
#
#         print(f"#{iteration} -- end - toggle only last bulb. list_bulb: ", list_bulb)
#         print(f"#{iteration} list_bulb.count(1):  ", list_bulb.count(1))
#         return list_bulb.count(1)


class Solution:
    def bulb_switch(self, n: int) -> int:
        return int(sqrt(n))


assert Solution().bulb_switch(6) == 2
assert Solution().bulb_switch(5) == 2
assert Solution().bulb_switch(4) == 2
assert Solution().bulb_switch(3) == 1
assert Solution().bulb_switch(0) == 0
assert Solution().bulb_switch(1) == 1
print("OK assertions!")
