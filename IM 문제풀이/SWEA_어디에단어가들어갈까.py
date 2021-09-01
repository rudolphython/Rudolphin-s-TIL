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
            else :
                if row_result == 3:
                    result += 1
                row_result = 0


    print(f"#{test_case} {result}")