import math

# log
# def isPowerofTwo(n):
#     # Your code here
#     x = math.log(n, 2)
#     print(x)
#     if x.is_integer():
#         return True
#     return False

# by bit


def isPowerofTwo(n):
    if (n and (not n & (n-1))):
        return "Power of 2"
    return "Power of not 2"


print(isPowerofTwo(int(input("Enter number :"))))
