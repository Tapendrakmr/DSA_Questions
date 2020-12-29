def maxSubStr(S, n):
    count0 = 0
    count1 = 0
    cnt = 0
    for i in range(n):
        if S[i] == '0':
            count0 += 1
        else:
            count1 += 1
        if count0 == count1:
            cnt += 1
    if count0 != count1:
        return -1
    return cnt


S = input("Enter String ")
n = len(S)
print(maxSubStr(S, n))
