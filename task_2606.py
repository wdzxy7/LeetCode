def maximumCostSubstring(self, s, chars, vals):
    word_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12,
                 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23,
                 'x': 24, 'y': 25, 'z': 26}
    for c, v in zip(chars, vals):
        word_dict[c] = v
    pre_value = 0
    max_sum = 0
    for i in s:
        pre_value = max(pre_value + word_dict[i], word_dict[i])
        if pre_value > max_sum:
            max_sum = pre_value
    return max_sum

print(maximumCostSubstring(None, 'kqqqqqkkkq', 'kq', [-6,6]))