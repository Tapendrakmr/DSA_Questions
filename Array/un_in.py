def union(Arr1, Arr2):
    i, j = 0, 0

    while i < len(Arr1) and j < len(Arr2):
        if Arr1[i] < Arr2[j]:
            print(Arr1[i], end='')
            i += 1
        elif Arr2[j] < Arr1[i]:
            print(Arr2[j], end='')
            j += 1
        else:
            print(Arr1[i], end='')

            i += 1
            j += 1
    while i < len(Arr1):
        print(Arr1[i], end=' ')
        i += 1
    while j < len(Arr2):
        print(Arr2[j], end=' ')
        j += 1


def intersection(Arr1, Arr2):
    i, j = 0, 0
    while i < len(Arr1) and j < len(Arr2):
        if Arr1[i] < Arr2[j]:
            i += 1
        elif Arr2[j] < Arr1[i]:
            j += 1
        else:
            print(Arr1[i])
            i += 1
            j += 1


Arr1 = [int(x) for x in input().split(' ')]
Arr2 = [int(x) for x in input().split(' ')]
union(Arr1, Arr2)
intersection(Arr1, Arr2)
