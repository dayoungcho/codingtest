nums = list()
n = int(input())
for i in range(n):
  nums.append(input())

for i in range(n):
  a, b = map(int, nums[i].split())
  print(a+b)