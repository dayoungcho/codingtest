
T = int(input())

for tc in range(1, T+1):
    n = int(input())  # 스위치의 개수
    prev_switches = list(map(int, input().split()))  # 초기 스위치 상태
    next_switches = list(map(int, input().split()))  # 바꿀 스위치 상태

    # 버튼을 누르는 최소 횟수
    result = 0

    # 스위치 리스트를 순회하며 바꿔야하는 것과 다르면 스위치를 누름
    for i in range(n):
        # 같으면 패스
        if prev_switches[i] == next_switches[i]:
            continue

        # 다르면
        result += 1
        # 누른 애부터 끝까지 순회
        for j in range(i, n):
            prev_switches[j] = 1 - prev_switches[j]  # 0이면 1, 1이면 0으로 전환

    print(f"#{tc} {result}")