def bingo(arr):
    result = 0
    for i in range(5):
        if arr[i] == [1, 1, 1, 1, 1]:
            result += 1

    for i in range(5):
        count = 0
        for j in range(5):
            if arr[j][i] == 1:
                count += 1
        if count == 5:
            result += 1

    count = 0
    for i in range(5):
        for j in range(5):
            if i == j and arr[i][j] == 1:
                count += 1
    if count == 5:
        result += 1

    count = 0
    for i in range(5):
        for j in range(5):
            if i + j == 4 and arr[i][j] == 1:
                count += 1
    if count == 5:
        result += 1

    if result >= 3:
        total = 1
        return total

me = [list(map(int, input().split())) for _ in range(5)]
mc = [list(map(int, input().split())) for _ in range(5)]
arr = [[0]*5 for _ in range(5)]

order = []
for i in range(5):
    for j in range(5):
        order.append(mc[i][j])
final = []
for a in range(len(order)):
    for i in range(5):
        for j in range(5):
            if me[i][j] == order[a]:
                arr[i][j] = 1
                result = bingo(arr)
                if result == 1:
                    final.append(a+1)

print(final[0])



