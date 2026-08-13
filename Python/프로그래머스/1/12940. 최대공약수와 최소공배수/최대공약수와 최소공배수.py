def solution(n, m):
    min_num = 1  # 최대공약수
    max_num = n * m  # 최소공배수
    for i in range(1, n*m+1):
        # 최대공약수
        if i <= min(n,m):
            if n % i == 0 and m % i == 0 and i > min_num:
                min_num = i
        else:
            if i % n == 0 and i % m == 0 and i < max_num:
                max_num = i
    answer = [min_num, max_num]
    return answer