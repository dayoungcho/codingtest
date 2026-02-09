def is_pair(brackets):
    match = { ')': '(',
              ']': '[',
              '}': '{',
              '>': '<'}
    stack = []
    for i in brackets:
        if i in match.values():
            stack.append(i)
        elif i in match.keys():
            if len(stack) == 0:
                return 0
            brac = stack.pop()
            if match[i] != brac:
                return 0
        else:
            continue

    if len(stack) == 0:
        return 1
    else:
        return 0

for _ in range(1, 11):
    N = int(input())  # 테스트 케이스의 길이
    brackets = input()
    ans = is_pair(brackets)
    print(f"#{_} {ans}")