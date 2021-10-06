'''
꼼꼼하게 반복하고, 3번 풀고, 버리자!
문제 유형: q
문제 요약: q 활용 접근, 리스트 추가 시 조건 적용
풀이 전략: q 구현
'''

import sys
sys.stdin = open("input.txt", "r")

# 인접 리스트로 풀이
from collections import deque

T = int(input())

for test_case in range(1, T + 1):
    V, E = map(int, input().split())
    adj = [list(map(int, input().split())) for _ in range(E)]
    start, end = map(int, input().split())

    adj_list = [[] for _ in range(V + 1)]

    for i in adj:
        adj_list[i[0]].append(i[1])
        adj_list[i[1]].append(i[0])

    q = deque()
    visited = [0] * (V + 1)  # 방문 지점 체크 초기화
    visited[start] = 1  # 처음 방문은 1로 해주고(나중에 1 빼줘야함!)
    q.append(start)  # q에 스타트 넣어주기

    while len(q) > 0:  # q가 비어있지 않을 때만
        now = q.popleft()  # 현재를 빼고
        for next in adj_list[now]:
            if visited[next] != 0:  # 방문했으면 건너 뛰고
                continue
            q.append(next)  # 방문 안했으면 가보고
            visited[next] = visited[now] + 1  # 카운트니까 now에서 1 더해줌

    if visited[end] == 0:
        print(f'#{test_case} 0')
    else:
        print(f'#{test_case} {visited[end] - 1}')