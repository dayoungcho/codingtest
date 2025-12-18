import math

n = int(input())
nums = list(map(int, input().split()))
count = 0

def ifprime(num):
  if num==1:
    return False
  for j in range(2,int(math.sqrt(num))+1):
    if num%j==0:
      return False
  return True

for i in nums:
  if ifprime(i):
    count += 1

print(count)