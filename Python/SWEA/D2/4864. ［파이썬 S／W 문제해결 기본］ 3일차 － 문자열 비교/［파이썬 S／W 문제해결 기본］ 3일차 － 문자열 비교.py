def brute_force(target, string):
    N = len(target)
    M = len(string)

    i, j = 0, 0  # target, string의 초기인덱스

    while i < N and j < M:
        if target[i] != string[j]:
            j = j - i
            i = -1
        i += 1
        j += 1
    if i == N:
        return 1
    else:
        return 0
    
T = int(input())

for _ in range(1, T+1):
    str1 = input()
    str2 = input()
    ans = brute_force(str1, str2)
    print(f"#{_} {ans}")
