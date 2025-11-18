def solution(array, n):
    answer = 0
    for i in array:
        if i==int(n):
            answer += 1
    return answer