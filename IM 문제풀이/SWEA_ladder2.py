def calc_goal(j):
    x = 0
    y = j
    count = 0
    while x < 99:
        x += 1
        count += 1

        if ladder[x][y - 1] == 1 and y > 0:
            while ladder[x][y - 1] == 1 and y > 0:
                y -= 1
                count += 1

        elif y < 99 and ladder[x][y + 1] == 1:
            while y < 99 and ladder[x][y + 1] == 1:
                y += 1
                count += 1

    return count


T = 10

for test_case in range(1, T + 1):
    tc = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]

    start = []
    for i in range(100):
        if ladder[0][i] == 1:
            start.append(i)

    result = []
    minI = 100000000000
    for j in start:
        if calc_goal(j) < minI:
            minI = calc_goal(j)
            minIndex = j

    print(f"#{test_case} {minIndex}")