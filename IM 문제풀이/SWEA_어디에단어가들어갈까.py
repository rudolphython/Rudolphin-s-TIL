T = int(input())

for test_case in range(1, T + 1):
    N, K = map(int, input().split())  # N은 테이블의 row, column 값(5이상 15이하) / K는 단어 길이(2이상 N이하)
    arr = [list(map(int, (input()).split())) for _ in range(N)]

    # 행 따로, 열 따로 계산해야 할듯
    # x에서는 1의 연속이 K만큼
    # y에서는 1의 연속이 K만큼
    result = 0
    for i in range(N):
        row_result = 0
        column_result = 0
        for j in range(N):
            if arr[i][j] == 1:
                row_result += 1
            else:
                if row_result == K:
                    result += 1
                row_result = 0
            # 3이 된다면 result에 1을 넣어줌. 1을 못 만난다면 초기화해야함.

            if arr[j][i] == 1:
                column_result += 1
            else:
                if column_result == K:
                    result += 1
                column_result = 0

        if j == N - 1:  # j가 끝에 다오면 그냥 result 계산 값이 3이면 최종 값 증가시켜주기
            if column_result == K:
                result += 1
            if row_result == K:
                result += 1

    print(f"#{test_case} {result}")