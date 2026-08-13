def solution(s):
    upper = []
    lower = []
    for i in s:
        if i.isupper():
            upper.append(i)
        else:
            lower.append(i)
    upper = sorted(upper, reverse=True)
    lower = sorted(lower, reverse=True)
    upper = ''.join(upper)
    lower = ''.join(lower)
    return lower + upper