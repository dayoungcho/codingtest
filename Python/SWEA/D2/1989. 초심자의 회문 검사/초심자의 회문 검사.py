T = int(input())

for _ in range(1, T+1):
    word = input()
    N = len(word)
    flag = 1

    for i in range(N//2):
        if word[i] != word[N-i-1]:
            flag = 0

    print(f"#{_} {flag}")