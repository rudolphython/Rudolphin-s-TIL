## 리스트와 튜플 연습문제 풀이

# python

```
# # 리스트와 튜플 연습문제 18
# a = input()
# t_list = list(map(int, a.split(', ')))
# result = []
# for i in range(t_list[0]):
#    temp = []
#    for j in range(t_list[1]):
#       temp.append(i*j)
#    result.append(temp)
# print(result)

# # 리스트와 튜플 연습문제 19
# a = input("단어를 입력하시오: ")
# a_list = list(map(str, a.split(',')))
# result = ', '.join(sorted(a_list))
# # join() 함수는 리스트를 인수로 받아서 문자열 하나로 만들 수 있음.
# print(result)

# # 리스트와 튜플 연습문제 20
# a = input("숫자를 입력하시오: ")
# a_list = list(map(int, a.split(',')))
# # split() 함수는 문자열을 분리할 때 사용함.
# result = [i for i in a_list if i & 1]
# print(','.join(map(str, result)))

# # 리스트와 튜플 연습문제 21
# a = (1,2,3,4,5,6,7,8,9,10)
# front_list = a[0:5]
# end_list = a[5:10]
# print(front_list)
# print(end_list)

# # 리스트와 튜플 연습문제 22
# a = [5, 6, 77, 45, 22, 12, 24]
# t = [i for i in a if i % 2 != 0]
# print(t)

# # 리스트와 튜플 연습문제 23
# a = [12, 24, 35, 70, 88, 120, 155]
# b= [sym for idx, sym in enumerate(a) if idx % 2 != 0]
# print(b)
# # enumerate() 함수는 enumerate(리스트명, 인덱스의 시작값)으로 쓴다.
# # 리스트 내포 : [표현식 for 변수 in 반복자료형 if 조건]

# # 리스트와 튜플 연습문제 24
# a = [0 for i in range(4)]
# b = [a for i in range(3)]
# c = [b for i in range(2)]
# print(c)

# # 리스트와 튜플 연습문제 25
# a = [12, 24, 35, 70, 88, 120, 155]
# b = [sym for idx, sym in enumerate(a) if idx != 0 and idx != 4 and idx != 5]
# print(b)

# # 리스트와 튜플 연습문제 26
# a = [1,3,6,78,35,55]
# b = [12,24,35,24,88,120,155]

# for i in range(0, len(a)):
#        if a[i] in b:
#            print(a[i]) 

# # 리스트와 튜플 연습문제 27
# a = [12,24,35,24,88,120,155,88,120,155]
# list_a = set(a)
# print(sorted(list_a))
# # sorted함수는 매개별수로 들어온 이터러블한 데이터를 새로 정렬된 리스트로 반들어서 반환
```

