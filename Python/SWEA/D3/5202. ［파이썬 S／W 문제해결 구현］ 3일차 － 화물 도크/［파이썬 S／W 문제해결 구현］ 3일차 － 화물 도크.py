T = int(input())

for tc in range(1,T+1):
    N = int(input())
    works = [tuple(map(int, input().split())) for _ in range(N)]
    works.sort(key = lambda x: -x[1])
    cnt = 0
    end_time = 0
    while works:
        work = works.pop()
        if work[0] >= end_time:  # 만약 현재 하려고 하는 작업의 시작 시간이 이전 작업이 끝나는 시간과 같거나 그 이후라면
            cnt += 1
            end_time = work[1]
    print(f"#{tc} {cnt}")