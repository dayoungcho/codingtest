def solution(n):
    cand = n + 1
    while True:
        if bin(n)[2:].count('1') == bin(cand)[2:].count('1'):
            return cand
        cand += 1
        