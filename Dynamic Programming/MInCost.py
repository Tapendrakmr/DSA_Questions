def solution(cost, row, col):
    dp = [[0 for i in range(col+1)] for j in range(row + 1)]
    dp[0][0] = cost[0][0]
    for i in range(1, row+1):
        dp[i][0] = cost[i][0]+dp[i-1][0]
    for j in range(1, col + 1):
        dp[0][j] = cost[0][j]+dp[0][j-1]
    for i in range(1, row+1):
        for j in range(1, col + 1):
            dp[i][j] = min(dp[i-1][j], dp[i][j-1],
                           dp[i-1][j-1])+cost[i][j]
    print(dp)
    return dp[row][col]


cost = [[1, 2, 3],
        [4, 8, 2],
        [1, 5, 3]]
print(solution(cost, 2, 2))
