def preorder(t):
    global ans
    if t:
        ans += 1
        preorder(left[t])
        preorder(right[t])


T = int(input())

for _ in range(1, T+1):
    E, N = map(int, input().split())  # E: 간선의 개수, N: 루트 노드
    V = E + 1  # V: 노드의 개수
    arr = list(map(int, input().split()))

    left = [0] * (V+1)
    right = [0] * (V+1)


    for i in range(E):
        parent = arr[i*2]
        child = arr[i*2+1]

        if left[parent] == 0:
            left[parent] = child
        else:
            right[parent] = child

    ans = 0
    preorder(N)
    print(f"#{_} {ans}")