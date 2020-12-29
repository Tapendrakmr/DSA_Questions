def Solution(Arr, K):
    if len(Arr) < 0:
        return 0
    Arr.sort()

    ans = Arr[-1]-Arr[0]
    small = Arr[0]+K
    big = Arr[-1]-K
    if small > big:
        small, big = big, small
    for i in range(1, len(Arr)):
        subtract = Arr[i]-K
        add = Arr[i]+K

        if (subtract >= small or add < big):
            continue

        if (big-subtract <= add-small):
            small = subtract
        else:
            big = add
    return min(ans, big-small)


Arr = [int(x) for x in input().split(' ')]
K = int(input('Enter K value :'))
print(Solution(Arr, K))
