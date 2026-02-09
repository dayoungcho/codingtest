T = int(input())

for _ in range(1, T+1):
    money_dic = {50000: 0,
                 10000: 0,
                 5000: 0,
                 1000: 0,
                 500: 0,
                 100: 0,
                 50: 0,
                 10: 0}
    N = int(input())  # 손님에게 거슬러 주어야 할 금액

    for i in money_dic.keys():
        money_dic[i] = N//i
        N %= i
    print(f"#{_}")
    print(' '.join(map(str, money_dic.values())))