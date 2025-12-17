lines = list()

while True :
    try :
        lines.append(input())
    except EOFError :
        break

for i in range(len(lines)):
  N, S = lines[i].split()
  print(int(S)//(int(N)+1))