def solution(my_string, is_suffix):
    suffix = []
    for i in range(len(my_string)):
        suffix.append(my_string[i:])
    answer = 1 if is_suffix in suffix else 0
    return answer


# 다른풀이
def solution(my_string, is_suffix):
    if my_string[-len(is_suffix):]==is_suffix:
        return 1
    return 0