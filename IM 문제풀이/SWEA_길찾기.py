T = 10

for test_case in range(1, T+1):
    t, V = map(int, input().split())    # t는 테스트 케이스, V는 노선

    arr = list(map(int, input().split()))
    adj = [[0] * 100 for _ in range(100)]


    for i in range(0, V*2, 2):
        x, y = arr[i], arr[i+1]
        adj[x][y] = 1

    visited = [0] * 100
    start = 0
    end = 99

    def arrive(now):
        for next in range(100):
            if adj[now][next] == 1 and visited[next] == 0:
                visited[next] = 1
                arrive(next)

    visited[start] = 1
    arrive(0)

    print(f"#{test_case} {visited[end]}")