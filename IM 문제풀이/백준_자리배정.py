col, row = map(int, input().split())
target = int(input())
arr = [[0]*col for _ in range(row)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

x, y = row, 0
cnt = 1

k = 0

while cnt <= row * col:
    di = x + dx[k]
    dj = y + dy[k]
    if di >= 0 and dj >= 0 and di < row and dj < col and arr[di][dj] == 0:
        arr[di][dj] = cnt
        cnt += 1
        x, y = di, dj

    else :
        k = (k + 1) % 4

result = 0
for i in range(len(arr)):
    for j in range(len(arr[i])):
        if arr[i][j] == target:
            result += 1
            print(j + 1,row - i)

if result == 0:
    print(0)







