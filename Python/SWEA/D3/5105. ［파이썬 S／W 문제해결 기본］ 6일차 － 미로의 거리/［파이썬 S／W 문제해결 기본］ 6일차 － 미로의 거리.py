# 델타(상하좌우)
dr = [-1,1,0,0]
dc = [0,0,-1,1]

def dfs(r,c):
    global cnt
    if arr[r][c] == 3:
        return True
    
    for i in range(4):
        rr = r + dr[i]
        cc = c + dc[i]
        if 0 <= rr < N and 0 <= cc < N and visited[rr][cc] is False and arr[rr][cc] != 1:
            cnt += 1
            visited[rr][cc] = True
            if dfs(rr,cc):
                return True
    cnt -= 1
    return False

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    arr= [list(map(int,input())) for r in range(N)]
    visited = [[False] * N for r in range(N)]

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                r, c = i, j  # 시작점
                visited[r][c] = True
                break
    cnt = 0
    ans = dfs(r,c)
    if ans:
        cnt -= 1
    else:
        cnt = 0

    print(f"#{tc} {cnt}")