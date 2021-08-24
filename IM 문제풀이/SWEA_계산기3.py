T = 10

for tc in range(T):
    N = int(input())
    infix = input().rstrip()
    stack = []
    result = []
    for ch in infix:
        if '0' <= ch <= '9':
            result.append(ch)
        elif ch == '(':
            stack.append(ch)
        elif ch == ')':
            while len(stack) != 0 and stack[-1] != '(':
                result.append(stack.pop(-1))
            stack.pop(-1)
        elif ch == '*' or ch == '/':
            while len(stack) != 0 and stack[-1] != "(" and \
                    (stack[-1] == "*" or stack[-1] == "/"):
                result.append(stack.pop(-1))
            stack.append(ch)
        elif ch == '+' or ch == '-':
            while len(stack) != 0 and stack[-1] != '(':
                result.append(stack.pop(-1))
            stack.append(ch)

    while len(stack) != 0:
        result.append(stack.pop(-1))

    calc = []
    for i in result:
        if '0' <= i <= '9':
            calc.append(int(i))

        elif i == '*':
            a = calc.pop()
            b = calc.pop()
            ans = a * b
            calc.append(ans)

        elif i == '+':
            a = calc.pop()
            b = calc.pop()
            ans = a + b
            calc.append(ans)

    print(f"#{tc + 1} {calc[0]}")