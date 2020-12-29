def solve(arr):
    sums = arr[0]
    for i in range(1, len(arr)):
        print(sums)
        sums ^= arr[i]
    print(sums)
    sums = (sums & -sums)
    print("2's complement ", sums)
    sum1 = 0
    sum2 = 0
    for i in range(len(arr)):
        if (arr[i] & sums) > 0:

            sum1 ^= arr[i]
            print("sum1", sum1)
        else:

            sum2 ^= arr[i]
            print("sum2", sum2)
    print("sum1 :", sum1, " Sum2 :", sum2)


arr = [int(x) for x in input().split(' ')]

solve(arr)
