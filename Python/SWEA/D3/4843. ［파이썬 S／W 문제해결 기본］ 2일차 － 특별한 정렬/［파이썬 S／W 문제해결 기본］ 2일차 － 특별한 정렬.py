T = int(input())  # 테스트 케이스 수

for _ in range(1, T+1):
    N = int(input())  # 정수의 개수
    arr = list(map(int, input().split()))  # N개의 정수 리스트

    mode = 2  # 1: 최솟값 찾기, 2: 최댓값 찾기

    for i in range(N):
        if mode == 1:

            min_idx = i

            for j in range(i+1, N):
                if arr[j] < arr[min_idx]:
                    min_idx = j
            
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            mode = 2

        elif mode == 2:
            max_idx = i

            for j in range(i+1, N):
                if arr[j] > arr[max_idx]:
                    max_idx = j
            arr[i], arr[max_idx] = arr[max_idx], arr[i]
            mode = 1
    arr = arr[:10]
    
    print(f"#{_} {' '.join(map(str, arr))}")