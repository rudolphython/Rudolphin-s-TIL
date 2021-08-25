T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    arr = list(map(str, input().split()))
    if len(arr) % 2 == 0:
        a = arr[0:N//2]
        b = arr[N//2:N]

    else :
        a = arr[0 : N//2+1]
        b = arr[N//2+1 : N]

    result = []


    if len(a) > len(b):
        for i in range(len(b)):
            result.append(a[i])
            result.append(b[i])
        result.append(a[-1])
    else :
        for i in range(len(b)):
            result.append(a[i])
            result.append(b[i])

    print(f"#{test_case}", end=" ")
    print(*result)
