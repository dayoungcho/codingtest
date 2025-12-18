lines = list()
while True:
  try:
    lines.append(input())
  except EOFError:
      break

for i in lines:
  print(sum(list(map(int, i.split()))))