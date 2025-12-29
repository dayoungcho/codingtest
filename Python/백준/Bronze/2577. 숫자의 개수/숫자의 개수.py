a = int(input())
b = int(input())
c = int(input())

mul = str(a*b*c)
lst = [0,0,0,0,0,0,0,0,0,0]
for i in mul:
  lst[int(i)] += 1

for i in lst:
  print(i)