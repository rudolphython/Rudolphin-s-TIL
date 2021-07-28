### 객체지향 문제풀이(0729)

```python
# 객체지향 연습문제 1
class Grade:
    def __init__(self, kor, eng, math):
        self.kor = kor
        self.eng = eng
        self.math = math

    def total(self):
        print(f'총점은 {self.kor + self.eng + self.math}입니다.') 

g1 = Grade(89, 90, 100)
g1.total()


# 객체지향 연습문제 2
class Korean:

    @staticmethod
    def staticmethod():
        return '대한민국'

print(Korean.staticmethod())

# 객체지향 연습문제 3
class Student:
    def __init__(self, name):
        self.name = name

    def talk_my_name(self):
        print(f'이름:{self.name}')

class GraduateStudent(Student):
    def __init__(self, name, major):
        super().__init__(name)
        self.major = major

    def talk_my_name(self):
        print(f'이름:{self.name}, 전공:{self.major}')

a1 = Student('홍길동')
b1 = GraduateStudent('이순신', '컴퓨터공학과')

a1.talk_my_name()
b1.talk_my_name()

# 객체지향 연습문제 4
class Circle:
    pi = 3.14
    r = 2

    def __init__(self, r):
        r.self = r

    def calc_area():
        return Circle.pi * (Circle.r **2)

print(Circle.calc_area())

# 객체지향 연습문제 5
class Shape:
    def __init__(self, length):
        self.length = length

    def calc_area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        super().__init__(length)

    def calc_area(self):
        return self.length * self.length

r = Square(3)
print(r.calc_area())

# 객체지향 연습문제 6
class Person:
    def __init__(self, sex):
        self.sex = sex

    def getGender(self):
        return "Unknown"
    
class Male(Person):
    def __init__(self, sex):
        super().__init__(sex)

    def getGender(self):
        return self.sex

class Female(Person):
    def __init__(self, sex):
        super().__init__(sex)

    def getGender(self):
        return self.sex

m1 = Male('Male')
w1 = Female('Female')

print(m1.getGender())
print(w1.getGender())
```

