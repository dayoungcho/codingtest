T = int(input())


for tc in range(1, T+1):
    N, M = map(int, input().split())  # N: 컨테이너 수, M: 트럭 수
    weights = list(map(int, input().split()))  # 각 컨테이너의 무게 리스트
    capacity = list(map(int, input().split()))  # 각 트럭의 적재용량
    weights.sort()
    capacity.sort()
    ans = 0

    while weights and capacity:
        cap = capacity.pop()
        while weights and weights[-1] > cap:
            weights.pop()
        if weights:
            ans += weights.pop()

    print(f"#{tc} {ans}")