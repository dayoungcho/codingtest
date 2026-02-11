T = int(input())

for _ in range(1, T+1):
    # N:  붕어빵 사러 오는 사람 수
    # M초에 K개의 붕어빵을 만들 수 있음
    N, M, K = map(int, input().split())
    customer = list(map(int, input().split()))  # 손님이 오는 시간 리스트
    customer.sort()  # 손님 오는 순서대로 정렬
    final_customer = customer[-1]  # 가장 늦는 손님

    # 만들어지는 붕어빵의 개수를 리스트에 표시.... 
    # ex) M=2, K=1이고 가장 늦게 오는 손님이 4초에 올 때 -> [0,1,0,1]
    boong_lst = [0] * final_customer
    for i in range(final_customer):
        if (i+1) % M == 0:
            boong_lst[i] = K

    # 붕어빵 개수 리스트를 순회하며 각 손님이 붕어빵을 살 수 있는지 확인
    '''
    손님이 2, 4초에 온다면 
    i) 2초에 오는 손님 -> 붕어빵리스트 인덱스 0~1까지 순회할 때, 2초에 붕어빵이 1개 있으므로 붕어빵을 살 수 있음
                        남은 붕어빵을 1 -> 0으로 변경

    ii) 4초에 오는 손님 -> 붕어빵리스트 인덱스 0~3까지 순회할 때, 4초에 붕어빵이 1개 있으므로 붕어빵을 살 수 있음
    '''
    ans = 'Possible'
    for ctmer in customer:
        for i in range(ctmer):
            if boong_lst[i] != 0:
                boong_lst[i] -= 1
                break
        else:  # 순회 범위 내에 붕어빵이 하나도 없다면 붕어빵을 살 수 없음
            ans = 'Impossible'
            break

    print(f"#{_} {ans}")