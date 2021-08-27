jang = []
for i in range(9):
    nan = int(input())
    jang.append(nan)

jang = sorted(jang)
check = []

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]

result = []
for i in range(1<<len(arr)):
    check = []
    for j in range(len(arr)):
        if i & (1<<j):
            check.append(j)
    if len(check) == 7:
        result.append(check)




for i in range(len(result)):
    sum = 0
    for j in result[i]:
        sum += jang[j]
    if sum == 100:
        final = result[i]

for k in final:
    print(jang[k])
