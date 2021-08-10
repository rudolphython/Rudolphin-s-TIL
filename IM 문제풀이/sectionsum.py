# SWEA12459 문제풀이 구간합

T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, (input()).split())
    my_list = list(map(int, (input()).split()))

    len = N - M + 1
    # 무조건 len은 전체 길이에서 구간만큼 빼고 1 더해야 함.
    # 만약 5개 길이고 3개 구간이면 123. 234, 345 총 케이슨느 3개이니까
    result = [0]*len
    # 결과 리스트는 어차피 len만큼만 생기니 초기화(append)쓰지말자..
    for i in range(len):
        my_sum = 0
        for j in range(i, i + M):
            my_sum += my_list[j]
        result[i] = my_sum

    max, min = result[0], result[0]
    for i in range(len):
        if max < result[i]:
            max = result[i]
        elif result[i] < min:
            min = result[i]

    my_ans = max - min

    print(f"#{test_case} {my_ans}")

