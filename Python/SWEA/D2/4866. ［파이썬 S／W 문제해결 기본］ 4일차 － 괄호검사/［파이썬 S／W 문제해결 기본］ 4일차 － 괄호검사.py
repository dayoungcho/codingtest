def check_brackets(brackets):
    matches = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    stack = []

    for i in brackets:
        # 1) 여는 괄호이면 스택에 추가하기
        if i in matches.values():
            stack.append(i)
        # 2) 닫는 괄호이면
        elif i in matches.keys():
            # 2-1) 스택 안에 여는 괄호가 없으면 -1 반환
            if len(stack) == 0:
                return 0
            # 2-2) 스택 안에 여는 괄호가 있으면 꺼내기
            opening_bracket = stack.pop()
            # 2-2-1) 괄호의 종류가 맞지 않으면 -1 반환
            if matches[i] != opening_bracket:
                return 0
        else:
            continue
    # 3) 반복이 끝난 후 스택이 비어 있으면 모든 괄호의 짝이 맞는 것이므로 1 반환
    if len(stack) == 0:
        return 1
    else: # 아니면 -1 반환
        return 0

T = int(input())  # 테스트 케이스 수
for _ in range(1, T+1):
    brackets = input()
    ans = check_brackets(brackets)
    print(f"#{_} {ans}")