def dfs(row):
    global my_min, my_sum

    if my_min < my_sum:
        return

    if row >= N:
        if my_min > my_sum:
            my_min = my_sum
            return

    for next in range(N):
        if visited[next] == 1:
            continue
        my_sum += arr[row][next]
        visited[next] = 1
        dfs(row+1)
        my_sum -= arr[row][next]
        visited[next] = 0


T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    my_min = 9999999
    my_sum = 0
    visited = [0] * N
    dfs(0)

    print(my_min)
