def groupAnagrams(self, strs):
    sort_str = [''.join(sorted(i)) for i in strs]
    str_dict = {}
    for i in range(len(sort_str)):
        try:
            str_dict[sort_str[i]].append(strs[i])
        except:
            str_dict[sort_str[i]] = [strs[i]]
    res = []
    for key in str_dict.keys():
        res.append(str_dict[key])
    return res

print(groupAnagrams(None, ["a"]))