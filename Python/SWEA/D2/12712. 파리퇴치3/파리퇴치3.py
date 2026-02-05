T = int(input())  # 테스트 케이스 수

# + 형태로 분사될 때 더할 값(상하좌우)
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# x 형태로 분사될 때 더할 값(좌상부터 시계방향)
xr = [-1, -1, 1, 1]
xc = [-1, 1, 1, -1]


for _ in range(1, T+1):

    N , M = map(int, input().split())  # N: 배열 크기, M: 스프레이 세기

    # 파리 배열 생성
    arr = []
    for r in range(N):
        row = list(map(int, input().split()))
        arr.append(row)
    
    flies = []  # 스프레이를 한 번 분사했을 때 잡는 파리의 수를 저장하는 리스트

    # 모든 칸을 순회하면서 몇 마리 잡을 수 있는지 세기
    for i in range(N):
        for j in range(N):
            r, c = i, j  # 중심 인덱스값
            sum1 = 0  # + 형태로 분사될 때 잡는 파리 수
            sum2 = 0  # x 형태로 분사될 때 잡는 파리 수
            # 4방향 순회
            for k in range(4):
                for l in range(1,M):
                    if 0 <= r + l * dr[k] < N and 0 <= c + l * dc[k] < N:
                        sum1 += arr[r + l * dr[k]][c + l * dc[k]]

                    if 0 <= r + l * xr[k] < N and 0 <= c + l * xc[k] < N:
                        sum2 += arr[r + l * xr[k]][c + l * xc[k]]

            sum1 += arr[r][c]
            sum2 += arr[r][c]
            flies.append(sum1)
            flies.append(sum2)

    print(f"#{_} {max(flies)}")