T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]

    i = 0
    j1 = N // 2
    j2 = N // 2
    my_sum = 0

    while i <= N // 2:
        for j in range(j1, j2+1):
            my_sum += arr[i][j]
        i += 1
        j1 -= 1
        j2 += 1

    i = N - 1
    j1 = N // 2
    j2 = N // 2
    while i > N//2:
        for j in range(j1, j2+1):
            my_sum += arr[i][j]
        i -= 1
        j1 -= 1
        j2 += 1

    print(f"#{test_case} {my_sum}")




