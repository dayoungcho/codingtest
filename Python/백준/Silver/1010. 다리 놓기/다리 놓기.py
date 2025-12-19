T = int(input())
ans = [1,1,1]

for i in range(T):
    n , m = map(int, input().split())

    numerator = 1
    denominator = 1
    
    for i in range(n):
        numerator *= (m - i)
    
    for i in range(n):
        denominator *= (n - i)
    result = numerator // denominator
    print(result)