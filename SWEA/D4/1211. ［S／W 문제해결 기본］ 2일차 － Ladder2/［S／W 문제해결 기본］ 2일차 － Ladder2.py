T = 10

for _ in range(1, T+1):
    t = int(input())  # 테스트 케이스 번호
    ladder = [list(map(int, input().split())) for r in range(100)]
    starting_point = []

    for i in range(100):
        if ladder[0][i] == 1:
            starting_point.append(i)

    min_dist = 100*100  # 최단거리 저장할 변수
    ans = 0  # 정답 저장할 변수

    for start in starting_point:
        r, c = 0, start  # 초기 시작점
        distance = 0
        while r < 99:
            if 0 <= c-1 < 100 and ladder[r][c-1] == 1:
                while 0 <= c-1 < 100 and ladder[r][c-1] == 1:
                    c -= 1
                    distance += 1
                r += 1
                distance += 1
            elif 0 <= c+1 < 100 and ladder[r][c+1] == 1:
                while 0 <= c+1 < 100 and ladder[r][c+1] == 1:
                    c += 1
                    distance += 1
                r += 1
                distance += 1
            else:
                r += 1
                distance += 1

        if distance < min_dist:
            min_dist = distance
            ans = start
        
    print(f"#{t} {ans}")