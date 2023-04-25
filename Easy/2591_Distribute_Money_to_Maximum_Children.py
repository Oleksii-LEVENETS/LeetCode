"""
2023-04-25

2591. Distribute Money to Maximum Children
Easy, 18.4% acceptance

You are given an integer money denoting the amount of money (in dollars) that you have and another
integer children denoting the number of children that you must distribute the money to.

You have to distribute the money according to the following rules:
    - All money must be distributed.
    - Everyone must receive at least 1 dollar.
    - Nobody receives 4 dollars.
    - Return the maximum number of children who may receive exactly 8 dollars if you distribute the money
      according to the aforementioned rules. If there is no way to distribute the money, return -1.

Example 1:
Input: money = 20, children = 3
Output: 1
Explanation:
The maximum number of children with 8 dollars will be 1. One of the ways to distribute the money is:
- 8 dollars to the first child.
- 9 dollars to the second child.
- 3 dollars to the third child.
It can be proven that no distribution exists such that number of children getting 8 dollars is greater than 1.

Example 2:
Input: money = 16, children = 2
Output: 2
Explanation: Each child can be given 8 dollars.

Constraints:
1 <= money <= 200
2 <= children <= 30
"""


class Solution:
    def dist_money(self, money: int, children: int) -> int:
        if money / children == 8:
            return children
        if money < children:
            return -1
        counter = 0
        while money > 0 and children > 1:
            if money < (8 + (children - 1)):
                break
            counter += 1
            children -= 1
            money -= 8
            if money == 4 and children == 1:
                counter -= 1
                break
        return counter


assert Solution().dist_money(16, 2) == 2
print("Assert #1 OK!")
assert Solution().dist_money(20, 3) == 1
print("Assert #2 OK!")
assert Solution().dist_money(2, 2) == 0
print("Assert #3 OK!")
assert Solution().dist_money(3, 4) == -1
print("Assert #4 OK!")
