T = int(input())

for _ in range(1, T+1):
    N, M = map(int, input().split())  # N: 글자판 크기, M: 회문의 길이

    # 문자판 만들기
    arr = []
    for r in range(N):
        row = list(input())
        arr.append(row)
    ans = ''
    for i in range(N):
        for j in range(N-M+1):  # 기준 인덱스

            horizontal = ''.join(arr[i][j:j+M])

            for l in range(M//2):
                if horizontal[l] != horizontal[M-l-1]:
                    break
            else:
                ans = horizontal

            if ans:
                break

            vertical = ''

            for k in range(M):
                vertical += arr[j + k][i]

            for m in range(M//2):
                if vertical[m] != vertical[M-m-1]:
                    break
            else:
                ans = vertical

            if ans:
                break
        if ans:
            break
    
    print(f"#{_} {ans}")