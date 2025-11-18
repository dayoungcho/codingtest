def solution(ineq, eq, n, m):
    answer = 0
    if ineq == "<":
        if eq == "=":
            answer = int(n <= m)
        else:
            answer = int(n<m)
    else:
        if eq == "=":
            answer = int(n>=m)
        else:
            answer = int(n>m)
    return answer