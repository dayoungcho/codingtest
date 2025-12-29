lst = list()
for i in range(10):
  lst.append(int(input()))

for i in range(10):
  lst[i] = lst[i]%42

print(len(set(lst)))