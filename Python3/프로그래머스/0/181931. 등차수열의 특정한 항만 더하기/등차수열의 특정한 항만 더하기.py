def solution(a, d, included):
    a_num = 0
    d_num = 0
    for i in range(len(included)):
        if included[i]:
            a_num += 1
            d_num += i
    answer = a * a_num + d * d_num
    return answer


# 똑똑하게 코딩한사람

def solution(a, d, included):
    answer = 0
    for i in range(len(included)):
        answer += (a + d * i) * int(included[i])
    return answer