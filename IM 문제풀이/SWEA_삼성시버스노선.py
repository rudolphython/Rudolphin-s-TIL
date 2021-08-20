T = int(input())

for test_case in range(1, T+1):
    N = int(input())

    station = [0]*5001

    for i in range(N):
        start, end = map(int, input().split())
        for j in range(start, end + 1):
            station[j] += 1

    P = int(input())
    result = []

    for i in range(P):
        p = int(input())
        result.append(station[p])


    print(f'#{test_case}', end=" ")
    print(*result)
