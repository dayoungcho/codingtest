a, b = map(int, input().split())
mul = a*b
while True:
  a, b = b, a%b
  if b==0:
    break
print(a)
print(int(mul/a))