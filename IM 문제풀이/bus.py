# SWEA12454 문제 풀이 전기버스

T = int(input())
for tc in range(T):
    k, n, m = map(int,input().split())
    chargers = list(map(int,input().split()))

    #일단 N개만큼의 정류정 설립
    li = [0] * n
    for i in range(len(chargers)):
        li[chargers[i]] = 1

    count = 0
    now = 0
    while now + k < n:
        next = now
        for i in range(now + 1,now + k + 1):
            if li[i] == 1:
                next = i
        if next == now:
            break
        now = next
        count += 1
    if now + k >= n:
        print("#{} {}".format(tc + 1, count))
    else:
        print("#{} {}".format(tc + 1, 0))
        # 도착 못했자면





