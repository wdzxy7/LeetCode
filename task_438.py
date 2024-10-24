from collections import Counter


def findAnagrams(self, s: str, p: str):
    s = list(s)
    res = []
    front = 0
    back = len(p)
    base = Counter(p)
    search = Counter(s[front:back])
    while back <= len(s):
        if search == base:
            res.append(front)
        search[s[front]] -= 1
        front += 1
        back += 1
        if back <= len(s):
            search[s[back - 1]] += 1
            if search[s[front - 1]] == 0:
                del search[s[front - 1]]
    return res


print(findAnagrams(None, 'cbaebabacd', 'abc'))