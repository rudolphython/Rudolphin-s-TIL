T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    days = list(map(int, input().split()))

    result = 0
    max_cost = days[-1]
    for i in range(N-2, -1, -1):
        if max_cost > days[i]:
            result += max_cost - days[i]

        else :
            max_cost = days[i]

    print(f"#{test_case} {result}")
