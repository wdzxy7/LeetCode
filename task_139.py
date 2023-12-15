def wordBreak(self, s, wordDict):
    ss = set(wordDict)
    n = len(s)
    f = [False] * (n + 10)
    f[0] = True
    for i in range(1, n + 1):
        j = i
        while j >= 1 and not f[i]:
            sub = s[j - 1:i]
            if sub in ss:
                f[i] = f[j - 1]
            j -= 1
    return f[n]

print(wordBreak(None, "catsandog", ["cats", "dog", "sand", "and", "cat", "san"]))