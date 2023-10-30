def isAnagram(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    if s == t:
        return True
    if len(s) != len(t):
        return False
    s = list(s)
    t = list(t)
    dict1 = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0,
             'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}
    dict2 = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0,
             'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}
    for i, j in zip(s, t):
        dict1[i] += 1
        dict2[j] += 1
    for key in dict1.keys():
        if dict1[key] != dict2[key]:
            return False
    return True


print(isAnagram('s', 'b'))