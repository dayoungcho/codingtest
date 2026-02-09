for _ in range(1, 11):
    N, chars = input().split()
    stack = []
    for char in chars:
        # 스택 안에 아무것도 없으면 스택에 문자 집어넣기
        if len(stack) == 0:
            stack.append(char)
        # 스택 맨 뒤의 값이 현재 문자와 같으면 꺼내기
        elif stack[-1] == char:
            out = stack.pop()
        # 이외의 경우엔 스택에 문자 집어넣기
        else:
            stack.append(char)

    print(f"#{_} {''.join(stack)}")