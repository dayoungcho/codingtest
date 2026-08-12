def solution(x):
    digitsum = sum(map(int, list(str(x))))
    if x % digitsum == 0:
        return True
    else:
        return False