l = int(input())
s = input()
r = 31
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

ans = 0
for i in range(l):
  ans += (alphabet.index(s[i])+1)* r**i
print(ans)