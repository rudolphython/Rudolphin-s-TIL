T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())    # N은 이중리스트의 크기(N x N), M은 파리채의 크기(M * M)
    my_list = [list(map(int, input().split())) for _ in range(N)]

    result = []
    for x in range(N-(M-1)):
        for y in range(N-(M-1)):
            my_sum = 0
            for i in range(x, x+M):
                for j in range(y, y+M):
                    my_sum += my_list[i][j]
            result.append(my_sum)

    print(max(result))


