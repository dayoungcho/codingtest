def solution(left, right):
    answer = 0
    for numerator in range(left, right+1):
        factor = []
        for denominator in range(1, numerator+1):
            if numerator % denominator == 0:
                factor.append(denominator)
        if len(factor) % 2 == 0:
            answer += numerator
        else:
            answer -= numerator
    return answer