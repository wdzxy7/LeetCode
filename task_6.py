def convert(self, s, numRows):
    if numRows == 1:
        return s
    l = len(s)
    res_list = []
    k = 0
    back = 0
    search_index = []
    # 改值是否处理过
    string_dict = {}
    for i in range(l):
        string_dict[i] = 0
    while k < l:
        res_list.append(s[k])
        string_dict[k] = 1
        search_index.append(k)
        k += (numRows - 1) * 2
        back += 1
    if k >= l:
        search_index.append(k)
    l_res = back
    while l_res != l:
        # 存储这一排的长度
        t_len = 0
        t_search_index = []
        for i in search_index:
            left = i - 1
            down = i + 1
            if (left > 0) and (left < l):
                if string_dict[left] != 1:
                    string_dict[left] = 1
                    res_list.append(s[left])
                    l_res += 1
                    t_len += 1
                    t_search_index.append(left)
            elif left >= l:
                t_search_index.append(left)
            if down < l:
                if string_dict[down] != 1:
                    string_dict[down] = 1
                    res_list.append(s[down])
                    l_res += 1
                    t_len += 1
                    t_search_index.append(down)
        # 移动到下一排
        search_index = t_search_index
    return ''.join(res_list)


print(convert(None, 'ABCDE', 3))