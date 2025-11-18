def solution(n):
    if n%2==1:
        answer = sum(range(1,n+1,2))
    else:
        lst = []
        for i in range(2,n+1,2):
            lst.append(i**2)
        answer = sum(lst)
    return answer