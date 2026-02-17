T = int(input())

for _ in range(1, T+1):
    N = int(input())  # 농장 크기
    
    arr = [list(map(int, list(input()))) for r in range(N)]

    start = N//2
    end = N//2
    ans = 0

    ans += sum(arr[N//2])

    for i in range(N//2):
        ans += sum(arr[i][start:end+1])
        ans += sum(arr[N-i-1][start:end+1])
        start -= 1
        end += 1

    print(f"#{_} {ans}")