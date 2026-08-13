def solution(s):
    stack = []
    for m in s:
        if m == '(':
            stack.append(m)
        if m == ')':
            if not stack:
                return False
            stack.pop()
    if not stack:
        return True
    return False