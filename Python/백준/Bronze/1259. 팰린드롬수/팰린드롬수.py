nums = []
while True:
  num = input()
  if num == '0':
    break
  nums.append(num)


for num in nums:
  ans = 'yes'
  for i in range(len(num)//2):
    if num[i] != num[-i-1]:
      ans = 'no'
      break 
  print(ans)