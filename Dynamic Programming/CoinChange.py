# given some numbers you to count how many way you can use them to make number n
def solution(n):
    if n < 1:
        return 0
    if n == 1:
        return 1
    return (solution(n-1)+solution(n-3)+solution(n-5))


solution(int(input("Enter number :")))
