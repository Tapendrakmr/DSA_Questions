def soltuion(n):
    if n == 0:
        return 0
    x = largetPower2range(n)
    print(x)
    bit = x*(pow(2, (x-1)))
    m = (n-(pow(2, x)+1))
    res = (n-(pow(2, x)))
    ans = bit+m+soltuion(res)
    print(ans)


def largetPower2range(n):
    x = 0
    while (1 << x) <= n:
        x += 1
    return x-1


n = int(input("Enter number limit :"))
soltuion(n)
