T = int(input())

for test_case in range(1, T+1):
    N = list(map(int, ' '.join(input()).split()))

    count = [0] * 10
    runn, tri = 0, 0
    for i in N:
        count[i] += 1

    i = 0
    while i < 10:
        if count[i] >= 3:
            count[i] -= 3
            tri += 1
            continue
        if i <= 7:
            if count[i] and count[i + 1] and count[i + 2]:
                runn += 1
                count[i] -= 1
                count[i + 1] -= 1
                count[i + 2] -= 1
                continue
        i += 1

    if tri + runn == 2:
        print(f'#{test_case} Baby Gin')
    else:
        print(f'#{test_case} Lose')

