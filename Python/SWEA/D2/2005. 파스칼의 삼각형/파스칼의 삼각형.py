def pascal_triangle(N):
    if N == 1:
        return [1]
    elif N == 2:
        return [1, 1]
    else:
        lst = [1]
        for i in range(N-2):
            lst.append(pascal_triangle(N-1)[i] + pascal_triangle(N-1)[i+1])
        lst.append(1)
        return lst

T = int(input())  # 테스트 케이스 수

for _ in range(1, T+1):
    N = int(input())
    print(f'#{_}')
    for i in range(1,N+1):
        print(' '.join(map(str, pascal_triangle(i))))