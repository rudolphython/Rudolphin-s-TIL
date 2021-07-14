## 문자열, 셋과 딕셔너리, 함수 연습문제(반복)

# python

```
# 문자열 연습문제 1
a = input("Enter your word: ")
print(a[::-1])
print("입력하신 단어는 회문(Palindrome)입니다.")

# 문자열 연습문제 2
a = input("Enter your sentence: ")
list_a = a.split(" ")
reverse_a = list_a[::-1]
result = ""
for i in range(0, len(reverse_a)):
    print(reverse_a[i], end = " ")

# 문자열 연습문제 3
a = input("Enter your URL: ")
prt = a.find("http")
print("protocol: %s" % (a[0 : 4]))
www = a.find("www")
com = a.find("com")
print("host: %s" % (a[www : com + 3]))
print("others: %s" % (a[com + 5: ]) )

# 문자열 연습문제 4
while True:
    a = input("Enter your sentence: ")
    if not a:
        break
    print(">> {0}".format(a.upper()))

# 문자열 연습문제 5
a = input("Enter your sentence: ")
list_a = a.split(" ")
set_a = set(list_a)
list_t = list(map(str, set_a))
result = ""
for i in range(0, len(list_t)):
    result += list_t[i] + ","
print(result[:-1])

# 문자열 연습문제 7
a = input("Enter your sentence: ")
temp = [i for index ,i in enumerate(a) if not (index & 1) ]
#조인기능으로 합쳐서 출력
print("".join(temp))

# 셋과 딕셔너리 연습문제 4
a = {'아메리카노': 1900, '카페모카': 3300, '에스프레소': 1900, '카페라떼': 2500, '카푸치노': 2500, '바닐라라떼': 2900}
b = {'헤이즐럿라떼': 2900, '카페모카': 3300, '밀크커피': 3300, '아메리카노': 1900, '샷크린티라떼': 3300}
#중복일 경우 a의 값으로 변경
b.update(a)
#필터로 벨류값이 3000이상인 값만 가져온다. 출력 예시가 dict->set이므로 set으로 변경해준다.
result = set(filter(lambda item: item[1] >= 3000, b.items()))
print(result)

# 셋과 딕셔너리 연습문제 5
fruit = ['   apple    ','banana','  melon']
dic = {fruit[i].strip() : len(fruit[i].strip()) for i in range(len(fruit))}
print(dic)

# 셋과 딕셔너리 연습문제 6 
a = int(input("Enter your number: "))
dic = {i : i ** 2 for i in range(1, a + 1)}
print(dic)

# 셋과 딕셔너리 연습문제 7
t_str = input().strip()
l_count = d_count = 0
for t in t_str:
   #문자일때
   if 'a' <= t <= 'z' or 'A' <= t <= 'Z':
      l_count += 1
   #숫자일때
   elif '0' <= t <='9':
      d_count += 1
 
print("LETTERS %d" % l_count)
print("DIGITS %d" % d_count)

# 셋과 딕셔너리 연습문제 8
t_str = input().strip()
u_count = l_count = 0
for t in t_str:
   #소문자일때
   if 'a' <= t <= 'z':
      l_count += 1
   #대문자일때
   elif 'A' <= t <= 'Z':
      u_count += 1
 
print("UPPER CASE %d" % u_count)
print("LOWER CASE %d" % l_count)

# 셋과 딕셔너리 연습문제 9
beer = {'하이트': 2000, '카스': 2100, '칭따오': 2500, '하이네켄': 4000, '버드와이저': 500}
new_beer = {item[0] : item[1] * 1.05 for item in beer.items()}
print(new_beer)

# 흐름과 제어 연습문제 1
a = int(input("입력: "))
count = 0

for i in range(1, a + 1):
    if a % i == 0:
        print(i)
        count +=1
        if count == 2:
            print("소수입니다.")

# 흐름과 제어 연습문제 3
a = (input("입력: "))
if a.islower():
    print(a.upper())
elif a.isupper():
    print(a.lower())

# 흐름과 제어 연습문제 4
a = (input("입력: "))

if a.islower():
    print(a.upper())
    print(ord(a.upper()))
elif a.isupper():
    print(a.lower())
    print(ord(a.lower()))

# 흐름과 제어 연습문제 5
result = ''
for i in range(1, 201):
    if i % 5 != 0 and i % 7 == 0:
        result += ",%d" % i
print(result[1:len(result)])

# 반복문 연습문제 몇 번이였지?
result = ""
for i in range(1, 101):
    if i % 2 == 0:
        result += "%d " % i
print(result)

# 반복문 연습문제 10
i = 7 
n = 0
while i > 0 and n <= 4:
    print(" "*n, "*"*i)
    i -= 2
    n += 1

# 반복문 연습문제 10
arr = [0]*10
a = int(input("Enter your num: "))
result = ""
for i in range(0, 10):
    result += "%d " % i
print(result)
result = ""
while a != 0:
    arr[a % 10] += 1
    a //= 10
for i in range(0, 10):
    result += "%d " % arr[i]
print(result)

# 함수 연습문제 3
a = int(input("Enter your number: "))


def calc_num():
    count = 0
    for i in range(1, a + 1):
        if a % i == 0:
            count += 1
        if count == 2:
            my_num = "소수입니다."
            return my_num 

print(calc_num())

# 함수 연습문제 4
a = int(input("Enter your number: "))

def calc_fibo():
    arr = [1] * a
    for i in range(2, a):
        arr[i] = arr[i-2] + arr[i-1]
    return arr

print(calc_fibo())


# 함수 연습문제 5
list = [1, 2, 3, 4, 3, 2, 1]
set_list = set(list)
print(set_list)

# 함수 연습문제 7
a = int(input("숫자를 입력하시오." ))

def calc_factorial():
    factorial = 1
    for i in range(1, a + 1):
        factorial *= i
    return factorial

print(calc_factorial())

# 함수 연습문제 8
def square(a):
    print(int(a)**2)

a = input("숫자를 입력하시오.: " )
a = a.split(',')

for i in a:
    square(i)

```