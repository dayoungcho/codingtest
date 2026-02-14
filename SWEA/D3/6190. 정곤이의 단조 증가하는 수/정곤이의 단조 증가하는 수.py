T = int(input())  #  테스트 케이스 수

def is_increasing(number):
    num_as_str = str(number)
    for i in range(len(num_as_str)-1):
        if num_as_str[i] > num_as_str[i+1]:
            return False
    else:
        return True

for _ in range(1, T+1):
    N = int(input())  # 정수 개수
    int_lst = list(map(int, input().split()))
    candidates = []
    ans = -1
    for i in range(N):
        for j in range(i+1, N):
            candidate = int_lst[i] * int_lst[j]
            if is_increasing(candidate):
                if candidate > ans:
                    ans = candidate
            
    print(f"#{_} {ans}")
