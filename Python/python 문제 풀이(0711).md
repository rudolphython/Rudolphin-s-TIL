# # 반복문 연습문제 이해 정리

# python
```
# num = int(input("입력: "))
# array = [0] * 10
# #현재 array: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# result =""
# while num:
#     array[num % 10] += 1
#     #만약 11일 경우, 나머지는 1이므로 array[1]에 1을 추가해라.
#     num //= 10S
#     #만약 11일 경우, 몫인 1이 되고 다시 10의 몫을 구하면 num 값은 0이 됨(num이 0이 될 때까지 반복)
#     #만약 121일 경우, 몫은 12, 다음 몫은 1, 다음 몫은 0이므로 false가 되므로 while 반복문은 종료
# for i in range(0, 10):
#     result += "%d " % array[i]
#     #카운터된 array 값을 보여줘라. array[0] ~ [9]
# print(result)

# # 함수 연습문제 3
# def prime_number():
#     a = int(input("입력: "))
#     count = 0
#     for i in range(1, a +1):
#         if a % i == 0:
#             count += 1
#             if count == 2:
#                 print("소수입니다.")

# prime_number()

# # 함수 연습문제 5

# def set_list():
#     list = [1, 2, 3, 4, 3, 2, 1]
#     set_list = set(list)
#     return set_list

# print(set_list())

# # 함수 연습문제 6
# list = [2, 4, 6, 8, 10]
# a = int(input("입력: "))

# def find_list(list):
#     if a in list:
#         print("%d => True" % (a))
#     else :
#         print("%d => False" % (a))

# find_list(list)

# # 함수 연습문제 8
# def squares(a):
#     print("square(%d) => %d" % (int(a), int(a)**2))

# a = input("입력: ")
# a = a.split(',')
# for i in a:
#     squares(i)
#     # 리스트로 따지면 2개니깐 2번 반복(for 변수 in 리스트)

# # 내장함수 연습문제 1
# import datetime
# name = input("이름 입력: ")
# t = 100 - int(input("나이 입력: "))

# year = datetime.datetime.now().year + t - 1
# print("%s(은)는 %d년에 100세가 될 것 입니다." % (name, year))

# # 내장함수 연습문제 4
# t_str = "ADCBBBBCABBCBDACBDCAACDDDCAABABDBCBCBDBDBDDABBAAAAAAADADBDBCBDABADCADC"
# str_list = list(t_str)
# t = list(map(lambda x : ord('E') - ord(x) , str_list))
# # 람다함수 사용법
# # lambda 인자 : 표현식 => (lambda x, y: x + y)(10, 20)
# # map함수 사용법(map 함수를 쓰기 위해서는 리스트화를 해두자.)
# # map(함수, 리스트) => map(lambda x: x ** 2, range(5))
# print(sum(t))

# 내장함수 연습문제 5
# 가변형 : 지속적으로 데이터를 추가, 삭제하는 것. 예로는 리스트, 딕셔너리가 있음.
# 불변형 : 값을 초기화하면 변경이 불가능한 것. 예로는 정수형, 실수형, 튜플이 있음.
# def sum_list(*a):
#     result = 1
#     for i in a:
#         if type(a) != int:
#             print("에러발생")
#             return
#         result *= i
#     print(result)

# sum_list(1, 2)

# # 내장함수 연습문제 6
# def aaa():
#     a = int(input())
#     print("ASCII %d => %s" % (a, chr(a)))

# aaa()

# # 내장함수 연습문제 7
# # filter 함수 사용법 : filter(함수, 리스트)로 사용(예시: filter(lambda x: x < 5, range(10)))
# a = list(filter(lambda x : x % 2 == 0 , range(1, 11, 1)))
# print(a)

# # 내장함수 연습문제 8
# # map() 함수 사용법 : map(변환할 데이터 타입, 리스트)
# a = list(map(lambda x : x * x, range(1, 11, 1)))
# print(a)

# # 내장함수 연습문제 9
# a = list(filter(lambda x : x % 2 == 0, range(1, 11, 1)))
# b = list(map(lambda x : x * x, a))
# print(b)

# # 내장함수 연습문제 10
# def find_max(*params):
#     b = max(my_list)
#     print("max(3, 5, 4, 1, 8, 10, 2) => %d" % (b))

# my_list = [3, 5, 4, 1, 8, 10, 2]
# find_max()

# # 내장함수 연습문제 11
# # zip() 함수 : 합치는 것. 예시: zip(numbers, letters)
# # items() 함수 : 키-값을 쌍으로 한꺼번에 뽑아내는 함수
# a = "abcdef"
# b = [0, 1, 2, 3, 4, 5]
# c = dict((zip(a, b)))
# for key,val in c.items():
#     print("%s : %d" % (key, val))
```



