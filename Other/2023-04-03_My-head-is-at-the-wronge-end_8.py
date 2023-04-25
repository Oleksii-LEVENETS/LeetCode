def fix_the_meerkat(arr):
    return arr[::-1]


print('fix_the_meerkat(["bottom", "middle", "top"]):  ', fix_the_meerkat(["bottom", "middle", "top"]))

assert fix_the_meerkat(["tail", "body", "head"]) == ["head", "body", "tail"]
assert fix_the_meerkat(["tails", "body", "heads"]) == ["heads", "body", "tails"]
assert fix_the_meerkat(["bottom", "middle", "top"]) == ["top", "middle", "bottom"]
assert fix_the_meerkat(["lower legs", "torso", "upper legs"]) == ["upper legs", "torso", "lower legs"]
assert fix_the_meerkat(["ground", "rainbow", "sky"]) == ["sky", "rainbow", "ground"]
