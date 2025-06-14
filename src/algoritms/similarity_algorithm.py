

# Similar to LeetCode #72 Bottom up approach
def find_similarities(word1, word2):
    """
    Finds similarities between dataset columns
    """
    dp = [[0 for _ in range(len(word2) + 1)] for _ in range(len(word1) + 1)]
  
    # Word1
    for i in range(len(word1) + 1): # 0-5
        dp[i][len(word2)] = len(word1) - i 
    
    # Word2
    for j in range(len(word2) + 1):
        dp[len(word1)][j] = len(word2) - j

    for i in range(len(word1) -1, -1, -1):
        for j in range(len(word2) -1, -1, -1):
            if word1[i] == word2[j]:
                dp[i][j] = dp[i+1][j+1] 
                
            else: 
                dp[i][j] = min(dp[i+1][j], dp[i][j+1], dp[i+1][j+1]) + 1
    return dp[0][0]