def flipBit(n):
    count = 0
    while n:
        count += n & 1
        n >>= 1
    print(count)


x = int(input("First no. :"))
y = int(input("Second no. :"))
flipBit(x ^ y)
