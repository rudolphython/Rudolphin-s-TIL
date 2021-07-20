## 제어, 반복 문제 풀이


```py
# 1. 네모 출력
n, m = 3, 4
star_row = '*' * n + '\n'
print((star_row) * m)

# 2. 근의 공식
a = int(input('Enter your number: '))
b = int(input('Enter your number: '))
c = int(input('Enter your number: '))

x1 = (-b + ((b**2 -4*a*c)**(1/2))) / 2*a
x2 = (-b - ((b**2 -4*a*c)**(1/2))) / 2*a

print(x1, x2)

# 3. 숫자 피라미드 만들기
my_num = int(input("Enter your number: "))
for i in range(1, my_num + 1):
    for j in range(1, i + 1):
        print(j, end="")
    print()
```