## 반복, 조건문 문제 풀이

```py
# 1. 별 만들기

a, b = 5, 3

for i in range(a):
        print('*' * b)
print()


# 2. SWEA 6249

num = int(input("Enter your num: "))

my_list = [0] * 10
result = ''

for i in range(10):
    print(i, end=' ')

print('\n')

while num:
    my_list[num % 10] += 1
    num //= 10

for aa in my_list:
    print(aa, end = ' ')

# SWEA 2019
num = int(input("Enter your num: "))
a = 1

for i in range(0, num + 1, 1):
    a = 2 ** i
    print(a, end=" ")    


# 피보나치 수열 함수 만들기

a = int(input("Enter your name: "))

def calc_fibo(a):
    my_list = []
    for i in range(a):
        if i < 3:
            my_list.append(1)
        elif i >= 3:
            my_list.append(my_list[i-1] + my_list[i-2])
    print(my_list)

calc_fibo(a)
```
