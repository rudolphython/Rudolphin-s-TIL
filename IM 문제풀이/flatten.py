# SWEA1208 문제풀이 flatten

T = 10

for test_case in range(1, T+1):
    dump = int(input())
    builds = list(map(int, (input()).split()))

    for d in range(dump +1):
        my_max = 0 # max 값 초기화
        my_min = 100 # min 값 초기화
        # max_h = 0 # max의 index 초기화
        # min_h = 0 # min의 index 초기화
        for i in range(len(builds)): #최대, 최소 구하기
            if builds[i] > my_max:
                my_max = builds[i]
                max_h = i #최대값의 인덱스 구하기
                continue

        for j in range(len(builds)):
            if builds[j] < my_min:
                my_min = builds[j]
                min_h = j

            # elif builds[i] <= my_min:
            #     my_min = builds[i]
            #     min_h = i #최소값의 인덱스 구하기
        builds[max_h] -= 1 # 최대값에는 1을 빼고
        builds[min_h] += 1 # 최소값에는 1을 더하기

    result = my_max - my_min # 차이 구하기
    print(f"#{test_case} {result}")

