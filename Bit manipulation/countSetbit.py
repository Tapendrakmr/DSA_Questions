def countbit(n):
    count = 0
    while n:
        print('binary', bin(n))
        print(n & 1)
        count += n & 1
        n >>= 1
    print("result", count)
    return count


n = int(input())
countbit(n)
