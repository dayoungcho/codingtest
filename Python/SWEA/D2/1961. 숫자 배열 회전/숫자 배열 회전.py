
T = int(input())

for _ in range(1, T+1):
    N = int(input())  # 행렬의 차원 N
    arr = []
    for r in range(N):
        row = list(map(int, input().split()))
        arr.append(row)
    arr_90 = list(zip(*arr[::-1]))
    arr_180 = list(zip(*arr_90[::-1]))
    arr_270 = list(zip(*arr_180[::-1]))
    print(f"#{_}")
    for i in range(N):
        print(''.join(map(str, arr_90[i])), ''.join(map(str, arr_180[i])), ''.join(map(str, arr_270[i])))