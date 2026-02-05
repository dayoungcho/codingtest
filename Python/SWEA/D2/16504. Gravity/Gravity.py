T = int(input())  # 테스트 케이스 수

for _ in range(1, T+1):
    N = int(input())  #  방의 가로길이
    boxes = list(map(int, input().split())) # 쌓여있는 상자의 수
    maxfall = 0  # 가장 큰 낙차 저장용 변수
    for idx in range(N):
        if boxes[idx] != 0:
            for box in range(1, boxes[idx]+1):  # 각 상자더미에서 각 박스의 낙차 구하기
                count = 0
                for i in range(idx+1,N):
                    if box - boxes[i] > 0:
                        count += 1
                if count > maxfall:
                    maxfall = count
    print(f"#{_} {maxfall}")