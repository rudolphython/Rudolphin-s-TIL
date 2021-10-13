T = int(input())


def dfs(x, y, d, cnt):
    global ans
    direction[d] += 1
    nx = x + dx[d]
    ny = y + dy[d]

    if 0 <= nx < N and 0 <= ny < N:
        if d == 3 and (nx, ny) == start:
            ans = max(ans, cnt)
            return
        if mp[nx][ny] not in dessert:
            dessert.append(mp[nx][ny])
            dfs(nx, ny, d, cnt + 1)
            dessert.pop()

    if d < 3 and direction[d] >= 1:
        d += 1
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < N and 0 <= ny < N:
            if d == 3 and (nx, ny) == start:
                ans = max(ans, cnt)
                return

            if mp[nx][ny] not in dessert:
                dessert.append(mp[nx][ny])
                dfs(nx, ny, d, cnt + 1)
                dessert.pop()


for test_case in range(1, T + 1):
    N = int(input())
    mp = [list(map(int, input().split())) for _ in range(N)]
    dx = [1, 1, -1, -1]
    dy = [1, -1, -1, 1]
    ans = 0

    for i in range(N - 2):
        for j in range(1, N - 1):
            start = (i, j)
            dessert = [mp[i][j]]
            direction = [-1, 0, 0, 0]
            dfs(i, j, 0, 1)

    if ans == 0:
        ans = -1
    print(f"#{test_case} {ans}")