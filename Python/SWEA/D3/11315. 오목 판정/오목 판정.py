def is_bingo(N, arr):
    # 델타(오른쪽 위부터 시계방향, 오른쪽이나 아래로 가는 방향만 탐색)
    dr = [-1, 0, 1, 1]
    dc = [1, 1, 1, 0]
    for i in range(N):
        for j in range(N):
            # 기준점 인덱스: (i,j)
            if arr[i][j] == 'o':
                for k in range(4):
                    rr = i + 4*dr[k]
                    cc = j + 4*dc[k]
                    if 0 <= rr < N and 0 <= cc < N:
                        for m in range(4,0,-1):
                            if arr[i+m*dr[k]][j+m*dc[k]] != 'o':
                                break
                        else:
                            return "YES"
    return "NO"

T = int(input())

for _ in range(1, T+1):
    N = int(input())  # 판 크기
    arr = [list(input()) for r in range(N)]
    ans = is_bingo(N, arr)
    print(f"#{_} {ans}")