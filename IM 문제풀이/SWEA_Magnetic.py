T = 10

for test_case in range(1, 11):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    count = 0
    for j in range(100):
        state = 0
        for i in range(100):
            if arr[i][j] == 1 and state == 0:
                state = 1
            elif arr[i][j] == 2 and state == 1:
                state = 0
                count += 1

    print(f"#{test_case} {count}")