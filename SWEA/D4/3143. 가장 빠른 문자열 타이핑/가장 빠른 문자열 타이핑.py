T = int(input())  #  테스트 케이스 수

for _ in range(1, T+1):
    a, b = input().split()

    idx = 0
    cnt = 0
    while idx <= (len(a)-len(b)):
        if a[idx:idx+len(b)] == b:
            idx += len(b)
            cnt += 1
        else:
            idx += 1
    ans = len(a) - cnt*(len(b)-1)

    print(f"#{_} {ans}")