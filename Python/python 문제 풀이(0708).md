# # 연산자 연습문제 5(소숫점 문제 되풀이)
# a = (0.2 * 100 / 300 ) * 100
# print("혼합된 소금물의 농도: {0:0.2f}%".format(a))

# # 흐름제어 연습문제 2(소수 문제 되풀기)
# a = int(input("입력: "))
# cou = 0
# for i in range(1, a + 1):
#     if a % i == 0:
#         cou += 1
#         if cou == 2:
#             print("%d(은)는 1과 %d로만 나눌 수 있는 소수입니다." % (a,a))

# 흐름제어 연습문제 3(대소문자 구분하기)
# alp = str(input("입력: "))
# if alp.islower():
#     print("소문자입니다.")
# else :
#     print("대문자입니다.")

# # 흐름제어 연습문제 4(리스트 활용 문제)
# rsp = ["가위", "바위", "보"]
# a = input("입력: ")
# b = input("입력: ")
# if a == rsp[0]:
#     if b == rsp[0]:     
#         print("DRAW")

# # 흐름제어 연습문제 5(아스키 코드 변환 내장함수 연습)
# a = input("입력: ")
# print("{0}, {1}, {2}, {3}".format(a, a.upper(), ord(a), ord(a.upper())))

# # 흐름제어 연습문제 7(append 함수 및 join 함수 연습)
# result = ""
# for i in range(1, 201):
#     if i % 5 == 0:
#         result =  result + "%d," % i 
# print(result[:-1])

# # 반복문 연습문제 7(pop함수에 대한 이해)
# i = 0
# tot = 0
# scores = [85, 65, 77, 83, 75, 22, 98, 88, 38, 100]
# sc_len = len(scores)

# while i < sc_len:
#     NSC = scores.pop()
#     if NSC >= 80:
#         tot = tot + NSC
#     i = i + 1 
# print(tot)

# # 반복문 연습문제 10
# array = [0]*10
# num = int(input("입력: "))
# result = ""
# #num이 0이 될때까지 반복하며 숫자체크
# #while 반복문은 참일 때만 실행, False(0)을 만들기
# while num:
#     array[num % 10] += 1
#     num //= 10
# for i in range(0, 10):
#     result += "%d " % i
# print(result)
# result = ""
# for i in range(0, 10):
#     result += "%d " % array[i]
# print(result)

# # 함수 연습문제 1
# a = str(input("입력: "))

# def rev_word(a):
#     rev_word = a[: : -1]
#     return rev_word

# print(rev_word(a))

# #  함수 연습문제 3
# my_list = [1, 2, 3, 4, 3, 2, 1]

# def new_list(my_list):
#     new_list = set(my_list)
#     return new_list

# print(new_list(my_list))

# # 함수 연습문제 5
# mylist = [2, 4, 6, 8, 10]
# len_list = len(mylist)
# a = int(input("숫자 입력: "))

# def asd(mylist):
#     if a in mylist:
#         print("True")
#     else :
#         print("False")

# asd(mylist)

# # 함수 연습문제 8
# def square(k):
#     print("squares(%d) => %d" % (int(k), int(k)**2))

# k = input()
# k = k.split(',')
# for i in k:
#     square(i)

# 내장함수 연습문제 1

