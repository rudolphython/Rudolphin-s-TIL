T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    day = list(map(int, input().split()))

    result = 0
    max_cost = day[-1]
    for i in range(N - 2, -1, -1):
        if max_cost > day[i]:
            result += max_cost - day[i]

        else:
            max_cost = day[i]

    print(f"#{test_case} {result}")
