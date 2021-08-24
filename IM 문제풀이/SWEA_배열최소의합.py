def dfs(row):
    global my_sum, total    # 전역변수 선언

    if row == N: # 종료조건
        if my_sum < total: # 종료될 때마다 total가 비교
            total = my_sum # 한 턴 종료될 때마다 total은 계속 달라짐
        return


    for col in range(N):
        if visited[col] == 1:
            continue
        my_sum += arr[row][col] # sum 합격한 값을 더해주고
        visited[col] = 1 # 썼다고 표시
        dfs(row+1) # 가라
        my_sum -= arr[row][col] # 갔으니까 다시 이전 더한 값 빼주고
        visited[col] = 0 # 초기화



T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0]*N
    my_sum, total = 0, 99999999999

    dfs(0)

    print(f"#{test_case} {total}")