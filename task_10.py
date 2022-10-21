def isMatch(self, s, p):
    s = list(s)
    p = list(p)
    index_p = len(p) - 1
    i = len(s) - 1
    front_char = ''
    back_char = ''
    star_use = False
    while i >= 0:
        print(p[index_p], s[i])
        if p[index_p] != '.' and p[index_p] != '*':
            if p[index_p] != s[i]:
                return False
            else:
                index_p -= 1
        elif p[index_p] == '.':
            index_p -= 1
        elif p[index_p] == '*':
            if star_use:
                if front_char == '.':
                    # 出现不同字符.结束
                    if s[i] != back_char:
                        if index_p - 2 >= 0:
                            index_p -= 2
                            star_use = False
                            continue
                        elif index_p - 2 < 0:
                            return False
                        if i == 0 and index_p - 2 < 0:
                            return True
                else:
                    if s[i] != front_char:
                        if index_p - 2 >= 0:
                            index_p -= 2
                            star_use = False
                            continue
                        elif index_p - 2 < 0:
                            return False
                    else:
                        if i == 0 and index_p - 2 < 0:
                            return True
            else:
                if p[index_p - 1] != '.':
                    if p[index_p - 1] != s[i]:
                        return False
                star_use = True
                front_char = p[index_p - 1]
                back_char = s[i]
        i -= 1
    if index_p == -1 and i == -1:
        return True
    return False

print(isMatch(None, 'aa', 'a*'))
print(isMatch(None, 'mississippi', 'mis*is*p*.'))