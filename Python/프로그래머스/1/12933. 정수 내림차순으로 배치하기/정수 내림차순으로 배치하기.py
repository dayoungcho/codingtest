def solution(n):
    n = sorted(list(map(int, list(str(n)))), reverse=True)
    answer = ''.join(list(map(str, n)))
    return int(answer)