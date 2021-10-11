T = 10

for test_case in range(1, T+1):
    tc, pws = map(str, input().split())
    stack = []

    for i in range(len(pws)):
        if len(stack) == 0:
            stack.append(pws[i])
        else :
            if stack[-1] == pws[i]:
                stack.pop()
            else :
                stack.append(pws[i])

    result = ""
    for j in stack:
        result += j

    print(result)
