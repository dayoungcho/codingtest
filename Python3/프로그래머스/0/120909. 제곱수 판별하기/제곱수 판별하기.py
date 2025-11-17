def solution(n):
    answer = 1 if n**(1/2)%1==0 else 2
    return answer

# n**(1/2) is int는 항상 False임 => float형으로 계산되기 때문,,