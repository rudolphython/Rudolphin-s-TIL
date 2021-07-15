## 0716 내장함수, 리스트 문제풀이

# python
```
# 내장함수 연습문제 1
import datetime

name = input("Enter your name: ")
age = int(input("Enter your age: "))
t_age = 100 - age

calc_age = datetime.datetime.now().year + t_age
print(calc_age)

# 내장함수 연습문제 4
list_a = "ADCBBBBCABBCBDACBDCAACDDDCAABABDBCBCBDBDBDDABBAAAAAAADADBDBCBDABADCADC"
str_list = list_a
# 일단 모두 리스트로 변환
calc_list = list(map(lambda x: ord('E') - ord(x), str_list))
print(sum(calc_list))

# 내장함수 연습문제 5
def sum_list(*a):
    result = 1
    for i in a:
        if type(a) != int:
            print("에러발생")
            return
        result *= i
    print(result)

sum_list(1, 2)

# 내장함수 연습문제 6
num = int(input("Enter your num: "))
print("ASCII %d => %s" %(num, chr(num)))

# 내장함수 연습문제 7
calc_num = list(filter(lambda x : x % 2 == 0, range(1, 11,1)))
print(calc_num)

# 내장함수 연습문제 8
calc_list = list(map(lambda x: x**2, range(1, 11, 1)))
print(calc_list)

# 내장함수 연습문제 9
first_list = list(filter(lambda x: x % 2 == 0, range(1, 11,1)))
second_list = list(map(lambda x: x **2, first_list))
print(second_list)

# 내장함수 연습문제 10
list = [3, 5, 4, 1, 8, 10, 2]
def calc_max(*list):
    max_num = max(list)
    return max_num

print(calc_max(*list))


# 내장함수 연습문제 11
# zip() 함수 : 합치는 것. 예시: zip(numbers, letters)
# items() 함수 : 키-값을 쌍으로 한꺼번에 뽑아내는 함수
t_str = "abcdef"
t_list = [0, 1, 2, 3, 4, 5]
t_dict = dict(zip(t_str, t_list))
for key, val in t_dict.items():
    print(key, val)

# 리스트와 튜플 연습문제 1
scores = [{90, 80}, {85, 75}, {90, 100}]
print(sum(scores[0]))
print((sum(scores[0]) / 2))

# 리스트와 튜플 연습문제 2
my_list = 'Python is powerful... and fast; plays well with others; runs everywhere; is friendly & easy to learn; is Open.'
chk_list = 'aeiou'
final_list = [i for i in my_list if i not in chk_list]
print("".join(final_list))

# 리스트와 튜플 연습문제 3
result_list = []
for i in range(2, 10):
   temp_list = []
   for j in range(1, 10):
      t = i*j
      #3의 배수이거나 7의 배수라면 continue. 즉, 아래 코드로 진행(3과 7의 배수는 appped하지 않겠다라는 뜻)
      if not (t % 3) or not (t % 7):
      #3의 배수도 아니고 7의 배수도 아니면 참. 즉, continue 됨.
         continue
      temp_list.append(t)
   result_list.append(temp_list)
print(result_list)

# 리스트와 튜플 연습문제 4
list = [int(input("숫자를 입력하세요: ")) for i in range(5)]

print(sum(list) / 5)

# 리스트와 튜플 연습문제 5
num = int(input("숫자를 입력하세요: "))
list = []
for i in range(1, num + 1):
    if num % i == 0:
        list.append(i)
print(list)

# 리스트와 튜플 연습문제 8
list = [1, 3, 11, 15, 23, 28, 37, 52, 85, 100]
new_list = [i for i in list if i % 2 == 0]
print(new_list)

# 리스트와 튜플 연습문제 11
def fibo(x):
    if x == 1  or x ==2:
        return 1
    elif x > 2:
        return fibo(x-2) + fibo(x-1)

result = [fibo(x) for x in range(1,11,1)]
print(result)

# 리스트와 튜플 연습문제 13
a = input("숫자를 입력하시오: ")
tot = 0
for i in a:
    tot = tot + int(i)
print(tot)

# 리스트와 튜플 연습문제 16
a = input("숫자를 입력하시오: ")
b_list = list(map(int, a.split(',')))
b_tuple = tuple(map(int, a.split(',')))
print(b_list)
print(b_tuple)

# 리스트와 튜플 연습문제 19
list = input("Enter your word: ")
list = list.split(',')
new_list = sorted(list)
final_list = ','.join(new_list)
print(final_list)

# 리스트와 튜플 연습문제 20
a = input("숫자를 입력하시오: ")
a_list = list(map(int, a.split(',')))
# split() 함수는 문자열을 분리할 때 사용함.
result = [i for i in a_list if i & 1]
print(','.join(map(str, result)))

# 리스트와 튜플 연습문제 24
list = [5, 6, 77, 45, 22, 12, 24]
new_list = [i for i in list if i % 2 == 0]
print(new_list)

# 리스트와 튜플 연습문제 25
list = [12, 24, 35, 70, 88, 120, 155]
new_list = [x for i, x in enumerate(list) if i % 2 == 0]
print(new_list)

# 리스트와 튜플 연습문제 26
a = [1,3,6,78,35,55]
b = [12,24,35,24,88,120,155]

for i in range(0, len(a)):
    if a[i] in b:
        print(a[i])

```