# SWEA 문제(리스트 색칠하기)

T = int(input())

for test_case in range(1, T+1):
    N = int(input())  # 칠할 영역의 갯수
    red_list = []
    blue_list = []
    for i in range(N):
        r1, c1, r2, c2, color = map(int, input().split())

        for x in range(r1, r2+1):
            for y in range(c1, c2+1):
                if color == 1:
                    if [x, y] not in red_list:
                        red_list.append([x, y])
                if color == 2:
                    if [x, y] not in blue_list:
                        blue_list.append([x, y])
    count = 0
    for r in red_list:
        for b in blue_list:
            if r == b:
                count += 1

    print(f"#{test_case} {count}")


