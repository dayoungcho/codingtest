def postorder(t):
    global expr
    if t:
        postorder(left[t])
        postorder(right[t])
        expr.append(num_arr[t])

def calculator(expr):
    stack = []
    for token in expr:
        if token.isdigit():
            stack.append(token)
        else:
            right = stack.pop()
            left = stack.pop()

            if token == '+':
                stack.append(int(left) + int(right))
            elif token == '-':
                stack.append(int(left) - int(right))
            elif token == '*':
                stack.append(int(left) * int(right))
            elif token == '/':
                stack.append(int(left) / int(right))
    return stack.pop()
            

T = 10

for _ in range(1, T+1):
    V = int(input())  # 노드의 수

    num_arr = [0] * (V+1)  # 각 노드에 할당된 숫자 저장
    left = [0] * (V+1)
    right = [0] * (V+1)

    for i in range(1,V+1):
        info = list(input().split())
        

        if info[1] in '+-*/':
            left[i] = int(info[2])
            right[i] = int(info[3])
        num_arr[i] = info[1]

    expr = []
    postorder(1)
    ans = calculator(expr)
    print(f"#{_} {int(ans)}")