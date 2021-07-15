## 7월 6일 문제 풀이
# python

```

# 연산자 연습문제 5
a = 0.2 * 100
b = 100 + 200
c = a / b * 100
print("혼합된 소금물의 농도: {0:0.2f}%".format(c))

# 흐름제어 연습문제 2
a = int(input("입력: "))
count = 0
for i in range(1, a + 1):
    if a % i == 0:
        count = count + 1
        if count == 2:
            print("%d(은)는 1과 %d로만 나눌 수 있는 소수입니다." % (a, a))

# 흐름제어 연습문제 5
a = str(input("입력: "))
if a.islower():
    print(a, a.upper(), ord(a), ord(a.upper()))

# 흐름제어 연습문제 6
result = ""
for i in range(1, 201):
    if i % 5 == 0:
        result = result + " %d" % i
print(result)

# 흐름제어 연습문제 7
result = ""
for i in range(1, 201):
    if i % 5 == 0:
        result = result + "%d," % i 
print(result[:-1])

# 반복문 연습문제 1
list = [88, 30, 75]
for i in list:
    if i >= 60:
        print("합격입니다.")
    elif i <= 60:
        print("불합격입니다.")

# 반복문 연습문제 4
result = ""
for i in range(1, 101):
    if i % 2 == 1:
        result =  result + "%d," % i 
print(result[:-1])

# 반복문 연습문제 7
i = 0
tot = 0
scores = [85, 65, 77, 83, 75, 22, 98, 88, 38, 100]
sc_len = len(scores)

while i < sc_len:
    NSC = scores.pop()
    if NSC >= 80:
        tot = tot + NSC
    i = i + 1 
print(tot)

#반복문 연습문제 10
array = [0]*10
num = int(input("입력: "))
result = ""
#num이 0이 될때까지 반복하며 숫자체크
while num:
    array[num % 10] += 1
    num //= 10
for i in range(0, 10):
    result += "%d " % i
print(result)
result = ""
for i in range(0, 10):
    result += "%d " % array[i]
print(result)

# 반복문 연습문제 14
num = int(input("입력: "))
print(format(num,'b'))

# 함수 1
a = str(input("입력: "))

def ch_word():
    ch_word = a[: :-1]
    return ch_word

print(ch_word())

# 함수 연습문제 2
a = int(input("입력: "))

def dec():
    cou = 0
    for i in range(1, a + 1):
        if a % i == 0:
            cou = cou + 1
            if cou == 2:
                print("소수")

print(dec())

# 함수 연습문제 3
a = int(input("입력: "))
arr = []
for i in range(a):
    if i < 2:
        arr.append(1)
    else : 
        arr.append(arr[i-1] + arr[i-2])
print(arr)

# 함수 연습문제 5
list = [1, 2, 3, 4, 3, 2, 1]
print(list)

def new_list(list):
    my_list = set(list)
    list = my_list
    return list

print(new_list(list))

# 함수 연습문제 6
list = [2, 4, 6, 8, 10]
a = input("입력: ")

def check_list(list):
    if a in list:
        print("true")
    else :
        print("false")

print(check_list(list))

# 함수 연습문제 7
a = int(input("입력: "))

def fatorial(a):
    fat = 1
    for i in range(1, a + 1):
        fat = i * fat
    return fat

# print(fatorial(a)) 

#함수 연습문제 8
def square(k):
    print("squares(%d) => %d" % (int(k), int(k)**2))

k = input()
k = k.split(',')
for i in k:
    square(i)

# 함수 연습문제 9
def chk_word(a):
    if len(a[0]) > len(a[1]):
        print(a[0])
    else :
        print(a[1])

a = str(input("입력: "))
a = a.split(',')
chk_word(a)

# 내장함수 연습문제 1
import datetime
name = input("이름을 입력하시오.: ")
t = 100 - int(input("나이를 입력하시오.: "))
#채점표가 2019년으로 되어있으므로 -1년 (현재 2020년) + 100-현재나이
year = datetime.datetime.now().year -2 + t
print("%s(은)는 %d년에 100세가 될 것입니다." % (name, year))

# 내장함수 연습문제 4
t_str = "ADCBBBBCABBCBDACBDCAACDDDCAABABDBCBCBDBDBDDABBAAAAAAADADBDBCBDABADCADC"
str_list = list(t_str)
t = list(map(lambda c : ord('E') - ord(c) , str_list))
print(sum(t))

# 내장함수 연습문제 5
def multiplication(*param):
   result = 1
   for i in param:
      if type(i) != int:
         print("에러발생")
         return
      result *= i
   print(result)
      
multiplication(1, 2, '4', 3)

# 내장함수 연습문제 6
a = int(input("입력: "))
print("ASCII %d => %s" %(a, chr(a)))

#  내장함수 연습문제 7
a = [1, 2 ,3, 4, 5, 6, 7, 8, 9, 10]
f = list(filter(lambda x :  x % 2 == 0, a))
print(f)

# 내장함수 연습문제 8
a = [1, 2 ,3, 4, 5, 6, 7, 8, 9, 10]
b = list(map(lambda x : x * x, a))
print(b)

# 내장함수 연습문제 9 
a = [1, 2 ,3, 4, 5, 6, 7, 8, 9, 10]
f = list(filter(lambda x :  x % 2 == 0, a))
s = list(map(lambda x : x * x, f))
print(s)

# 내장함수 연습문제 10
param = (3, 5, 4, 1, 8, 10, 2)
def calc_max(*param): 
    print("max{0} => {1}".format(param, max(param)))

calc_max(*param)

# 내장함수 연습문제 11
a = "abcdef"
b = [0, 1, 2, 3, 4, 5]
c = dict(zip(a, b))
for key, val in c.items():
    print("%s : %d" % (key, val))

```