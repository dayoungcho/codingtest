n = int(input())
size = list(map(int, input().split()))
t, p = map(int, input().split())

tn = 0
for i in size:
  if i%t==0:
    tn += i//t
  else:
    tn += i//t + 1
print(tn)
print(n//p, n%p)