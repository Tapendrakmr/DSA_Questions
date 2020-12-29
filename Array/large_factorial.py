def large_fact(n):
    res = [None]*500
    res[0] = 1
    res_size = 1
    x = 2
    while x <= n:
        res_size = multiple(x, res, res_size)
        x += 1
    i = res_size-1
    while i >= 0:
        print(res[i], end='')
        i -= 1


def multiple(x, res, res_size):
    carry = 0
    i = 0
    while i < res_size:
        prod = res[i]*x+carry
        res[i] = prod % 10
        carry = prod//10
        i = i+1
    while (carry):
        res[res_size] = carry % 10
        carry = carry//10
        res_size = res_size+1
    return res_size


n = int(input("Enter number"))
large_fact(n)
