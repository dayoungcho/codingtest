def solution(s):
    answer = ''
    stack = []
    for i in s:
        if i == ' ':
            while len(stack) != 0:
                stack.pop()
            answer += ' '
        else:
            stack.append(i)
            if len(stack) % 2 == 0:
                answer += i.lower()
            else:
                answer += i.upper()
    return answer