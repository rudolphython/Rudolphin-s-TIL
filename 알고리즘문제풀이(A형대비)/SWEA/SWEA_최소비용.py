def dfs(now_x, now_y, weight):
    global result
    if now_x == N-1 and now_y == N-1:
        if weight <= result:
            result = weight
        return

    if weight > result:
        return

    dx = [1,0]
    dy = [0,1]
    for i in range(2):
        next_x = now_x + dx[i]
        next_y = now_y + dy[i]
        if 0 <= next_x < N and 0 <= next_y < N:
            if visited[next_x][next_y] == 1:
                continue
            if arr[next_x][next_y] > arr[now_x][now_y]:
                visited[next_x][next_y] = 1
                dfs(next_x, next_y, weight + arr[next_x][next_y] - arr[now_x][now_y]+1)
                visited[next_x][next_y] = 0
            else :
                visited[next_x][next_y] = 1
                dfs(next_x, next_y, weight+1)
                visited[next_x][next_y] = 0


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]
    visited[0][0] = 1
    result = 999999
    dfs(0,0,0)
    print(f"#{test_case} {result}")
