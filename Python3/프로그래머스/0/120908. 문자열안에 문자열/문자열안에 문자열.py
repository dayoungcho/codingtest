def solution(str1, str2):
    answer = 0
    str11 = str1.split(str2)
    if len(str11) >1:
        answer = 1
    else:
        answer=2
    return answer