def calc(now):
    global count
    if N >= now: # 배열 저장이므로 배열 크기 준수!
        calc(now * 2) # 왼쪽 노드는 현재 인덱스의 2배
        tree[now] = count # 현재 노드에다가 값 넣기
        count += 1 # 넣었으니 카운트 증가
        calc(now * 2 + 1) # 오른쪽 노드는 현재 인덱스의 2배 + 1


T = int(input())
for testcase in range(1, T + 1):
    N = int(input())
    tree = [0] * (N + 1)
    count = 1
    calc(1)
    print(f'#{testcase} {tree[1]} {tree[N // 2]}')
