deep_list = [1, [2, [3, [4, [5, 5.1]]], 6], 7]


def flat_list(d_list):
    f_list = []
    for element in d_list:
        if not isinstance(element, list):
            f_list.append(element)
        else:
            f_list.extend(flat_list(element))
    return f_list


print(flat_list(deep_list))

assert flat_list([1, [2, [3, [4, 5]], 6], 7]) == [1, 2, 3, 4, 5, 6, 7]
print("OK assertion!")
