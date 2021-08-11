# 달팽이 (SWEA)


T = 10

for test_case in range(1, T+1):
    N = int(input())
    # 오른쪽, 아래쪽, 왼쪽, 위쪽
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    table = [[0]*(N) for _ in range(N)]

    x, y = 0, 0 # 초기값 설정
    my_way = 0 # 0은 오른쪽, 1은 아래, 2는 왼쪽, 3은 위로

    for i in range(1, N*N+1): #일단 0,0부터 출발하기
        table[x][y] = i
        x += dx[my_way]
        y += dy[my_way]

        if x<0 or y<0 or x>=N or y>=N or table[x][y] !=0:  # 범위를 벗어나면 한 칸 뒤로
            x -= dx[my_way]
            y -= dy[my_way]
            my_way = (my_way + 1) % 4 # 한칸 뒤로 간다음 방향 바꾸기
            x += dx[my_way]
            y += dy[my_way]

    print(f"#{test_case}")
    for i in table:
        print(*i)
