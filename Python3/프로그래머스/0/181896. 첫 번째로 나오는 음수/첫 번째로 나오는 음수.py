#첫 번째 인덱스에서 음수가 있었을 경우도 고려해야함

def solution(num_list):
    answer = 0
    check = 1
    for i in range(len(num_list)):
        check = check * num_list[i]
        if num_list[i] < 0:
            answer = i 
            break
    if check > 0:
        answer = -1
    return answer