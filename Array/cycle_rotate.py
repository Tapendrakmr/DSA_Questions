def solution(Arr):
    if len(Arr) == 1:
        return Arr
    temp1 = Arr[0]
    last = Arr[-1]
    for i in range(1, len(Arr)):
        temp2 = Arr[i]
        Arr[i] = temp1
        temp1 = temp2
    Arr[0] = last
    return Arr


arr = [int(x) for x in input().split(' ')]
print(solution(arr))
