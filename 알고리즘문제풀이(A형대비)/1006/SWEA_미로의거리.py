'''
꼼꼼하게 반복하고, 3번 풀고, 버리자!
문제 유형: DFS, BFS -> 큐를 활용해서 문제 풀기
문제 요약: 출발지가 주어지고 목적지를 찾을 때, 이동 칸 수를 도출
풀이 전략:
    1. 연결구조 생성
    2. 큐 생성
    3. 시작점 세팅
    4. now 계산
    5. 유망성 확인
    6. 조건을 통한 next 확인
'''
import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T+1):
    # 1. 연결구조 생성
    N = int(input())
    arr = [list(map(int, input().rstrip())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]

    # 2. q
    q = []

    # 3. 시작점 세팅
    for row in range(N):
        for col in range(N):
            if arr[row][col] == 2:
                start_x = row
                start_y = col
                q.append([row, col])
                visited[row][col] = 1

    # 4. now 계산 및 종료조건 확인
    result = 0 # 도착하면 카운팅
    while len(q) > 0:
        now = q.pop(0)
        now_x = now[0]
        now_y = now[1]
        if arr[now_x][now_y] == 3:
            result += 1
            check = visited[now_x][now_y]


        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        for i in range(4):
            next_x = now_x + dx[i]
            next_y = now_y + dy[i]
            # 조건 확인(범위를 벗어날 때, 벽을 만날 때, 방문한 곳일 때)
            if next_x < 0 or next_y < 0 or next_x >= N or next_y >= N:
                continue
            if arr[next_x][next_y] == 1:
                continue
            if visited[next_x][next_y] != 0:
                continue
            visited[next_x][next_y] = visited[now_x][now_y] + 1 # 중요! 이동 횟수 카운팅 작업!
            q.append([next_x,next_y])


    if result >= 1:
        result = 1
        check -= 2
        print(f"#{test_case} {check}")
    else :
        result = 0
        print(f"#{test_case} 0")




