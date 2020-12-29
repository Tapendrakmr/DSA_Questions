No_OF_Chars = 256


def solution(Strng):
    count = [0]*No_OF_Chars
    count = findCount(count, Strng)
    k = 0
    for i in count:
        if int(i) > 1:
            print(chr(k) + ", count ="+str(i))
        k += 1


def findCount(count, Strng):
    for i in Strng:
        count[ord(i)] += 1
    return count


x = input("Enter String :")
print(solution(x))
