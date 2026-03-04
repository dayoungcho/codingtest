T = int(input()) 

for tc in range(1, T+1):
    N, M = map(int, input().split())
    adj_list = [[] for r in range(N+1)]
    adj_matrix = [[0] * (N+1) for r in range(N+1)]

    for i in range(M):
        n1, n2 = map(int, input().split())
        
        adj_list[n1].append(n2)
        adj_list[n2].append(n1)
        adj_matrix[n1][n2] = 1
        adj_matrix[n2][n1] = 1
    
    visited = [False] * (N+1)
    stack = []
    start = 1
    cnt = 1
    visited[start] = True
    stack.append(start)
    while sum(visited) != N:
        if stack:
            current = stack.pop()
            for next_node in adj_list[current]:
                if not visited[next_node]:
                    visited[next_node] = True
                    stack.append(next_node) 
        else:
            for i in range(1,N+1):
                if not visited[i]:
                    cnt += 1
                    stack.append(i)
                    visited[i] = True
                    break

    print(f"#{tc} {cnt}")