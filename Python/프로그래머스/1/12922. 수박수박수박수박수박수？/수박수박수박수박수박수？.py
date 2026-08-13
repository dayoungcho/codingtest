def solution(n):
    even = '수'
    odd = '박'
    answer = ''
    for i in range(n):
        if i % 2 == 0:
            answer += even
        else:
            answer += odd
    return answer