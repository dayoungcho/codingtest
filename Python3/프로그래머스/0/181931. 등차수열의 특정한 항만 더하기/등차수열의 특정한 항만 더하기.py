def solution(a, d, included):
    a_num = 0
    d_num = 0
    for i in range(len(included)):
        if included[i]:
            a_num += 1
            d_num += i
    answer = a * a_num + d * d_num
    return answer