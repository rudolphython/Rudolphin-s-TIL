## 리스트와 튜플 연습문제 풀이

# python

```
# # 리스트와 튜플 연습문제 1
# count = 0
# a = (90, 80)
# b = (85, 75)
# c = (90, 100)

# print("%d 학생의 총점은 %d점이고, 평균은 %0.2f점입니다." % (1, a[0] + a[1], (a[0] + a[1]) / 2))
# print("%d 학생의 총점은 %d점이고, 평균은 %0.2f점입니다." % (2, b[0] + b[1], (b[0] + b[1]) / 2))
# print("%d 학생의 총점은 %d점이고, 평균은 %0.2f점입니다." % (3, c[0] + c[1], (c[0] + c[1]) / 2))

# # 리스트와 튜플 연습문제 2
# # 리스트 내포 : for문과 if문을 활용하는 것. [표현식 for 변수 in 반복자료형 if 조건]
# a = 'Python is powerful... and fast; plays well with others; runs everywhere; is friendly & easy to learn; is Open.'
# b = 'aeiou'
# result = [i for i in a if i not in b]
# print("".join(result))
# # join함수는 리스트를 문자열로 합쳐서 반환해주는 것임.

# # 리스트와 튜플 연습문제 3
# result_list = []
# for i in range(2, 10):
#    temp_list = []
#    for j in range(1, 10):
#       t = i*j
#       #3의 배수이거나 7의 배수라면 continue. 즉, 아래 코드로 진행(3과 7의 배수는 appped하지 않겠다라는 뜻)
#       if not (t % 3) or not (t % 7):
#       #3의 배수도 아니고 7의 배수도 아니면 참. 즉, continue 됨.
#          continue
#       temp_list.append(t)
#    result_list.append(temp_list)
# print(result_list)

# # 리스트와 튜플 연습문제 4
# data_list = [int(input()) for i in range(5)]
# print("입력된 값 {0}의 평균은 {1:0.1F}입니다.".format(data_list, sum(data_list)/len(data_list)))

# 리스트와 튜플 연습문제 6
# a = int(input("숫자를 입력하시오.: "))
# arr = []
# for i in range(1, a + 1, 1):
#     if a % i == 0 :
#         arr.append(i)

# print(arr)

# # 리스트와 튜플 연습문제 9
# my_list = [1, 3, 11, 15, 23, 28, 37, 52, 85, 100]

# data_list = [i for i in my_list if i % 2 == 0]
# # 리스트 내포 : for문과 if문을 활용하는 것. [표현식 for 변수 in 반복자료형 if 조건]
# print(data_list)

# #리스트와 튜플 연습문제 10
# def fibo(x):
#     if x == 1 or x == 2:
#         return 1
#     return fibo(x-1) + fibo(x-2)
# result = [fibo(i) for i in range(1,11)]
# print(result)

# # 리스트와 튜플 연습문제 12
# result = [i * i for i in range(1, 21) if i % 3 or i % 5 ]
# print(result)

# # 리스트와 튜플 연습문제 13
# a = input("숫자를 입력하시오: ")
# tot = 0
# for i in a:
#     tot = tot + int(i)
# print(tot)

# # 리스트와 튜플 연습문제 14
# dicBase = (('가','깋'), ('나','닣'), ('다','딯'), ('라','맇'), ('마','밓'), ('바','빟'), ('사','싷'),('아','잏'),
#  ('자','짛'), ('차','칳'), ('카','킿'), ('타','팋'), ('파','핗'), ('하','힣'))
# inputWord = ['막', '부모님', '비용', '비행기', '원래', '처리', '최초', '꼴', '좀', '들다', '싶다',
# '수출', '계시다', '다', '뒤', '듣다', '함께', '아이', '무척', '보이다', '가지다', '그',
# '자르다', '데리다', '마리', '개', '정도', '옳다', '놀이','뜨겁다']

# reuslt = []
# for i in dicBase:
#    temp = [k for k in inputWord if i[0] <= k <= i[1]]
#    reuslt.append(temp)
# print(reuslt)

# # 리스트와 튜플 연습문제 15
# # map() 함수 사용해야함!
# a = input("숫자를 입력하시오: ")
# b_list = list(map(int, a.split(',')))
# b_tuple = tuple(map(int, a.split(',')))
# print(b_list)
# print(b_tuple)

# # 리스트와 튜플 연습문제 16
# from math import pi
# a = input("숫자를 입력하시오: ")
# a_list = list(map(int, a.split(',')))
# result = ""
# for r in a_list:
#     result += "%0.2f, " % (2*pi*r)
# print(result[: -2])
```

