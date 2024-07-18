def isInterleave(self, s1, s2, s3):
    len_s1 = len(s1)
    len_s2 = len(s2)
    len_s3 = len(s3)
    if len_s1 + len_s2 != len_s3:
        return False
    dp = [[False] * (len_s2 + 1) for i in range(len_s1 + 1)]
    dp[0][0] = True
    for i in range(1, len_s2 + 1):
        dp[0][i] = s2[:i] == s3[:i]
    for j in range(1, len_s1 + 1):
        dp[j][0] = s1[:j] == s3[:j]
    for i in range(1, len_s1 + 1):
        for j in range(1, len_s2 + 1):
            index = i + j - 1
            dp[i][j] = (dp[i - 1][j] and s1[i - 1] == s3[index]) or (dp[i][j - 1] and s2[j - 1] == s3[index])
    return dp[-1][-1]


print(isInterleave(None, "aabcc", "dbbca", "aadbbcbcac"))