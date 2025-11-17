def solution(my_string, overwrite_string, s):
    answer = ''
    for i in range(len(my_string)):
        if i < s or i >= s + len(overwrite_string):
            answer += my_string[i]
        elif i >= s and i < s + len(overwrite_string):
            answer += overwrite_string[i-s]
    return answer