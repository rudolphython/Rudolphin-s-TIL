N, K = map(int, input().split()) # N은 학생 수, K는 방에 들어갈 수 있는 수
room = {11:0, 10:0, 21:0, 20:0, 31:0, 30:0, 41:0, 40:0, 51:0, 50:0, 61:0, 60:0}
for i in range(N):
    S, Y = map(int, input().split()) # S는 성별, Y는 학년
    if Y == 1:
        if S == 1:
            room[11] += 1
        elif S == 0:
            room[10] += 1
    elif Y == 2:
        if S == 1:
            room[21] += 1
        elif S == 0:
            room[20] += 1
    elif Y == 3:
        if S == 1:
            room[31] += 1
        elif S == 0:
            room[30] += 1
    elif Y == 4:
        if S == 1:
            room[41] += 1
        elif S == 0:
            room[40] += 1
    elif Y == 5:
        if S == 1:
            room[51] += 1
        elif S == 0:
            room[50] += 1
    elif Y == 6:
        if S == 1:
            room[61] += 1
        elif S == 0:
            room[60] += 1

check = 0
for v in room.values():
    check += v % 2
    check += v // 2


print(check)