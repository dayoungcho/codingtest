T = int(input())  # 테스트 케이스 수

for _ in range(1, T+1):
    N, M = map(int, input().split())  # A의 길이, B의 길이
    arr_a = list(map(int, input().split()))  
    arr_b = list(map(int, input().split()))
    muls = []
    bigger = max(N,M)
    smaller = min(N,M)
    for i in range(bigger-smaller+1):
        mul = 0
        for j in range(smaller):
            if smaller == N:
                mul += arr_a[j] * arr_b[i+j]
            else:
                mul += arr_a[i+j] * arr_b[j]
        muls.append(mul)
    print(f"#{_} {max(muls)}")
