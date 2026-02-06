T = 10

for _ in range(1, T+1):
    N = 8
    M = int(input())  # 회문 길이

    # 글자판 생성
    arr = []
    for r in range(N):
        row = list(input())
        arr.append(row)

    cnt = 0  # 회문 개수 카운트

    for i in range(N):
        for j in range(N - M + 1):  # 기준 인덱스
            # 가로 문자열부터 회문 여부 검사
            horizontal = ''.join(arr[i][j:j + M])

            for l in range(M // 2):
                if horizontal[l] != horizontal[M - l - 1]:
                    break
            else:
                cnt += 1


            # 세로 문자열 회문 여부 검사
            vertical = ''
            for k in range(M):
                vertical += arr[j + k][i]

            for m in range(M // 2):
                if vertical[m] != vertical[M - m - 1]:
                    break
            else:
                cnt += 1


    print(f"#{_} {cnt}")