def solution(a, b, c):
    bool_result = (a==b) + (a==c) + (b==c)
    answer = a+b+c
    if bool_result >= 1:
        answer = answer*(a**2+b**2+c**2)
    if bool_result == 3:
        answer = answer*(a**3+b**3+c**3)
    return answer