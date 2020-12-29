def solution(A, B, C):
    print(A, B)
    res = []
    i, j = 0, 0
    while i < len(A) and j < len(B):
        if A[i] < B[j]:
            i += 1
        elif A[i] > B[j]:
            j += 1
        elif A[i] == B[j]:
            res.append(A[i])
            i += 1
            j += 1
    i, j = 0, 0
    fin = []
    while i < len(res) and j < len(C):
        if res[i] < C[j]:
            i += 1
        elif res[i] > C[j]:
            j += 1
        elif res[i] == C[j]:
            fin.append(res[i])
            i+=1
            j+=1

    print(fin)
    return res


A = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]
C = [int(x) for x in input().split()]

print(solution(A, B, C))
