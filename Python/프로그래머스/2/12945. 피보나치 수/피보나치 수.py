def fibonacci(n):
    a = 1
    b = 1
    if n == 1 or n == 2:
        return 1
    for i in range(n-1):
        a, b = b, b + a
    return a

def solution(n):
    answer = fibonacci(n) % 1234567
    return answer