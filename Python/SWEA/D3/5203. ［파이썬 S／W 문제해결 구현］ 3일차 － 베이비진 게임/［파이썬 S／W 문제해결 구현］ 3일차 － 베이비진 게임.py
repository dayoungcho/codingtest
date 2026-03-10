def check_run(count):
    for i in range(8):
        if count[i] != 0 and count[i+1] != 0 and count[i+2] != 0:
            return True
    return False

def check_triplet(count):
    for i in range(10):
        if count[i] >= 3:
            return True
    return False

T = int(input())

for tc in range(1, T+1):
    cards = list(map(int, input().split()))
    result = 0

    p1_count = [0] * 10
    p2_count = [0] * 10

    for i in range(len(cards)):
        if i % 2 == 0:
            p1_count[cards[i]] += 1
            if i >= 2:
                if check_triplet(p1_count) or check_run(p1_count):
                    result = 1
                    break
        elif i % 2 == 1:
            p2_count[cards[i]] += 1
            if i >= 2:
                if check_triplet(p2_count) or check_run(p2_count):
                    result = 2
                    break
    print(f"#{tc} {result}")