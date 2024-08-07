def lengthOfLongestSubstring(self, s):
    hash_dict = {}
    front_ind = 0
    max_len = 0
    t_len = 0
    i = 0
    while i < len(s):
        # 出现重复字符
        try:
            ind = hash_dict[s[i]]
            if ind < front_ind:
                hash_dict[s[i]] = i
                i += 1
                t_len += 1
                continue
            if t_len > max_len:
                max_len = t_len
            t_len = i - ind
            front_ind = ind
            hash_dict[s[i]] = i
            i += 1
        # 没有重复字符
        except:
            hash_dict[s[i]] = i
            t_len += 1
            i += 1
    if t_len > max_len:
        max_len = t_len
    return max_len


def lengthOfLongestSubstring2(self, s):
    window = []
    max_len = 0
    t_len = 0
    for i in range(len(s)):
        if s[i] in window:
            max_len = max(t_len, max_len)
            while len(window) > 0:
                t = window[0]
                t_len -= 1
                del window[0]
                if t == s[i]:
                    break
        t_len += 1
        window.append(s[i])
    return max(max_len, t_len)


print(lengthOfLongestSubstring2(None, 'bbtablud'))