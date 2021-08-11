# 부분합 (SWEA)


T = 10

for test_case in range(1, T+1):
    N = int(input())
    arr = list(map(int, (input()).split()))
    count = 0
    my_list = []

    for i in range(1<<N):
        check = 0
        for j in range(N):
            if i & (1<<j):
                check += arr[j]
        if check == 0:
            count += 1

    print(f"#{test_case} {count}")