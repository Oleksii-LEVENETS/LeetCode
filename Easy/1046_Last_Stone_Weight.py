class Solution:
    def last_stone_weight(self, stones: list[int]) -> int:
        print("stones original: ", stones)
        while len(stones) >= 2:
            stones = sorted(stones)
            print("sorted(stones): ", stones)
            last = stones.pop()
            print("last: ", last)
            pre_last = stones.pop()
            print("pre_last: ", pre_last)
            if (last - pre_last) > 0:
                stones.append(last - pre_last)
                print("stones.append(last - pre_last): ", stones)
        if len(stones) == 1:
            return stones[0]
        return 0


assert Solution().last_stone_weight([2, 7, 4, 1, 8, 1]) == 1
print("OK assertion!")
