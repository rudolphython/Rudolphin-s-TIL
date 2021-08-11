# 델타검색 응용(SWEA)

T = 10

for test_case in range(1, T+1):
    N = int(input())
    arr = [list(map(int, (input()).split())) for _ in range(N)]

    dx = [-2, -1, -2, -1, 1, 2, 1, 2]
    dy = [-1, -2, 1, 2, -2, -1, 2, 1]
    total = 0
    for x in range(len(arr)):
        for y in range(len(arr[x])):
            for t in range(8):
                nx = x + dx[t]
                ny = y + dy[t]
                if 0 <= nx < len(arr) and 0 <= ny < len(arr[x]):
                    me = arr[x][y]
                    others = arr[nx][ny]

                    if me > others:
                        my_sum = me - others
                    else :
                        my_sum = others - me

                    total += my_sum

    print(f"#{test_case} {total}")