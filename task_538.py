def minDistance(self, word1, word2):
    dp = [[0 for i in range(len(word1) + 1)] for i in  range(len(word2) + 1)]
    dp[0][0] = 0
    for i in range(1, len(word2) + 1):
        for j in range(1, len(word1) + 1):
            if word2[i - 1] == word1[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
    return len(word1) - dp[-1][-1] + len(word2) - dp[-1][-1]

print(minDistance(None, 'sea', 'eat'))