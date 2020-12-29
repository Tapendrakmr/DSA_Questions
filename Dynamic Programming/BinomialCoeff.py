# Coefficent C(n,k)=C(n-1,k-1)+C(n-1,k)
# Recursive approach


# def BinomialCoefficent(n, k):
#     if k > n:
#         return 0
#     if k == n or k == 0:
#         return 1
#     return BinomialCoefficent(n-1, k-1)+BinomialCoefficent(n-1, k)


# Dynamic

# def BinomialCoefficent(n, k):
#     dp = [[0 for i in range(k+1)] for j in range(n+1)]
#     for i in range(n+1):
#         for j in range(min(i, k)+1):
#             if j == 0 or j == i:
#                 dp[i][j] = 1
#             else:
#                 dp[i][j] = dp[i-1][j-1]+dp[i-1][j]
#     print(dp)
#     return dp[n][k]

# Optimised

def BinomialCoefficent(n, k):
    C = [0 for i in range(k+1)]
    C[0] = 1
    for i in range(1, n+1):
        j = min(k, i)
        while j > 0:
            C[j] = C[j]+C[j-1]
            j -= 1
        print(C)
    return C[k]


n = int(input("Enter n value :"))
k = int(input("Enter k value :"))
print(BinomialCoefficent(n, k))
