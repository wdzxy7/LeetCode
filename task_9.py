def isPalindrome(self, x):
    x = list(x)
    l = len(x)
    for i in range(0, l):
        j = l - i - 1
        if i >= j:
            break
        if x[i] != x[j]:
            return False
    return True


print(isPalindrome(None, '1'))