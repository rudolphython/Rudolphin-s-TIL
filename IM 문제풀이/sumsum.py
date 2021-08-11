# list 2일차 sum (SWEA)


for test_case in range(1, 11):
    text_number = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    row_list = []
    column_list = []
    diagonal_list = []

    for x in range(100):
        row_sum = 0
        column_sum = 0
        for y in range(100):
            row_sum += arr[x][y]
            column_sum += arr[y][x]
        row_list.append(row_sum)
        column_list.append(column_sum)

    diagonal_sum = 0
    for x in range(100):
        for y in range(100):
            if x == y:
                diagonal_sum += arr[x][y]

    x = 0
    y = 99
    diagonal_sum_reverse = 0
    while x <= 99:
        diagonal_sum_reverse += arr[x][y]
        x += 1
        y -= 1

    dia_list = [diagonal_sum, diagonal_sum_reverse]
    result_list = dia_list + row_list + column_list

    max = 0
    for i in range(len(result_list)):
        if max < result_list[i]:
            max = result_list[i]

    print(f"#{test_case} {max}")






