n, m = map(int, input().split())
arr = [list(input()) for _ in range(n)]
min_cnt = n * m

color = ['B','W']

for i in range(n-8+1):
  for j in range(m-8+1):
    for k in range(2):
      cnt = 0
      mode = k
      for r in range(8):
        for c in range(8):
          if arr[i+r][j+c] != color[mode]:
            cnt += 1
          mode = int(not mode)
          if c == 7:
            mode = int(not mode)
      if cnt < min_cnt:
        min_cnt = cnt

print(min_cnt)