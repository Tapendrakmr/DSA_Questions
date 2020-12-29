def solution(Arr):
    left = 0
    right = len(Arr)-1
    while left < right:
        if Arr[left] > 0 and Arr[right] < 0:
            Arr[right], Arr[left] = Arr[left], Arr[right]
            left += 1
            right -= 1
        elif Arr[left] < 0 and Arr[right] < 0:
            left += 1
        elif Arr[right] > 0 and Arr[right] > 0:
            right -= 1
    return Arr


Arr = [int(x) for x in input().split(' ')]
print(solution(Arr))
