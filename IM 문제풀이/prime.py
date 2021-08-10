# SWEA1945 문제풀이 간단한 소수인수분해

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    count2 = 0
    count3 = 0
    count5 = 0
    count7 = 0
    count11 = 0
    while N >= 2:
        if N % 2 == 0:
            N //= 2
            count2 += 1
        else :
            break
    while N >= 2:
        if N % 3 == 0:
            N //= 3
            count3 += 1
        else :
            break
    while N >= 2:
        if N % 5 == 0:
            N //= 5
            count5 += 1
        else :
            break
    while N >= 2:
        if N % 7 == 0:
            N //= 7
            count7 += 1
        else :
            break
    while N >= 2:
        if N % 11 == 0:
            N //= 11
            count11 += 1
        else :
            break
    print(f'#{test_case} {count2} {count3} {count5} {count7} {count11}')
