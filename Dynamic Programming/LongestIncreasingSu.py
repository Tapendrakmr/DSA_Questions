def solution(arr):
    temp = [1]*len(arr)
    print(temp)
    i = 1
    j = 0
    while i < len(arr):
        if i == j:
            j = 0
            i += 1
        elif arr[j] < arr[i]:
            temp[i] = max(temp[i], temp[j]+1)
            j += 1
        elif arr[j] >= arr[i]:
            j += 1

    print(temp)
    return max(temp)


print("Enter value of array")
arr = [int(x) for x in input().split(' ')]
print(solution(arr))
