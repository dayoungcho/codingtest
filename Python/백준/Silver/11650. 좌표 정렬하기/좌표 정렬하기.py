N = int(input())
dots = [list(map(int, input().split()))for _ in range(N)]
dots.sort(key = lambda x: (x[0],x[1]))
for i in range(N):
  print(' '.join(map(str, dots[i])))