T = int(input())

for _ in range(1, T+1):
    expr = list(input().split())
    stack = []

    for token in expr:
        if token.isdigit():
            stack.append(int(token))

        elif token in '+-*/':
            if len(stack) < 2:
                result = 'error'
                break
            right = stack.pop()
            left = stack.pop()

            if token == '+':
                stack.append(left + right)
            elif token == '-':
                stack.append(left - right)
            elif token == '*':
                stack.append(left * right)
            elif token == '/':
                stack.append(left / right)  

        elif token == '.':
            if len(stack) != 1:
                result = 'error'
                break
            result = int(stack.pop())
            break
        else:
            result = 'error'
            break

    print(f"#{_} {result}")