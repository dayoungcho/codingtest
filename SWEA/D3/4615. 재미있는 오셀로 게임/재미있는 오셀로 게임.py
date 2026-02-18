T = int(input())  # 테스트 케이스 개수
# 왼쪽 대각선 위부터 시계방향
dr = [-1, -1, -1, 0, 1, 1, 1, 0]
dc = [-1, 0, 1, 1, 1, 0, -1, -1]

for _ in range(1, T+1):

    N, M = map(int, input().split())  # N: 보드의 한 변의 길이, M: 플레이어가 돌을 놓는 횟수
    # 초기 보드 설정
    arr = [[0] * N for r in range(N)]
    arr[N//2-1][N//2-1] = 2
    arr[N//2][N//2] = 2
    arr[N//2-1][N//2] = 1
    arr[N//2][N//2-1] = 1

    for put in range(M):
        c, r, color = map(int, input().split())  # r, c: 돌을 놓는 좌표, color: 돌 색깔(1이 흑돌)
        r -= 1
        c -= 1
        arr[r][c] = color
        flipped = False
        # 모든 방향 탐색한다...
        for i in range(8): 
            for dist in range(max(r, c, N-r-1 , N-c-1),1,-1):
                rr = r + dr[i] * dist
                cc = c + dc[i] * dist
                if 0 <= rr < N and 0 <= cc < N and arr[rr][cc] == color:
                    for j in range(1,dist):
                        if color == 1:
                            if arr[r+dr[i]*j][c+dc[i]*j] != 2:
                                break
                        elif color == 2:
                            if arr[r+dr[i]*j][c+dc[i]*j] != 1:
                                break
                    else:
                        for j in range(1,dist):
                            if color == 1:
                                arr[r+dr[i]*j][c+dc[i]*j] = 1
                            elif color == 2:
                                arr[r+dr[i]*j][c+dc[i]*j] = 2
                        break
            if flipped is True:
                break

    ans = ''
    for r in range(N):
        ans += ''.join(map(str, arr[r]))
    
    print(f"#{_} {ans.count('1')} {ans.count('2')}")