def dfs(row):
    global cnt, min_cnt
    if row == N:
        if cnt < min_cnt:
            min_cnt = cnt
        return
    if cnt > min_cnt:
        return
    for i in range(N):
        if not visited[i]:
            cnt += arr_T[row][i]
            visited[i] = True
            dfs(row+1)
            visited[i] = False
            cnt -= arr_T[row][i]

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for r in range(N)]
    arr_T = list(map(list,zip(*arr)))
    cnt = 0
    min_cnt = 10*N
    # for case in cases:
    #     cnt = 0
    #     for i in range(N):
    #         cnt += arr_T[i][case[i]]
    #     if cnt < min_cnt:
    #         min_cnt = cnt
    # print(f"#{tc} {min_cnt}")

    visited = [False] * N
    dfs(0)
    print(f"#{tc} {min_cnt}")