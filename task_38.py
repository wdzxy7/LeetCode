def countAndSay(self, n):
    s = '1'
    for i in range(n - 1):
        count = 0
        word = s[0]
        new_s = ''
        for j in s:
            if j == word:
                count += 1
            else:
                new_s += str(count) + word
                word = j
                count = 1
        new_s += str(count) + word
        s = new_s
    return s

print(countAndSay(None, 4))