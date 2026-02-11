# 우선순위 처리하는 함수: 숫자가 클수록 우선임
def get_precedence(op):
    if op == '*' or op == '/':
        return 2
    elif op == '+' or op == '-':
        return 1
    elif op == '(':
        return 0
    else:
        return -1
    
def to_postfix(infix):
    stack = []
    result = []
    for token in infix:
        # 숫자면 결과 리스트에 추가
        if token.isdigit():  # isalnum()으로 알파벳도 포함시켜서 처리할 수도 있음
            result.append(token)

        # 여는 괄호면 스택에 추가
        elif token == '(':
            stack.append(token)

        # 닫는 괄호면 스택에서 여는 괄호 나올 때까지 pop해서 결과 리스트에 추가
        elif token ==')':
            while len(stack) != 0 and stack[-1] != '(':
                result.append(stack.pop())
            stack.pop()  # 마지막 여는 괄호 제거

        # 연산자 처리
        else:
            # 스택에서 여는 괄호 나오기 전까지, 우선순위가 현재 토큰보다 높은 연산자가 스택 안에 있다면
            while len(stack) != 0 and stack[-1] != '(' and get_precedence(stack[-1]) >= get_precedence(token):
                # 결과 리스트에 추가해줌
                result.append(stack.pop())
            # 우선순위가 높은거 다 처리했으면 현재 토큰 연산자를 결과 리스트에 추가
            stack.append(token)
        
        # 남은 연산자 처리
    while stack:
        result.append(stack.pop())
        
    return ''.join(result)

def calculate_postfix(expr):
    stack = []
    for token in expr:
        if token.isdigit():
            stack.append(int(token))
        else:
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
    return stack.pop()


for _ in range(1, 11):
    N = int(input())
    expr = input()
    postfix = to_postfix(expr)
    ans = calculate_postfix(postfix)
    print(f"#{_} {ans}")


