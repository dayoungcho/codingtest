import itertools

def solution(number):
    answer = 0
    cases = list(itertools.combinations(number, 3))
    for case in cases:
        if sum(case) == 0:
            answer += 1
    return answer