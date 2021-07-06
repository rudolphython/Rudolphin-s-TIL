# 7월 6일 문제 풀이
```python
# 변수 연습문제1 
Num = int(input("0부터 9까지 정수를 입력해주세요.: "))
if 0 < Num <= 9:
    print(Num + Num*10 + Num + Num*100 +Num*10 + Num + Num*1000 + Num*100 +Num*10 + Num )
else :
    print("올바르지 않은 입력입니다.")

# 연산자 연습문제 1
inp_inch = float(input("입력: "))
print("%.2f inch => %.2f cm" % (inp_inch, inp_inch * 2.54))

# 연산자 연습문제 2
inp_kg = float(input("입력: "))
print("%.2f kg => %.2f lb " % (inp_kg, inp_kg * 2.2046))

# 연산자 연습문제 3
cel = float(input("입력: "))
print("%.2f ℃ => %.2f ℉" % (cel, 180 * 0.28 + 32))

# 연산자 연습문제 4
fah = float(input("입력: "))
print("%.2f ℉ => %.2f ℃" % (fah, (fah - 32) / 180 * 100))

# 연산자 연습문제 5
a = 0.2 * 100
b = 100 + 200
c = a / b * 100
print("혼합된 소금물의 농도: {0:0.2f}%".format(c))

# 흐름제어 연습문제 1
num = int(input("입력: "))
for i in range(1, num + 1):
    if num % i == 0:
        print("%d(은)는 %d의 약수입니다." % (i, num))
        i = i + 1
    else :
        i = i + 1

# 흐름제어 연습문제 2 
num = int(input("입력: "))
k = 0

for i in range(1, num + 1):
    if num % i == 0:
        k = k + 1
        print("%d(은)는 %d의 약수입니다." % (i, num))
        if k == 2:
            print("%d(은)는 %d과 %d로만 나눌 수 있는 소수입니다." % (num, 1, num))

# 흐름제어 연습문제 3
alp = str((input("입력: ")))
if 'a' <= alp <= 'z':
    print("%s는 소문자입니다." %(alp))
elif 'A' <= alp <= 'Z':
    print("%s는 대문자입니다." %(alp))
```
