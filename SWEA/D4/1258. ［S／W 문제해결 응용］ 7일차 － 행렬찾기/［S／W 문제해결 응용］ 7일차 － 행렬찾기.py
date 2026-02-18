T = int(input())  # 테스트 케이스 개수

for _ in range(1, T+1):
    N = int(input())  # 배열 크기
    arr = [list(map(int, input().split())) for r in range(N)]
    cnt = 0
    boxes = []  # 각 박스의 [행,열]을 리스트로 저장
    r, c = 0, 0
    while r < N and c < N:
        if arr[r][c] != 0:
            cnt += 1
            box_r, box_c = r, c
            len_r = 1
            len_c = 1
            while box_r+1 < N and arr[box_r+1][box_c] != 0:
                box_r += 1
                len_r += 1
            while box_c+1 < N and arr[box_r][box_c+1] != 0:
                box_c += 1
                len_c += 1
            for i in range(r, box_r+1):
                for j in range(c, box_c+1):
                    arr[i][j] = 0
            boxes.append([len_r,len_c])
        if c < N-1:
            c += 1
        else:
            r += 1
            c = 0

    # 박스 정렬
    for i in range(cnt-1):
        for j in range(cnt-i-1):
            box_size_prev = boxes[j][0] * boxes[j][1]
            box_size_next = boxes[j+1][0] * boxes[j+1][1]
            if box_size_prev > box_size_next:
                boxes[j], boxes[j+1] = boxes[j+1], boxes[j]
            elif box_size_prev == box_size_next:
                if boxes[j][0] > boxes[j+1][0]:
                    boxes[j], boxes[j+1] = boxes[j+1], boxes[j]

    # 출력값 뽑기
    ans = ''
    for box in boxes:
        ans = ans +  ' '.join(map(str, box)) + ' '
    print(f"#{_} {cnt} {ans}")