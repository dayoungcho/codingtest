lines = list()
while True:
  try:
    lines.append(input())
  except EOFError:
      break

for i in range(len(lines)-1):
  sides = list(map(int, lines[i].split()))
  c = max(sides)
  sides.remove(c)
  if c**2==(sides[0]**2+sides[1]**2):
    print('right')
  else:
    print('wrong')