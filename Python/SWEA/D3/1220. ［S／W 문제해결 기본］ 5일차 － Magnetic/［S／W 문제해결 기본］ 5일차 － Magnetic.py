for _ in range(1,11):
    N = int(input())
    arr = [list(input().split()) for r in range(100)]
    transposed = list(map(list, zip(*arr)))
    cnt = 0
    for i in range(100):
        row = ''.join(transposed[i]).split('0')
        joined = ''.join(row)
        joined = joined.replace('12', 'V')
        cnt += joined.count('V')


    print(f"#{_} {cnt}")