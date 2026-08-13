def solution(num_list):
    prod = 1
    sum = 0
    for i in num_list:
        prod *= i
        sum += i
    if prod < sum**2:
        answer = 1
    else:
        answer = 0
    return answer