def findRepeatedDnaSequences(self, s):
    search_dict = {}
    res = set()
    for i in range(10, len(s) + 1):
        try:
            search_dict[s[i - 10:i]] += 1
            res.add(s[i - 10:i])
        except:
            search_dict[s[i - 10:i]] = 1
    return list(res)

print(findRepeatedDnaSequences(None, "AAAAAAAAAAA"))