def solution(str1, str2):
    answer = 0
    str11 = str1.split(str2)
    if len(str11) >1:
        answer = 1
    else:
        answer=2
    return answer

# 다른 풀이
# def solution(str1, str2):
#     answer = 1 if str2 in str1 else 2
#     return answer