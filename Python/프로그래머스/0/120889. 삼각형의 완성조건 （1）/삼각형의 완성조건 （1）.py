def solution(sides):
    answer = 0
    longest = max(sides)
    if sum(sides)-longest > longest:
        answer = 1
    else:
        answer = 2
    return answer