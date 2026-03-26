import sys



def todo(cmd):
  if cmd[0] == 'push':
    stack.append(int(cmd[1]))
  elif cmd[0] == 'pop':
    if stack:
      num = stack.pop()
      print(num)
    else:
      print(-1)
  elif cmd[0] == 'size':
    print(len(stack))
  elif cmd[0] == 'empty':
    if len(stack) == 0:
      print(1)
    else:
      print(0)
  elif cmd[0] == 'top':
    if stack:
      print(stack[-1])
    else:
      print(-1)

stack = []

N = int(sys.stdin.readline())
for _ in range(N):
  cmd = list(sys.stdin.readline().split())
  todo(cmd)