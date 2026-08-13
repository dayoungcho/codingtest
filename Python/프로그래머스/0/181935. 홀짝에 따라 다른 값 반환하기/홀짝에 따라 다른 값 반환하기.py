def solution(n):
    answer = 0
    if n%2==1:
        answer = sum(range(1,n+1,2))
    else:
        lst = []
        for i in range(2,n+1,2):
            answer += i**2
    return answer