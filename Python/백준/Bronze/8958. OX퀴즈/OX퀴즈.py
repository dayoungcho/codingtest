n = int(input())
lst = list()
score_list = list()

for i in range(n):
  lst.append(input())


for ox in lst:
  score = 0
  oxlist = ox.split('X')
  for i in oxlist:
    score += len(i)*(len(i)+1)/2
  score_list.append(int(score))

for i in score_list:
  print(i)
      