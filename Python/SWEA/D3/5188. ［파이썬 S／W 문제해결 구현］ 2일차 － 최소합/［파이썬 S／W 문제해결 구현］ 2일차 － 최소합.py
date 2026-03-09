# 델타(아래, 오른쪽)
dr = [1, 0]
dc = [0, 1]

def dfs(r,c):
    global cnt, min_cnt
    if r == N-1 and c == N-1:
        return
    for i in range(2):
        rr = r + dr[i]
        cc = c + dc[i]
        if 0 <= rr < N and 0 <= cc < N:
            cnt = visited[r][c] + arr[rr][cc]
            if visited[rr][cc] == 0:
                visited[rr][cc] = cnt
            else:
                if visited[rr][cc] > cnt:
                    visited[rr][cc] = cnt
            dfs(rr,cc)
    

T = int(input())

for tc in range(1,T+1):

    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0
    visited = [[0] * N for r in range(N)]
    visited[0][0] = arr[0][0]
    dfs(0,0)
    
    print(f"#{tc} {visited[N-1][N-1]}")