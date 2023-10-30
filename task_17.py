def letterCombinations(self, digits):
    num_dict = {
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z']
    }
    digits = list(digits)
    try:
        res_list = num_dict[digits[0]]
        del digits[0]
    except:
        return []
    for num in digits:
        new_list = []
        num_str = num_dict[num]
        for s in res_list:
            for n_s in num_str:
                new_list.append(s + n_s)
        res_list = new_list.copy()
    return res_list

print(letterCombinations(None, '23'))