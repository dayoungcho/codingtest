sums = []
while True:
  a, b = map(int, input().split())
  if a == 0 and b == 0:
    break
  sums.append(a+b)

for i in range(len(sums)):
  print(sums[i])