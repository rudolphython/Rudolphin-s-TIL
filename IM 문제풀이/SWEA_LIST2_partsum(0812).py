# SWEA 문제 (부분합 응용)

T = int(input())

for test_case in range(1, T+1):
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    N, K = map(int, input().split())

    # N은 부분집합 원소의 수
    # K는 부분집합의 합
    count = 0
    for i in range(1<<12):
        test_list = []
        test_sum = 0
        for j in range(12):
            if i & (1<<j):
                test_list.append(arr[j])
                test_sum += arr[j]

        if len(test_list) == N and test_sum == K:
            count += 1

    print(f"#{test_case} {count}")




