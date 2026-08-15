def solution(n):
    list_3 = []
    while n > 0:
        list_3.append(n % 3)
        n = n // 3
    rev_3 = ''.join(map(str, list_3))
    ans = int(rev_3,3)
    return ans
