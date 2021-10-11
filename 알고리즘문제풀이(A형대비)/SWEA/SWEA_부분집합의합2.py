def dfs(now, my_sum, count):
    global result
    if count == N and my_sum == K:
        result = 1


    if now < 20 and my_sum + my_list[now] <= K and count + 1 <= N:
        dfs(now + 1, my_sum + my_list[now], count + 1)
        dfs(now + 1, my_sum, count)




T = int(input())

for test_case in range(1, T + 1):
    N, K = map(int, input().split())    # N은 쓰이는 숫자, K는 부분집합의 합
    result = 0
    my_list = [i for i in range(1, 21)]
    dfs(0, 0, 0)
    print(result)