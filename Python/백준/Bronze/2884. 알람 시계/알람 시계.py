hour, min = map(int, input().split())
minn = min-45
if minn >= 0:
  print(hour, minn)
else:
  hour = hour-1
  if hour < 0:
    hour = 23
  minn = 60+minn
  print(hour, minn)