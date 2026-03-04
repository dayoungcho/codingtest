from collections import deque

def bfs(start_node):
    q = deque([start_node])
    distance = [-1] * (V+1)  # start_node로부터의 거리
    distance[start_node] = 0  # 시작점의 거리는 0

    while q:
        current_node = q.popleft()
        if current_node == G:
            return distance[current_node]
        for next_node in adj_list[current_node]:
            if distance[next_node] == -1:  # 방문하지 않은 노드라면
                distance[next_node] = distance[current_node] + 1
                q.append(next_node)
    return 0


T = int(input())

for tc in range(1,T+1):
    V, E = map(int, input().split())  # V: 노드의 개수, E: 간선의 개수

    adj_list = [[] for _ in range(V+1)]

    for i in range(E):
        n1, n2 = map(int, input().split())

        adj_list[n1].append(n2)
        adj_list[n2].append(n1)
    S, G = map(int, input().split())  # S: 출발 노드, G: 도착 노드
    ans = bfs(S)

    print(f"#{tc} {ans}")