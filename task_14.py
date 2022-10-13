def longestCommonPrefix(self, strs):
    length = len(strs)
    if length == 1:
        return strs[0]
    for i in range(length):
        strs[i] = list(strs[i])
    res = ''
    for i in range(len(strs[0])):
        for j in range(1, length):
            try:
                if strs[j][i] != strs[0][i]:
                    return res
            except:
                return res
        res += strs[0][i]
    return res


print(longestCommonPrefix(None, ["dog", 'd']))