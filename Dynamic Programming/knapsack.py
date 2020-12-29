# Recursive approach
# def knapsack(W, wt, val, n):
#     if n == 0 or W == 0:
#         return 0
#     if wt[n-1] > W:
#         return knapsack(W, wt, val, n-1)
#     else:
#         return max(val[n-1]+knapsack(W-wt[n-1], wt, val, n-1), knapsack(W, wt, val, n-1))

# Dynamic


def knapsack(W, wt, val, n):
    dp = [[0 for x in range(W+1)] for x in range(n+1)]
    for i in range(n+1):
        for w in range(W+1):
            if i == 0 or w == 0:
                dp[i][w] = 0
            elif wt[i-1] <= w:
                dp[i][w] = max(val[i-1]+dp[i-1][w-wt[i-1]], dp[i-1][w])
            else:
                dp[i][w] = dp[i-1][w]
    return dp[n][w]


n = int(input("Number of quantity :"))

print("Take weight :")
wt = [int(x) for x in input().split(' ')]

print("Take values :")
val = [int(x) for x in input().split(' ')]

W = int(input("Enter Weight amount :"))

print(knapsack(W, wt, val, n))
