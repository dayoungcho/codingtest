T = int(input())  #  테스트 케이스 수

for _ in range(1, T+1):
    N, K = map(int, input().split())

    arr = [list(input().split()) for r in range(N)]
    transposed = list(map(list,zip(*arr)))

    cnt = 0

    for i in range(N):
        squeezed = ''.join(arr[i]).strip('0').split('0')
        squeezed2 = ''.join(transposed[i]).strip('0').split('0')
        for j in squeezed:
            if len(j) == K:
                cnt += 1
        for j in squeezed2:
            if len(j) == K:
                cnt += 1
    
            
    print(f"#{_} {cnt}")