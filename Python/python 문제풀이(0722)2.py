# 셋과 딕셔너리 연습문제 1
my_dict = {
    '홍길동': '010-1111-1111',
    '이순신': '010-1111-2222',
    '강감찬': '010-1111-3333'
}

print('아래 학생들의 전화번호를 조회할 수 있습니다.')
for i in my_dict.keys():
    print(i)
a = input('전화번호를 조회하고자 하는 학생의 이름을 입력하시오.: ')
print(f'{a}의 전화번호는 {my_dict[a]}입니다.')

# 셋과 딕셔너리 연습문제 4
fruit = ['apple','banana','melon']

my_dict = {fruit[i] : len(fruit[i]) for i in range(len(fruit))}

print(my_dict)

# 셋과 딕셔너리 연습문제 6
number = int(input("숫자를 입력하세요: "))
my_dict = {i : i ** 2 for i in range(1, number + 1)}
print(my_dict)

# 셋과 딕셔너리 연습문제 8
a = 'Hello World! 123'
list1 = list(a)
count = 0
for i in list1:
    if i.isupper():
        count += 1

print(count)

# 셋과 딕셔너리 연습문제 9
beer = {'하이트': 2000, '카스': 2100, '칭따오': 2500, '하이네켄': 4000, '버드와이저': 500}
for key in beer.keys():
    beer[key] = beer[key] * 1.05

print(beer)
