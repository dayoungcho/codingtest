a, b, v = map(int, input().split())
n = (v-a)//(a-b)


if a >= v-n*(a-b):
    print(n+1)
else:
    print(n+2)