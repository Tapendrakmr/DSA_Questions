# # Count triplet with sum smaller than a given value
# def TripletLesSum(Arr, val):
#     n = len(Arr)
#     if n < 3:
#         return 0
#     count = 0
#     for i in range(n-2):
#         if (i > 0 and Arr[i+1] == Arr[i]):
#             pass
#             continue
#         else:
#             j = i+1
#             k = n-1
#             while j < k:
#                 if (Arr[i]+Arr[j]+Arr[k] >= val):
#                     k -= 1

#                 else:
#                     count += (k-j)
#                     j += 1
#     print(count)

# # merge 2 sorted arrays


# # def performAction(A1, A2):
# #     n = len(A1)
# #     i, j = 0, 0
# #     while i < n:
# #         if A1[i] > A2[j]:
# #             A1[i], A2[j] = A2[j], A1[j]

# #             A2.sort()
# #         i += 1
# #     for i in range(len(A1)):
# #         print(A1[i], end=' ')
# #     for j in range(len(A2)):
# #         print(A2[j], end=' ')


# def mergeSortArr(Arr1, Arr2):
#     n = len(Arr1)
#     m = len(Arr2)
#     if m == 0 and n == 0:
#         return []
#     if n == 0:
#         return m
#     if m == 0:
#         return n
#     else:

#         i, j = 0, 0
#         while i < n:
#             if Arr1[i] > Arr2[j]:
#                 Arr1[i], Arr2[j] = Arr2[j], Arr1[i]

#                 Arr2.sort()
#             i += 1
#         for i in range(len(Arr1)):
#             print(Arr1[i], end=' ')
#         print()
#         for j in range(len(Arr2)):
#             print(Arr2[j], end=' ')


# def solution(N):
#     x, i = 0, 0
#     while x < N:
#         x = i*i
#         if x < N:

#             i += 1
#         print(i, x)
#     print(i)


# print("Arr1")
# Arr1 = [int(x) for x in input().split()]
# Arr2 = [int(x) for x in input().split()]
# mergeSortArr(Arr1, Arr2)
# # print("Enter array values with space :")
# # Arr = [int(x) for x in input().split(' ')]
# # val = int(input("Enter Sum value"))
# # TripletLesSum(Arr, val)

N = int(input())
Arr = [int(x) for x in input().split(' ')]
Arr.sort()
print(Arr)
q = int(input())
power = 0
for _ in range(q):
    power = int(input())
    j = 0
    count, sum = 0, 0

    while (Arr[j] <= power and j < N):
        count += 1
        sum += Arr[j]
        j += 1
    print(count, sum)
