def solution(X, Y, m, n):
    L = [[None]*(n+1) for i in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif X[i-1] == Y[j-1]:
                L[i][j] = L[i-1][j-1]+1
            else:
                L[i][j] = max(L[i-1][j], L[i][j-1])
    return L[m][n]


print("Enter Strings")
X = input("Enter String1 :")
Y = input("Enter String2 :")
print(solution(X, Y, len(X), len(Y)))
