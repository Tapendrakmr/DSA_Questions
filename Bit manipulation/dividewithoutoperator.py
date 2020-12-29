def solve(dividend, divisor):
    sign = (-1 if ((dividend) < 0 or divisor < 0)else 1)
    dividend = abs(dividend)
    divisor = abs(divisor)

    quotient = 0
    temp = 0
    for i in range(31, -1, -1):
        if (temp + (divisor << i) <= dividend):
            print("temp before :", temp)
            temp += divisor << i
            quotient |= 1 << i
    return sign*quotient


dividend = int(input("Enter Dividend :"))
divisor = int(input("Enter Divisor :"))

print(solve(dividend, divisor))
