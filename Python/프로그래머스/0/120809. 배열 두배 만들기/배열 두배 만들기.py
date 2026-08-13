def solution(numbers):
    answer = []
    for i in numbers:
        answer.append(i*2)
    return answer


# list comprehension

def solution(numbers):
    return [i*2 for i in numbers]