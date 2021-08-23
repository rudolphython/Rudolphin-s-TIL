T = int(input())

for test_case in range(1, T+1):
    N, K = map(int, input().split())    # N은 총원 수, K는 제출한 사람 수
    good = list(map(int, input().split()))  # good은 과제를 낸 사람 수

    normal = []
    for i in range(1, N+1):
        normal.append(i)

    for j in good:
        if j in normal:
            normal.remove(j)

    print(f"#{test_case}", end = " ")
    print(*normal)


