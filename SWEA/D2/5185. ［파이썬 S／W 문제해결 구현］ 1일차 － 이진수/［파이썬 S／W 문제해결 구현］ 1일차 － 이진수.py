T = int(input())

for tc in range(1, T+1):
    n, num_16 = input().split()
    ans = ''
    for i in num_16:
        num_10 = int(i,16)
        num_2 = bin(num_10)
        num_2 = str(num_2[2:])
        if len(num_2) != 4:
            num_2 = '0' * (4-len(num_2)) + num_2
        ans += num_2
    print(f"#{tc} {ans}")