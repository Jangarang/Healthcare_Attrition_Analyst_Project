# Similar to Longest Common Subsequence
def LCS(text1, text2):
    """
    """
    dp = [[0 for _ in range(len(text2) +1)] for _ in range(len(text1) + 1)]

    for i in range(len(text1) + 1):
        dp[i][len(text2)] = 0
    
    for j in range(len(text2) + 1):
        dp[len(text1)][j] = 0

    print(dp)

    for i in range(len(text1) -1, -1, -1):
        for j in range(len(text2) -1, -1, -1):
            if (text1[i] == text2[j]):
                dp[i][j] += 1 + dp[i + 1][j + 1]
            else: 
                dp[i][j] = max(dp[i+1][j], dp[i][j+1])
    return dp[0][0]