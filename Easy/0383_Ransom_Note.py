from collections import Counter


# V-1
class Solution1:
    def can_construct_1(self, ransom_note: str, magazine: str) -> bool:
        ransom_counter = Counter(ransom_note)
        print("ransom_counter: ", ransom_counter)
        magazine_counter = Counter(magazine)
        print("magazine_counter: ", magazine_counter)
        print("ransom_counter & magazine_counter: ", ransom_counter & magazine_counter)
        return ransom_counter == ransom_counter & magazine_counter


# V-2
class Solution2:
    def can_construct_2(self, ransom_note: str, magazine: str) -> bool:
        magazine = list(magazine)
        for letter in ransom_note:
            if letter not in magazine:
                return False
            magazine.remove(letter)
        return True


assert Solution1().can_construct_1("a", "b") is False
assert Solution1().can_construct_1("aa", "aab") is True
assert Solution1().can_construct_1("aaabbbccc", "bbbaaacccvvvsshskjaabbsbdhfk") is True

assert Solution2().can_construct_2("a", "b") is False
assert Solution2().can_construct_2("aa", "aab") is True
assert Solution2().can_construct_2("aaabbbccc", "bbbaaacccvvvsshskjaabbsbdhfk") is True

print("OK assertion!")
