from itertools import permutations

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for r in range(N)]
    min_battery = max(arr[0]) * N**3  # 아무튼 임의로 큰 숫자

    order_cases = list(permutations(range(1,N),N-1))
    for order in order_cases:
        cnt = 0
        order = [0] + list(order) + [0]
        for i in range(len(order)-1):
            cnt += arr[order[i]][order[i+1]]
        if cnt < min_battery:
            min_battery = cnt
    
    print(f"#{tc} {min_battery}")