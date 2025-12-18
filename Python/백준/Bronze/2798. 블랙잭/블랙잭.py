import itertools

n, m = map(int, input().split())
cards = list(map(int, input().split()))
ans = 0
for i in itertools.combinations(cards,3):
  summ = sum(i)
  if summ <= m:
    ans = max(ans, summ)
print(ans)