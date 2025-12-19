t = int(input())
ans = []
for i in range(t):
  h, w, n = map(int, input().split())
  if n%h == 0:
    floor = h
    ho = n//h
  else:
    floor = n%h
    ho = n//h + 1
  if ho >= 10:
    ans.append(str(floor)+str(ho))
  else:
    ans.append(str(floor)+'0'+str(ho))
for i in range(t):
  print(ans[i])