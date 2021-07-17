## 셋과 딕셔너리 연습문제 풀이

# python

```
# 셋과 딕셔너리 연습문제 1

info = {
  "홍길동" : "010-1111-1111",
  "이순신" : "010-1111-2222",
  "강감찬" : "010-1111-3333" 
}

name = input("이름을 입력하세요.: ")
print(f'{name}의 전화번호는 {info[name]}입니다.')

# 셋과 딕셔너리 연습문제 3
import operator

dic = {"TV": "2000000","냉장고": "1500000", "책상": "350000", "노트북": "1200000", "가스레인지": "200000", "세탁기": "1000000"}
# operator.itemgetter(0)으로하면 키를 기준으로 1로하면 값을 기준으로 정렬
# 기본은 오름차순 정렬이므로 내림차순을 하려면 reverse를 True해야한다.
# 이 기능을 사용하기 위해서는 operator 모듈을 import해야한다.
dic = dict(sorted(dic.items(), key=operator.itemgetter(1), reverse=True))
for key, value in dic.items():
   print("{0}: {1}".format(key, value))

셋과 딕셔너리 연습문제 4
a = {'아메리카노': 1900, '카페모카': 3300, '에스프레소': 1900, '카페라떼': 2500, '카푸치노': 2500, '바닐라라떼': 2900}
b = {'헤이즐럿라떼': 2900, '카페모카': 3300, '밀크커피': 3300, '아메리카노': 1900, '샷크린티라떼': 3300}
b.update(a)
result = set(filter(lambda item: item[1] >= 3000, b.items()))
print(result)

# 셋과 딕셔너리 연습문제 5
fruit = ['   apple    ','banana','  melon']
dic = {fruit[i].strip() : len(fruit[i].strip()) for i in range(len(fruit))}
print(dic)

# 셋과 딕셔너리 연습문제 6
num = int(input("Enter your number: "))
dic = {i : i**2 for i in range(1, num + 1)}
print(dic)

# 셋과 딕셔너리 연습문제 7
a = 'hello world! 123'
new_a = list(a)
count_letter = 0
count_digit = 0
for i in range(len(new_a)):
  if 'a' <= new_a[i] <= 'z':
    count_letter += 1
  elif new_a[i].isdigit():
    count_digit += 1
print(count_letter, count_digit)

# 셋과 딕셔너리 연습문제 9
beer = {'하이트': 2000, '카스': 2100, '칭따오': 2500, '하이네켄': 4000, '버드와이저': 500}
new_beer = {item[0] : item[1] * 1.05 for item in beer.items()}
print(new_beer)

# 문자열 연습문제 2
a = "A better tomorrow"
new_a = a.split()
new_b = new_a[::-1]
result = ""
for i in range(len(new_b)):
  print(new_b[i], end = " ")

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
a = 'H1e2l3l4o5w6o7r8l9d'
list_a = list(map(str, a))
result = ""
for i in range(len(list_a)):
  if i % 2 == 0:
    result += list_a[i]
print(result)
```

