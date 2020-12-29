def check_arr2_subset_arr1(arr1, arr2):
    arr1.sort()  # T(O) nlogn
    arr2.sort()  # T(O) mlogm
    print(arr1, arr2)
    i, j = 0, 0
    cnt = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            i += 1
        elif arr1[i] > arr2[j]:
            j += 1
        elif arr1[i] == arr2[j]:
            cnt += 1
            i += 1
            j += 1
    if cnt == len(arr1) or cnt == len(arr2):
        return "yes"
    return 'No'


arr1 = [int(x) for x in input().split()]
arr2 = [int(x) for x in input().split()]

print(check_arr2_subset_arr1(arr1, arr2))
