def solution(price, money, count):
    total = 0
    for i in range(count):
        total += (price * (i+1))
    answer = total - money
    if answer < 0:
        return 0
    else:
        return answer