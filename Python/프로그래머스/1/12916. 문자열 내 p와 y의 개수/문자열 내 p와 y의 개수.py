def solution(s):
    s = s.lower()
    n_p = 0
    n_y = 0
    for i in s:
        if i == 'p':
            n_p += 1
        if i == 'y':
            n_y += 1
    return n_p == n_y