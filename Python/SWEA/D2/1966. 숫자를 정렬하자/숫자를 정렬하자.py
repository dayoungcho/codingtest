T = int(input())  # 테스트 케이스 수

for _ in range(1, T+1):
    N = int(input())  # 숫자의 개수
    arr = list(map(int, input().split()))

    for i in range(N):
        min_idx = i
        for j in range(i+1, N):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    
    print(f"#{_} {' '.join(map(str, arr))}")