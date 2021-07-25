### SWEA 단계별 문제풀이(월말평가 대비)

```py
# SWEA 2072
my_list = [3, 17, 39, 8, 41, 2, 32, 99, 2]

tot = 0
for i in my_list:
    if i % 2 == 1:
        tot += i
print(tot)

# 백준 2439
a = 5
j = 5
for i in range(0, a + 1, 1):
    print(' ' * (j-i) +'*' * i)

# 백준 2739
for i in range(2, 10):
    for j in range(1, 10):
        print (f'{i} * {j} = {i * j}')

# 백준 2438
n = 5
for i in range(1, n+1, 1):
    print(i*'*')

# 백준 2577
a = 150 * 266 * 427
list1 = [0] * 9

while a != 0:
    list1[a % 10] += 1
    a //= 10

for i in list1:
    print(i)

# 백준 1152
a = 'The Curious Case of Benjamin Button'
print(a.count(" ") + 1)

# 백준 2908
a, b = 734, 893
a, b = str(a), str(b)
r_a = ""
r_b = ""
for i in range(-1, -len(a)-1, -1):
    r_a += a[i]
for i in range(-1, -len(b)-1, -1):
    r_b += b[i]

if int(r_a) > int(r_b):
    print(r_a)
else :
    print(r_b)
```