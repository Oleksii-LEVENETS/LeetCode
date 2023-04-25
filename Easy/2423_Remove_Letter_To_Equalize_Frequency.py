from collections import Counter


class Solution:
    def equal_frequency(self, word: str) -> bool:
        word = list(word)
        print("word list: ", word)
        for letter in word:
            word_test = word[:]
            word_test.remove(letter)
            print("word_test remove: ", word_test)
            count_word = dict(Counter(word_test))
            print("count_word: ", count_word)
            set_value = set(count_word.values())
            print("set_value: ", set_value)
            if len(set_value) == 1:
                return True

        return False


# class Solution:
#     def equalFrequency(self, word: str) -> bool:
#         word = list(word)
#         print("word list: ", word)
#         for letter in word:
#             word_test = word[:]
#             word_test.remove(letter)
#             print("word_test remove: ", word_test)
#             # count_word = dict(Counter(word_test))
#             # print("count_word: ", count_word)
#             set_value = set(Counter(word_test).values())
#             print("set_value: ", set_value)
#             if len(set_value) == 1:
#                 return True
#
#         return False


assert Solution().equal_frequency("abcc") is True
assert Solution().equal_frequency("aazz") is False
