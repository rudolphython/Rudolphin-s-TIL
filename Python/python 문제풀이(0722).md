## 0722 문제 풀이

```py
# 내장함수 연습문제 5
def calc_num(*params):
    total = 1
    for num in params:
        total *= num
    print(total)

calc_num(1, 2, 3, 4)

# 내장함수 연습문제 6
a = int(input("Enter your number: "))
print(chr(a))

# 리스트 연습문제 1
scores = [(90, 80),  (85, 75), (90, 100)]
print(sum(scores[0]))

# 리스트 연습문제 13
a = input("Enter your number: ")
tot = 0
for i in a:
    tot += int(i)
print(tot)

# SWEA 1970 쉬운 거스름돈

T = int(input("테스트 케이스 입력: "))

for tc in range(1, T + 1):
    N = int(input("거슬러야 할 금액 입력: "))
    money_list = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    my_list = [0] * 8
    for i in range(0, 8, 1):
        if N // money_list[i] != 0:
            my_list[i] = N // money_list[i]
            N = N % money_list[i]
    result = ''
    for i in range(8):
        result += "%d " % my_list[i]
    print(f'#{tc}')
    print(result)

# 흐름제어 연습문제 1
a = int(input("숫자를 입력하시오: "))

for i in range(1, a+1):
    if a % i == 0:
        print(f'{i}은 {a}의 약수입니다.')

# 흐름제어 연습문제 7
result = ''
for i in range(1, 201, 1):
    if i % 7 == 0 and i % 5 != 0:
        result += "%d," % i

print(result[:-1])

# 반복문 연습문제 4
result = ''
for i in range(1, 100, 2):
    result += "%d, " % i

print(result[:-2])

# 반복문 연습문제 6
my_list = ['A', 'A', 'A', 'O', 'B', 'B', 'O', 'AB', 'AB', 'O']
a_count = my_list.count('A')
print(a_count)

# 반복문 연습문제 7
count = 5
while count > 0:
    print('*' * count)
    count -= 1

# 반복문 연습문제 10
a = int(input("숫자를 입력하세요: "))
result = ''
for i in range(0, 10, 1):
    result += '%d ' % i
print(result)

list1 = [0] * 10
result =''
while a != 0:
    list1[a % 10] += 1
    a //= 10

for i in range(10):
    result += '%d ' % list1[i]
print(result)


# 함수 연습문제 4
def fibo(n):
    if n <= 1:
        return 1
    else :
        return fibo(n-1) + fibo(n-2)

print(fibo(9))

# 함수 연습문제 5
list1 = [1, 2, 3, 4, 3, 2, 1]
list2 = set(list1)
print(list(list2))

# 함수 연습문제 7
def fact(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

print(fact(5))

# 함수 연습문제 8
print(pow(2, 2))

# 내장함수 연습문제 4
list1 = "ADCBBBBCABBCBDACBDCAACDDDCAABABDBCBCBDBDBDDABBAAAAAAADADBDBCBDABADCADC"
result = 0
list2 = (list(map(lambda x : ord('E') - ord(x), list1))) 
print(sum(list2))

# 내장함수 연습문제 5
def my_calc(*params):
    result = 1
    for param in params:
        result *= param
    return result

print(my_calc(1, 2, 3))

# 내장함수 연습문제 7
list1 = [1, 2, 3, 4, 5, 6]
list2 = list(map(lambda x : x ** 2, list1))
print(list2)

# 내장함수 연습문제 9
list1 = [1, 2, 3, 4, 5, 6]
list2 = list(filter(lambda x : x % 2 == 0, list1))
list3 = list(map(lambda x : x ** 2, list2))
print(list3)

# 내장함수 연습문제 11
a_str = 'abcdef'
for idx, val in enumerate(a_str):
    print(f'{val}: {idx}')

# 리스트 연습문제 2
alps = list('Pythn s pwrfl... nd fst; plys wll wth thrs; rns vrywhr; s frndly & sy t lrn; s Opn.')
list2 = list('aeiou')
for alp in alps:
    if alp in list2:
        alps.remove(alp)
result =''
for alp in alps:
    result += '%s' % alp

print(result)

# 리스트 연습문제 6
num = int(input("숫자를 입력하시오: "))
list1 = []
for i in range(1, num + 1):
    if num % i == 0:
        list1.append(i)

print(list1)\

# 리스트 연습문제 13
a = str(input("숫자를 입력하시오: "))
result = 0
for i in a:
    result += int(i)

print(result)

# 리스트 연습문제 19
a = ['python', 'hello', 'world', 'hi']
new_a = sorted(a)
print(new_a)

# 리스트 연습문제 22
numbers = [5, 6, 77, 45, 22, 12, 24]
for number in numbers:
    if number % 2 == 0:
        numbers.remove(number)

print(numbers)

# 리스트 연습문제 26
list1 = [1,3,6,78,35,55]
list2 = [12,24,35,24,88,120,155]
result = []
for a in list1:
    if a in list2:
        result.append(a)

print(result)
```




