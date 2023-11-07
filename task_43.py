def multiply(self, num1, num2):
    num_dict = {
        '0': 0,
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
    }
    num_dict2 = {
        0: '0',
        1: '1',
        2: '2',
        3: '3',
        4: '4',
        5: '5',
        6: '6',
        7: '7',
        8: '8',
        9: '9',
    }
    num1 = list(num1)
    num2 = list(num2)
    Num1 = 0
    for i in range(len(num1)):
        Num1 = Num1 * 10 + num_dict[num1[i]]
    Num2 = 0
    for i in range(len(num2)):
        Num2 = Num2 * 10 + num_dict[num2[i]]
    res = Num1 * Num2
    if res == 0:
        return '0'
    res_str = ''
    while res > 0:
        num = res % 10
        res = res // 10
        res_str = num_dict2[num] + res_str
    return res_str
print(multiply(None, '2', '3'))