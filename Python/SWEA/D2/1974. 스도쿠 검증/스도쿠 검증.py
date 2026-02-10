T = int(input())

for _ in range(1,T+1):

    # 행렬 생성
    arr = []
    for r in range(9):
        row = list(map(int, input().split()))
        arr.append(row)
    ans_arr = [1,2,3,4,5,6,7,8,9]
    ans = 1
    for i in range(9):
        # 가로 검사
        horizontal = arr[i][:]  # 여기서 슬라이싱을 안하면 원본 배열이 변해버린다...(얕은 복사)
        horizontal.sort()
        if horizontal != ans_arr:
            ans = 0
            break

        # 세로 검사
        vertical = []
        for j in range(9):
            vertical.append(arr[j][i])
        vertical.sort()
        if vertical != ans_arr:
            ans = 0
            break

    else:  # 가로세로 다 통과했을 경우 3*3 격자도 검사
        for i in range(0,9,3):
            for j in range(0,9,3):
                square = []
                for k in range(3):
                    square.extend(arr[i+k][j:j+3])
                square.sort()
                if square != ans_arr:
                    ans = 0
                    break
            if ans == 0:
                break

    print(f"#{_} {ans}")
