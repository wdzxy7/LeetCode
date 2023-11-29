def minDistance(self, word1, word2):
    len_word1 = len(word1) + 1
    len_word2 = len(word2) + 1
    dp = [[0] * len_word2 for i in range(len_word1)]
    dp[0] = [i for i in range(len_word2)]
    for i in range(len_word1):
        dp[i][0] = i
    for i in range(1, len_word1):
        for j in range(1, len_word2):
            if word1[i - 1] != word2[j - 1]:
                dp[i][j] = 1 + min([dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]])
            else:
                dp[i][j] = 1 + min([dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1] - 1])
    return dp[len_word1 - 1][len_word2 - 1]

print(minDistance(None, "horse", "ros"))