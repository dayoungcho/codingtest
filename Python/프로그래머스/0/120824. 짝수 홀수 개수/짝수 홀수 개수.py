def solution(num_list):
    even = 0
    odd = 0
    for i in num_list:
        if i%2==0:
            even += 1
        else:
            odd += 1
    answer = [even, odd]
    return answer


# 다른 풀이
# def solution(num_list):
#     answer = [0,0]
#     for i in num_list:
#         answer[i%2] += 1
#     return answer