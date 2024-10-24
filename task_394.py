def decodeString(self, s: str) -> str:
    words = []
    nums = []
    t_word = ''
    t_num = 0
    res = ''
    for i in range(len(s)):
        if '0' <= s[i] <= '9':
            t_num = t_num * 10 + int(s[i])
        elif 'a' <= s[i] <= 'z':
            t_word += s[i]
        elif s[i] == '[':
            if t_word != '':
                words.append(t_word)
                t_word = ''
            if t_num != 0:
                nums.append(t_num)
                t_num = 0
        else:
            words.append(t_word)
            t_word = ''
            num = nums.pop()
            word = words.pop()
            res += word
            for j in range(num - 1):
                res += res
            if len(words) > 0:
                t = words.pop()
                t += word
                words.append(t)
            else:
                words.append(word)
    print()


print(decodeString(None, '2[abc]3[cd]ef'))