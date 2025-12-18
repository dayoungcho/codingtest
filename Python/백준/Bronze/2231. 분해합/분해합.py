n = input()
for i in range(int(n)):
  j = str(i)
  a = i
  for k in j:
    a += int(k)
  if a==int(n):
    print(i)
    break
  if i==int(n)-1:
    print(0)